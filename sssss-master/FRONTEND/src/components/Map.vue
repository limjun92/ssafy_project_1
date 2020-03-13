<template>

    <div  style="height:100%;">
        <div class="d-flex flex-row-reverse" >
            <MapSearch v-bind:class="{hide:dragging}" @search_placename_type="search"/>
        </div>  

        <div id="container" style="height:100%;">
            <div id="rvWrapper">
                <div id="roadview" style="width:100%;height:100%;"></div> <!-- 로드뷰를 표시할 div 입니다 -->
                <!-- <div id="close" title="로드뷰닫기" @click="closeRoadview()"><span class="img"></span></div> -->
            </div>
            <div class="map_wrap" id = "mapWrapper">
                <div id="map" style="width:100%;height:100%"></div>
                
                <div id="roadviewControl" @click="setRoadviewRoad()" class="button-like shadow bg-white rounded">
                    <v-icon style="left: 15%; top:20%; color:#FF4081;">mdi-alpha-l-circle-outline</v-icon>
                </div>
                <div id="trafficviewControl" @click="setOverlayMapTypeId()" class="button-like shadow bg-white rounded">
                    <v-icon style="left: 15%; top:20%; color:#FF4081;">mdi-alpha-t-circle-outline</v-icon>
                </div>
                <div class="">
                    <div class="button-like shadow bg-white rounded" style="top:80px;">            
                        <span @click="geolocation_me_first_button"><v-icon style="left: 15%; top:20%; color:#FF4081;">mdi-crosshairs-gps</v-icon></span>
                    </div>
                    <div id="cafe_filter" class="button-like shadow bg-white rounded button-border" style="top:125px;">
                        <span @click="cafe_filter($event)"><v-icon style="left: 10%; top:15%; color:#FF4081;">mdi-coffee</v-icon></span>
                    </div>
                    <div id="library_filter" class="button-like shadow bg-white rounded button-border" style="top:170px;">
                        <span @click="library_filter($event)"><v-icon style="left: 13%; top:15%; color:#FF4081;">mdi-book-open-page-variant</v-icon></span>
                    </div>
                    <div id="study_filter" class="button-like shadow bg-white rounded button-border" style="top:215px;">
                        <span @click="study_filter($event)"><v-icon style="left: 13%; top:12%; color:#FF4081;">mdi-lead-pencil</v-icon></span>
                    </div>
                    <div id="like_filter" class="button-like shadow bg-white rounded button-border" style="top:260px;">
                        <span @click="like_filter($event)"><v-icon style="left: 10%; top:15%; color:#FF4081;">mdi-cards-heart</v-icon></span>
                    </div>     
                </div>   
            </div>
        </div>

        
    </div>

    
</template>



<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>



<script>
import MapSearch from "./MapSearch"
import axios_common from '../axios_common';
const kakao = window.kakao
export default {
    data() {
        return {
            dragging:false,
            map:{},
            infowindow:{},
            placename:'',
            placename_type:'',
            ps:{},
            che:true,
            markers:[],
            markers_library:[],
            markers_study:[],
            markers_db:[],
            markers_library_db:[],
            markers_study_db:[],
            placeOverlay:{},
            contentNode:'',
            listEl:'',
            CustomOverlay:{},
            first_y:-1,
            first_x:-1,
            db_place_data:[],
            db_my_data:[],
            db_userview_noi:[],
            db_userview_lig:[],
            db_userview_se:[],
            db_userview_and_myfa:[],
            my_place_like:[],
            i_dont_like_here:[],         
            db_place_data_all:[],  
            db_in_markers:[],
            placekeyword:{},      
            out_db_place_data:[],
            
            center_latlng:{},
            center_level:-1,

            overlayOn:false, // 지도 위에 로드뷰 오버레이가 추가된 상태를 가지고 있을 변수
            container:{},
            mapWrapper:{},
            mapContainer:{},
            rvContainer:{},
            rv:{},
            rvClient:{},

            road_marker:{},
            traffic_check:false,

            db_lotate_check:0,
            db_lotate_check_clusterer:0,

            clusterer:{},

            window_width:-1,
            address_name_count :0,
            place_name_count :0,
            category_name_count :0,
            data_length: 0,
            if_got_locate:0,
            if_got_locate_locate:false,
            category_include:0,
            in_db_place_data:[],
            
            str_check_2:'',

            str_incluses:0,

            db_check:true,
            just_one:true,
//////////////////////
        }
    },
    components:{
        MapSearch,  
    },
    updated() {
        this.$nextTick(function () {
        });
    },
    computed: {
        isAuthenticated() {
            return this.$store.getters.isAuthenticated;
        },
        userid(){
            return this.$store.getters.userId;
        },
        requestHeader(){
            return this.$store.getters.requestHeader;
        }
    },

    methods: {      
        about_roadview(){
            var markImage = new kakao.maps.MarkerImage(
            'https://t1.daumcdn.net/localimg/localimages/07/2018/pc/roadview_minimap_wk_2018.png',
            new kakao.maps.Size(26, 46),
            {
                        // 스프라이트 이미지를 사용합니다.
                        // 스프라이트 이미지 전체의 크기를 지정하고
                spriteSize: new kakao.maps.Size(1666, 168),
                        // 사용하고 싶은 영역의 좌상단 좌표를 입력합니다.
                        // background-position으로 지정하는 값이며 부호는 반대입니다.
                spriteOrigin: new kakao.maps.Point(705, 114),
                offset: new kakao.maps.Point(13, 46)
            }
        );    
        var map = this.map;

        this.road_marker = new kakao.maps.Marker({
            image : markImage,
            position: map.getCenter(),
            draggable: true
        });

        var road_marker = this.road_marker;

        //var rv = this.rv;
        var overlayOn = this.overlayOn;

        var rv = this.rv;

        kakao.maps.event.addListener(rv, 'position_changed', function() {

            // 현재 로드뷰의 위치 좌표를 얻어옵니다 
            var rvPosition = rv.getPosition();

            // 지도의 중심을 현재 로드뷰의 위치로 설정합니다
            map.setCenter(rvPosition);

            // 지도 위에 로드뷰 도로 오버레이가 추가된 상태이면
            // if(overlayOn) {
            //     // 마커의 위치를 현재 로드뷰의 위치로 설정합니다
                road_marker.setPosition(rvPosition);
            // }
        });

        var toggleRoadview = this.toggleRoadview

        kakao.maps.event.addListener(road_marker, 'dragend', function(mouseEvent) {

            // 현재 마커가 놓인 자리의 좌표입니다 
            var position = road_marker.getPosition();

            // 마커가 놓인 위치를 기준으로 로드뷰를 설정합니다
            toggleRoadview(position);
        });

        var check_click = this.check_click

        kakao.maps.event.addListener(map, 'click', function(mouseEvent){
        
            if(!check_click()){
                return;
            }

            var position = mouseEvent.latLng;
                // 마커를 클릭한 위치로 옮깁니다
            road_marker.setPosition(position);
                // 클락한 위치를 기준으로 로드뷰를 설정합니다
            toggleRoadview(position);
            // 클릭한 위치의 좌표입니다 
        });

        }  ,
        setOverlayMapTypeId() {
            
            var control = document.getElementById('trafficviewControl');

            // 버튼이 눌린 상태가 아니면
            
                if(!this.traffic_check){
                    this.map.addOverlayMapTypeId(kakao.maps.MapTypeId.TRAFFIC);
                    control.className = 'active'
                    this.traffic_check = true;
                }else{
                    this.map.removeOverlayMapTypeId(kakao.maps.MapTypeId.TRAFFIC); 
                    this.traffic_check = false; 
                    control.className = '';
                }
            
        },
        check_click(){
            return this.overlayOn
            // if(this.overlayOn){
            //     var position = mouseEvent.latLng;
            //     // 마커를 클릭한 위치로 옮깁니다
            //     this.road_marker.setPosition(position);
            //     // 클락한 위치를 기준으로 로드뷰를 설정합니다
            //     this.toggleRoadview(position);
            // }
        },
        toggleRoadview(position){

            //var position=  new kakao.maps.LatLng(33.45042 , 126.57091)

            var toggleMapWrapper = this.toggleMapWrapper;

            var rv = this.rv;

            this.rvClient.getNearestPanoId(position, 50, function(panoId) {
                // 파노라마 ID가 null 이면 로드뷰를 숨깁니다
                if (panoId === null) {
                    toggleMapWrapper(true, position);
                } else {
                    toggleMapWrapper(false, position);

                    // panoId로 로드뷰를 설정합니다
                    rv.setPanoId(panoId, position);
                }
            });
        },

        toggleMapWrapper(active, position) {
            if (active) {

                // 지도를 감싸고 있는 div의 너비가 100%가 되도록 class를 변경합니다 
                this.container.className = '';

                // 지도의 크기가 변경되었기 때문에 relayout 함수를 호출합니다
                this.map.relayout();

                // 지도의 너비가 변경될 때 지도중심을 입력받은 위치(position)로 설정합니다
                this.map.setCenter(position);
            } else {
                // 지도만 보여지고 있는 상태이면 지도의 너비가 50%가 되도록 class를 변경하여
                // 로드뷰가 함께 표시되게 합니다
                if (this.container.className.indexOf('view_roadview') === -1) {
                    this.container.className = 'view_roadview';
                    // 지도의 크기가 변경되었기 때문에 relayout 함수를 호출합니다
                    this.map.relayout();
                    // 지도의 너비가 변경될 때 지도중심을 입력받은 위치(position)로 설정합니다
                    this.map.setCenter(position);
                }
            }
        },

        toggleOverlay(active) {
            if (active) {
                this.overlayOn = true;

                // 지도 위에 로드뷰 도로 오버레이를 추가합니다
                this.map.addOverlayMapTypeId(kakao.maps.MapTypeId.ROADVIEW);

                // 지도 위에 마커를 표시합니다
                this.road_marker.setMap(this.map);

                // 마커의 위치를 지도 중심으로 설정합니다 
                this.road_marker.setPosition(this.map.getCenter());

                // 로드뷰의 위치를 지도 중심으로 설정합니다
                this.toggleRoadview(this.map.getCenter());

            } else {
                this.overlayOn = false;

                // 지도 위의 로드뷰 도로 오버레이를 제거합니다
                this.map.removeOverlayMapTypeId(kakao.maps.MapTypeId.ROADVIEW);

                // 지도 위의 마커를 제거합니다
                this.road_marker.setMap(null);
            }
        },

        setRoadviewRoad() {
            var control = document.getElementById('roadviewControl');

            // 버튼이 눌린 상태가 아니면
            if (control.className.indexOf('active') === -1) {
                control.className = 'active';

                // 로드뷰 도로 오버레이가 보이게 합니다
                this.toggleOverlay(true);
            } else {
                control.className = '';
                
                // 로드뷰 도로 오버레이를 제거합니다
                var position = this.road_marker.getPosition();
                this.toggleMapWrapper(true, position);
                this.toggleOverlay(false);
            }
        },
////////////////////////////////////////////////////


//기본 셋팅 함수들
////////////////////////////////////////////////////


        noi_lig_se_set(){
            this.db_userview_and_myfa[0] = -1;
            for(var i = 0;i<this.db_userview_noi.length;i++){
                if(this.db_userview_noi[i]!=null){
                    var noise = this.db_userview_noi[i]-this.db_my_data.noise1
                    var light = this.db_userview_lig[i]-this.db_my_data.light2
                    var seat = this.db_userview_se[i]-this.db_my_data.seat1
                    if(noise<0){
                        noise*=-1     
                    }
                    if(light<0){
                        light*=-1     
                    }
                    if(seat<0){
                        seat*=-1     
                    }
                    if((noise+light+seat)>=-1&&(noise+light+seat)<=4){
                        this.db_userview_and_myfa.push(noise+light+seat);
                        this.db_place_data.push(this.db_place_data_all[i-1]);
                    }
                }
            }
        },

        data_filter(){
            this.noi_lig_se_set();

            for(var i=0;i<this.db_place_data_all.length;i++){
                var check = false;
                var check2 = false;
                for(var j = 0;j<this.db_place_data_all[i].like_users.length;j++){
                    if(this.db_place_data_all[i].like_users[j].id==this.userid){
                        check = true;
                    }
                }
                for(var k = 0;k<this.db_place_data.length;k++){
                    if(this.db_place_data[k].id==this.db_place_data_all[i].id){
                        check = false;
                    }
                }
                if(check){
                    this.db_place_data.push(this.db_place_data_all[i])
                }
            }

        },

        addEventHandle(target, type, callback) {
            if (target.addEventListener) {
                target.addEventListener(type, callback);
            } else {
                target.attachEvent('on' + type, callback);
            }
        },

        placesSearchCB_location (data, status) {
            if (status === kakao.maps.services.Status.OK) {
                var bounds = new kakao.maps.LatLngBounds();
                for (var i=0; i<data.length; i++) {
                    bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
                }       
                this.map.setBounds(bounds);
            } 
        },
        geolocation_me(){
            if (navigator.geolocation) {
                var setCenter = this.setCenter;
                // GeoLocation을 이용해서 접속 위치를 얻어옵니다
                navigator.geolocation.getCurrentPosition(function(position) {
                    var lat = position.coords.latitude, // 위도
                        lon = position.coords.longitude; // 경도
                    var locPosition = new kakao.maps.LatLng(lat, lon); // 마커가 표시될 위치를 geolocation으로 얻어온 좌표로 생성합니다
                setCenter(locPosition);
                
                });
            } 
        },
        
        // 맵 접속시 내위치를 기반으로 주변 정보 뿌려주기
        geolocation_me_first(){            
            if (navigator.geolocation) {
               // console.log("navigator.geolocation",navigator.geolocation)
                var setCenter_first = this.setCenter_first;
                var map = this.map;
                this.search_keyword_type = "OnlyLocation"
                navigator.geolocation.getCurrentPosition(function(position) {
            
                    var lat = position.coords.latitude, // 위도
                        lon = position.coords.longitude; // 경도
                    var imageSrc = './img/my_position.png';

var position = new kakao.maps.LatLng(lat, lon);
            var imageSize = new kakao.maps.Size(30, 30);
            var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);

            var marker = new kakao.maps.Marker({
                     position: position, // 마커의 위치
                     image: markerImage 
                 });
            
            marker.setMap(map); // 지도 위에 마커를 표출합니다


                    if(sessionStorage.getItem('lat')!=null&&sessionStorage.getItem('lng')!=null){
                        map.setLevel(sessionStorage.getItem('level'));
                        lat = sessionStorage.getItem('lat');
                        lon = sessionStorage.getItem('lng');
                    }
                    var locPosition = new kakao.maps.LatLng(lat, lon); // 마커가 표시될 위치를 geolocation으로 얻어온 좌표로 생성합니다
                    setCenter_first(locPosition)
           
                });
            } 
        },

        geolocation_me_first_button(){            
            
            if (navigator.geolocation) {
                this.map.setLevel(3);
                var map = this.map 
                var setCenter_first = this.setCenter_first
                navigator.geolocation.getCurrentPosition(function(position) {
                
                    var lat = position.coords.latitude, // 위도
                        lon = position.coords.longitude; // 경도

                    var locPosition = new kakao.maps.LatLng(lat, lon); // 마커가 표시될 위치를 geolocation으로 얻어온 좌표로 생성합니다

                    map.setCenter(locPosition);  
           
                });
            } 
        },

        // 맵 접속시 실행되는 함수
         setCenter_first(locPosition) {
            
            this.map.setCenter(locPosition);  
            this.che = true;
        },
        
        // 스타벅스 검색시 내 위치를 기반으로 스타벅스를 찾아줌
        setCenter(locPosition) {
            this.map.setCenter(locPosition);  
            this.map.setLevel(3);
            this.che = true;
        },
/////////////////////////////////////
//검색 함수들
///////////////////////////////////
        //검색 시작 ======================================================================================
        search(placename_type){
            this.just_one = true;
            this.placename_type = placename_type;
            this.placename = this.placename_type;
            this.placename_type = "";
            var ps = new kakao.maps.services.Places(); 
            ps.keywordSearch(this.placename, this.place_type);
            this.if_got_locate = 0;
            this.if_got_locate_locate = false;
            this.che = false;
        },

        //검색받은 키워드 타입 확인 ======================================================================================
        place_type(data){
            this.str_check_2 = data[0].address_name.substring(0,2);
            this.data_length = data.length;

            this.str_incluses = 0;
            this.address_name_count=0;
            this.category_name_count=0;
            this.place_name_count=0;

            this.category_include=0;

            //if_got_locate = false;
            if(data!=null)
            

            for (var i=0; i<data.length; i++) {
                //광주
                if(data[i].address_name.includes(this.placename)){
                    this.address_name_count++;
                }
                //상무지구
                if(data[i].category_name.includes(this.placename)){
                    this.category_name_count++;
                }
                if(data[i].place_name.includes(this.placename)){
                    this.place_name_count++;
                }
                if(data[i].category_name.includes("카페")||data[i].category_name.includes("도서관")||data[i].category_name.includes("스터디카페")){
                    this.category_include++;
                }
                    for(var j = 0;j<this.placename.length-1;j++){
                        if(data[i].address_name.includes(this.placename.substring(j,j+2))){
                                this.if_got_locate ++; 
                                break;
                        }
                    }
                if(i>0&&data[i].address_name.includes(this.str_check_2)){
                    this.str_incluses++;

                }
            }
            console.log("0 data ",data)
            console.log("1 address_name_count ",this.address_name_count)
            console.log("2 category_name_count ",this.category_name_count)
            console.log("3 place_name_count ",this.place_name_count)
            console.log("4 category_include ",this.category_include)
            console.log("5 if_got_locate ",this.if_got_locate)
            console.log("5 str_incluses ",this.str_incluses)
            if((this.category_name_count>12||this.category_include>12)&&this.if_got_locate<5&&this.str_incluses<10){
                this.search_keyword_type = "OnlyPlace";
            }
            else{
                this.search_keyword_type = "OtherSearchKeyword";
            }

            switch(this.search_keyword_type) {
                case "OnlyPlace":   // 검색어 : '스타벅스'
                    this.che = true;
        
                    this.geolocation_me();
                    this.searchPlaces();
                    break;
                case "OtherSearchKeyword":  // 검색어 : '상무지구', '송정'
           
                    this.che = false;
                    this.ps.keywordSearch(this.placename, this.placesSearchCB_location); 
                    break;
            }
            
        },

        searchPlaces() {
            console.log("this.db_place_data_all",)
            this.placeOverlay.setMap(null);
            this.removeMarker(this.markers);
            this.removeMarker(this.markers_library);
            this.removeMarker(this.markers_study);
            this.removeMarker(this.markers_db);
            this.removeMarker(this.markers_library_db);
            this.removeMarker(this.markers_study_db);
            this.removeMarker(this.i_dont_like_here);
            this.removeMarker(this.db_in_markers);
            this.clusterer.clear();

            var bounds = this.map.getBounds();

            if(this.che){
                console.log(this.che)
                if(this.category_name_count>12||this.category_include>12){
                    console.log("1")
                    this.db_check = false;
                    this.ps.keywordSearch(this.placename, this.placesSearchCB,{bounds: bounds}); 
                }
                else{
                    console.log("2")
                    this.db_check = true;
                    this.ps.keywordSearch("스터디카페", this.placesSearchCB,{bounds: bounds}); 
                     this.ps.keywordSearch("도서관", this.placesSearchCB,{bounds: bounds}); 
                     this.ps.keywordSearch("카페", this.placesSearchCB,{bounds: bounds}); 
                }
            }
            else{console.log(this.che)
                
                 if((this.address_name_count>12&&this.if_got_locate>12)||this.place_name_count>8||this.category_include<5&&this.if_got_locate>12){
                     console.log("1")
                     this.db_check = true;
                     this.ps.keywordSearch("스터디카페", this.placesSearchCB,{bounds: bounds}); 
                     this.ps.keywordSearch("도서관", this.placesSearchCB,{bounds: bounds}); 
                     this.ps.keywordSearch("카페", this.placesSearchCB,{bounds: bounds}); 
                     
                 }
                 else{
                     console.log("2")
                     this.db_check = false;
                     this.ps.keywordSearch(this.placename, this.placesSearchCB,{bounds: bounds}); 
                 }
            }
           
            this.filter();
            
            
        },
        level_change(){

        },
        // 키워드 검색 완료 시 호출되는 콜백함수 입니다
        placesSearchCB(data, status) {
            console.log("asdasd",data)
            if(data.length==0&&this.just_one){
                this.map.setLevel(this.map.getLevel()+1)
            }else{
                this.just_one = false;
            }
            this.clusterer.clear();
            if (status === kakao.maps.services.Status.OK) {
                // 정상적으로 검색이 완료됐으면 지도에 마커를 표출합니다
                this.center_level = this.map.getLevel();
                if(this.center_level<13){
                    this.displayPlaces(data);
                    if(this.db_check){
                        this.displayPlaces_db();
                    }
                }
                else{
                    this.displayPlaces_db_clusterer();
                }
                
                this.filter();
                this.center_latlng = this.map.getCenter();
                
                sessionStorage.setItem('lat', this.center_latlng.getLat());
                sessionStorage.setItem('lng', this.center_latlng.getLng());
                sessionStorage.setItem('level', this.center_level);
            } else if (status === kakao.maps.services.Status.ERROR) {
            alert('검색 결과 중 오류가 발생했습니다.');
            return;
            }
        },

        // 마커 표시와 커스텀 오버레이를 만들어 준다. 
        displayPlaces(places) {

            //[ADD BY LEEK] OVERLAY를 위해서는 두 가지 데이터 타입이 필요함
            //KAKAO OBJECT를 관리하는 LIST,OUR DB OBJECT를 관리하는 LIST
            this.contentNode.innerHTML="";
            //var dbListFromCurrentPos = []
            for(var i = 0;i<places.length;i++){
                var db_check = false;
                //var db_id = 0;
               for(var j = 0;j<this.db_place_data_all.length;j++){
                    if(this.db_place_data_all[j].placeid==places[i].id){
                        db_check = true;            
                        //db_id = this.db_place_data[j].id;
                        this.in_db_place_data.push(this.db_place_data_all[j]);
                        break;
                    }
               }

               if(!db_check){
                   this.out_db_place_data.push(places[i]);
               }

            };

            for ( var i=0; i<this.out_db_place_data.length; i++ ) {
                if(this.out_db_place_data[i]!=null){
                var marker = this.addMarker_1(new kakao.maps.LatLng(this.out_db_place_data[i].y, this.out_db_place_data[i].x),this.out_db_place_data[i],false);
                var displayPlaceInfo = this.displayPlaceInfo;
                var out_db_place_data=  this.out_db_place_data[i];

               var map =  this.map; 
             
                (function(marker, place,place_y,place_x) {
                    kakao.maps.event.addListener(marker, 'click', function() {

                        displayPlaceInfo(place,false,place_y,place_x);
                    });
                })(marker, out_db_place_data,out_db_place_data.y,out_db_place_data.x);
            }}
             for ( var i=0; i<this.in_db_place_data.length; i++ ) {
                if(this.in_db_place_data[i]!=null){
                var marker = this.addMarker_1(new kakao.maps.LatLng(this.in_db_place_data[i].latitude, this.in_db_place_data[i].longitude),this.in_db_place_data[i],true);
                var displayPlaceInfo = this.displayPlaceInfo;
                var in_db_place_data=  this.in_db_place_data[i];

               var map =  this.map; 
             
                (function(marker, place,place_y,place_x) {
                    kakao.maps.event.addListener(marker, 'click', function() {    
        
                        displayPlaceInfo(place,true,place_y,place_x);
                    });
                })(marker, in_db_place_data,in_db_place_data.latitude,in_db_place_data.longitude);
            }}

            this.out_db_place_data = [];
            this.in_db_place_data = [];
            

        },
        displayPlaces_db(){
            // this.db_lotate_check++;
            // if(this.db_lotate_check!=3){
            //     return;
            // }
            this.contentNode.innerHTML="";
            var dbListFromCurrentPos = []
            for(var i = 0;i<this.db_place_data.length;i++){
                var marker = this.db_addMarker(i+1,new kakao.maps.LatLng(this.db_place_data[i].latitude, this.db_place_data[i].longitude),this.db_place_data[i]);

                var displayPlaceInfo = this.displayPlaceInfo;
                var dbIndex = dbListFromCurrentPos[i];
                var our_db_object = this.db_place_data[dbIndex];
                var kakao_object_in_dbdata = this.db_place_data[i];
                var kakao_object_in_dbdata_y = kakao_object_in_dbdata.latitude;
                var kakao_object_in_dbdata_x = kakao_object_in_dbdata.longitude;                

                var db_place_data = this.db_place_data[i];

                (function(marker, place, place_y, place_x) {
                    kakao.maps.event.addListener(marker, 'click', function() {   
                        displayPlaceInfo(place,true,place_y,place_x);
                    });
                })(marker, db_place_data,kakao_object_in_dbdata_y,kakao_object_in_dbdata_x);                 
                //this.filter();
            }
            this.db_lotate_check = 0;
        },
        displayPlaces_db_clusterer(){
            this.db_lotate_check_clusterer++;
            if(this.db_lotate_check_clusterer!=3){
                return;
            }
            for(var i = 0;i<this.db_place_data.length;i++){
                var db_place_data = this.db_place_data[i];

                var imageSrc='';
                var imageSize = new kakao.maps.Size(45, 50);
                if(db_place_data.cafe.length==1){
                   imageSrc = './img/cafe_7.png';
                }
                if(db_place_data.library.length==1){
                    imageSrc = './img/library_7.png';
                }
                if(db_place_data.studycafe.length==1){
                   imageSrc = './img/study_7.png';
                }

                var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);

                var marker = new kakao.maps.Marker({
                     position: new kakao.maps.LatLng(db_place_data.latitude, db_place_data.longitude), // 마커의 위치
                     image: markerImage 
                });

                this.clusterer.addMarker(marker)

            }
            this.db_lotate_check_clusterer = 0;
        },

        db_addMarker(id,position,place){
            var type =100;
            if(this.db_userview_and_myfa[id]!=null){
                type = this.db_userview_and_myfa[id];
            }
                var check_like = false;
                for(var i = 0;i<this.db_place_data[id-1].like_users.length;i++){
                    if(this.db_place_data[id-1].like_users[i].id==this.userid){
                        check_like = true;
                    }
                }

                var imageSrc='';

                if(check_like){
                     imageSize = new kakao.maps.Size(80, 40);
                     imageSrc= './img/하트.png';
                 }else{
                     imageSize = new kakao.maps.Size(0, 0);
                     imageSrc= '';
                 }

                 markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);

                 var markerheart = new kakao.maps.Marker({
                     position: position, // 마커의 위치
                     image: markerImage 
                 });

                markerheart.setMap(this.map);

                if(place.cafe.length==1){
                   imageSrc = './img/cafe_8.png';
                }
                if(place.library.length==1){
                    imageSrc = './img/library_8.png';
                }
                if(place.studycafe.length==1){
                   imageSrc = './img/study_8.png';
                }

                 var imageSize = new kakao.maps.Size(45, 50);  // 마커 이미지의 크기
                 var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);
                 
           
                 var marker = new kakao.maps.Marker({
                     position: position, // 마커의 위치
                     image: markerImage 
                 });
               
                 marker.setMap(this.map); // 지도 위에 마커를 표출합니다
                

                imageSize = new kakao.maps.Size(45, 20);
                if(type<=1){
                    imageSrc = './img/star_3.png';
                }
                else if(type<=2){
                    imageSrc = './img/star_2.png';
                }
                else if(type<=4){
                    imageSrc = './img/star_1.png';
                }
                else{
                    imageSrc = '';
                }

                markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);

                var markerstar = new kakao.maps.Marker({
                     position: position, // 마커의 위치
                     image: markerImage 
                 });

                 markerstar.setMap(this.map);
                 
                 var like_check = false;
                 for(var j = 0;j<place.like_users.length;j++){
                     if(place.like_users[j].id==this.userid){
                         like_check = true;
                     }
                 }
                 if(!like_check){
                     this.i_dont_like_here.push(marker)
                     this.i_dont_like_here.push(markerstar)
                     this.i_dont_like_here.push(markerheart)
                 }

                if(place.cafe.length==1){
                    this.markers_db.push(marker);
                    this.markers_db.push(markerstar);
                    this.markers_db.push(markerheart);
                }
                else if(place.library.length==1){
                    this.markers_library_db.push(marker);
                    this.markers_library_db.push(markerstar);
                    this.markers_library_db.push(markerheart);
                }
                else if(place.studycafe.length==1){
                    this.markers_study_db.push(marker);
                    this.markers_study_db.push(markerstar);
                    this.markers_study_db.push(markerheart);
                }
                 return marker
        },
        
        addMarker_1(position,place,type) {
                var content = '';

                var customOverlay = new kakao.maps.CustomOverlay({
                    position: position,
                    content: content   
                });

                var imageSrc = '';
                if(!type){
                    if(place.category_name.includes("스터디카페")){
                        imageSrc = './img/study_7.png';
                    }else if(place.category_name.includes("카페")){
                        imageSrc = './img/cafe_7.png';
                    }else if(place.category_name.includes("도서관")){
                        imageSrc = './img/library_7.png';
                    }
                }
                else{
                    if(place.cafe.length==1){
                        imageSrc = './img/cafe_8.png';
                    }
                    if(place.library.length==1){
                        imageSrc = './img/library_8.png';
                    }
                    if(place.studycafe.length==1){
                        imageSrc = './img/study_8.png';
                    }
                }

                var imageSize = new kakao.maps.Size(45, 50);  
                var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);
                    
                var marker = new kakao.maps.Marker({
                    position: position, 
                    image: markerImage 
                });

                marker.setMap(this.map); 

                this.i_dont_like_here.push(marker)
                     
                if(!type){
                if(place.category_name.includes("스터디카페")){
                    this.markers_study.push(marker);
                }else if(place.category_name.includes("카페")){
                     this.markers.push(marker);
                }else if(place.category_name.includes("도서관")){
                    this.markers_library.push(marker);
                }
                }
                else{
                    if(place.cafe.length==1){
                    this.markers.push(marker);
                }
                if(place.library.length==1){
                    this.markers_library.push(marker);
                }
                if(place.studycafe.length==1){
                    this.markers_study.push(marker);
                }

                }
            return marker;
        },
        
        removeMarker(markers) {
            for ( var i = 0; i < markers.length; i++ ) {
                markers[i].setMap(null);
            }
            markers.splice(0);
        },
        
        //[ADD BY LEEK] MOVE TO DETAIL PAGE
        moveToDetail(placeid,place_name,place_lat,place_lng,category_group_name,address_name){            
            
            this.$router.push({name:'temdetail', params:{'id':placeid,'place_lat':place_lat,'place_lng':place_lng, 'place_name':place_name,'category_group_name':category_group_name,'address_name':address_name}})//'/detail/'+placeid);
            //this.$router.push('/temdetail')
        },
        //[ADD BY LEEK] DISPLAY CUSTOM OVERLAY WHEN MARKER IS CLICKED        
        async displayPlaceInfo(place,type,place_y,place_x){            
            const isThis = this;
            this.contentNode.innerHTML=""
            var unified_name = "place"
            var imgtag  = ""            
            var placeid = ""
            var right_top_content=""
            var right_bottom_content = ""
            var imgsrc = ""   
            var place_lat = -1;
            var place_lng = -1;
            var resultCategory = ''
            var resultAddress = ''
            if(type == false)
            {   
                //db에 저장되지 않은 장소라면 kakao로 부터 장소 이름을 받아와야 한다.
                placeid = place.id
                unified_name=place.place_name
                place_lat = place.y;
                place_lng = place.x;
                right_top_content = document.createElement('div')
                right_top_content.textContent = "등록된 정보가 없습니다."                
                if(place.category_name.includes("스터디카페")){
                    resultCategory = '스터디카페'
                }else if(place.category_name.includes("카페")){
                    resultCategory = '카페'
                }else if(place.category_name.includes("도서관")){
                    resultCategory = '도서관';
                }                
                resultAddress = place.address_name
                
            }
            else{
                //db에 저장된 장소라면 db로부터 내용을 채워야 한다.
                resultAddress = place.location
                placeid = place.placeid
                unified_name = place.placename                  
                var serverdomain="http://localhost:8000"                
                //var serverdomain="https://i02c102.p.ssafy.io:8000"
                if(place.placepicture.length>0){
                    imgsrc=serverdomain+place.placepicture[0].name
                }                
                // 장소 키워드 정보
                var keyword = await this.getkeywordfromcomment(placeid)

                right_bottom_content = '<span>'
                if(keyword.length >0)
                    right_bottom_content += '<i class="fas fa-hashtag" style="font-size:90%;"></i><span class="mr-2" style="font-size:90%;">'+keyword[0]+'</span>'
                else                    
                    right_bottom_content = ""                    
                if(keyword.length >1)
                    right_bottom_content += '<i class="fas fa-hashtag" style="font-size:90%;"></i><span style="font-size:90%;">'+keyword[1]+'</span>'
                else
                    right_bottom_content += '</span>'
                if(keyword.length > 2){
                    right_bottom_content += '<div class="mt-2"></div>'
                    right_bottom_content += '<i class="fas fa-hashtag" style="font-size:90%;"></i><span style="font-size:90%;">'+keyword[2]+'</span>'
                    right_bottom_content += '</span>'
                }
                else
                    right_bottom_content += '</span>'
                right_top_content=document.createElement('button')
                right_top_content.className = "btn btn-outline-success btn-rounded waves-effect";
                right_top_content.textContent="상세보기";
                right_top_content.addEventListener("click",function(event){                   
                    isThis.moveToDetail(placeid,unified_name,place_lat,place_lng,resultCategory,resultAddress);                   
                });
            }
            if(!imgsrc){
                imgsrc="../../img/information.png"
            }
            imgtag='<img src="'+imgsrc+'" width="73" height="70">'
            var infoDiv = document.createElement('div');
            infoDiv.className="info";                
            var titleDiv = document.createElement('div');            
            var title_text = document.createTextNode(unified_name);            
            titleDiv.addEventListener("click",function(event){
                    isThis.moveToDetail(placeid,unified_name,place_lat,place_lng,resultCategory,resultAddress);
            });
            titleDiv.appendChild(title_text);
            titleDiv.className="title";

            var bodyDiv = document.createElement('div');
            bodyDiv.className="body";
            var body_imgDiv = document.createElement('div');
            body_imgDiv.className="img";            
            body_imgDiv.innerHTML=imgtag           
            bodyDiv.appendChild(body_imgDiv);

            var body_descDiv = document.createElement('div');            
            body_descDiv.className="desc";
           
            var desc_textdiv = document.createElement('div')
            desc_textdiv.appendChild(right_top_content)            
            var desc_hrDiv = document.createElement('hr');
            var desc_hastagDiv = document.createElement('div');
            desc_hastagDiv.className="hashtag ellipsis mt-2";
            if(!right_bottom_content)
            {                
                var button = document.createElement('button');
                button.className = "mt-3 btn btn-outline-success btn-rounded waves-effect";
                button.textContent="상세보기";                
                button.addEventListener("click",function(event){                   
                    isThis.moveToDetail(placeid,unified_name,place_lat,place_lng,resultCategory,resultAddress);                   
                });                
                desc_hastagDiv.appendChild(button);
            }
            else 
                desc_hastagDiv.innerHTML=right_bottom_content;
            body_descDiv.appendChild(desc_textdiv)
            body_descDiv.appendChild(desc_hrDiv);
            body_descDiv.appendChild(desc_hastagDiv);
            bodyDiv.appendChild(body_descDiv);
            var afterDiv = document.createElement('div');
            afterDiv.className="after";

            infoDiv.appendChild(titleDiv);
            infoDiv.appendChild(bodyDiv);
            infoDiv.appendChild(afterDiv);            
            var wrapdiv = document.getElementById('contentNode')  
            this.contentNode.appendChild(infoDiv)            
            this.placeOverlay.setPosition(new kakao.maps.LatLng(place_y, place_x));
            this.placeOverlay.setMap(this.map);  

        },
        
        filter(){
            
            this.study();
            this.library();
            this.cafe();
            this.like();
        },


        setMarkers(map,markers) {
        for (var i = 0; i < markers.length; i++) {
                    markers[i].setMap(map);
            }         
        },
        showMarkers() {   
            this.setMarkers(this.map,this.markers)
            this.setMarkers(this.map,this.markers_db)              
        },
        hideMarkers() {
            this.setMarkers(null,this.markers);
            this.setMarkers(null,this.markers_db);
        },
        showMarkers_library() {
            this.setMarkers(this.map,this.markers_library)
            this.setMarkers(this.map,this.markers_library_db)  
            
        },
        hideMarkers_library() {
           this.setMarkers(null,this.markers_library);
           this.setMarkers(null,this.markers_library_db);
        },
        showMarkers_study() {
            this.setMarkers(this.map,this.markers_study)        
            this.setMarkers(this.map,this.markers_study_db)       
        },
        hideMarkers_study() {
            this.setMarkers(null,this.markers_study);
            this.setMarkers(null,this.markers_study_db);
        },

        showMarkers_like() {
            this.setMarkers(this.map,this.i_dont_like_here);
        },
        hideMarkers_like() {
            this.setMarkers(null,this.i_dont_like_here);       
        },
        like_filter(e){
            var parent = e.target.parentNode.parentNode
            parent.classList.toggle('button-border')            
            this.like();
        },
        cafe_filter(e){
             var parent = e.target.parentNode.parentNode
            parent.classList.toggle('button-border')            
            this.cafe();
        },
        library_filter(e){
             var parent = e.target.parentNode.parentNode
            parent.classList.toggle('button-border')            
            this.library();
        },
        study_filter(e){
             var parent = e.target.parentNode.parentNode
            parent.classList.toggle('button-border')            
            this.study();
        },

        like(){
            var tmp = document.getElementById('like_filter').classList.contains("button-border")
            if(!tmp){
                this.hideMarkers_like()
            }
            else{
                this.showMarkers_like()
                if(!document.getElementById('cafe_filter').classList.contains("button-border")){
                     this.hideMarkers()
                 }
                 if(!document.getElementById('library_filter').classList.contains("button-border")){
                     this.hideMarkers_library()
                 }
                 if(!document.getElementById('study_filter').classList.contains("button-border")){
                     this.hideMarkers_study()
                 }
            }
        },
        cafe(){
            var tmp = true;
            if(!document.getElementById('cafe_filter').classList.contains("button-border"))
                tmp = false;
            if(tmp){
                this.showMarkers()
                if(!document.getElementById('like_filter').classList.contains("button-border")){
                    this.hideMarkers_like()
                }
            }
            else{
                this.hideMarkers()
            }
        },
        library(){
            var tmp = document.getElementById('library_filter').classList.contains("button-border")
            if(tmp){
                this.showMarkers_library();
                if(!document.getElementById('like_filter').classList.contains("button-border")){
                    this.hideMarkers_like()
                }
            }
            else{
                this.hideMarkers_library()
            }
        },
        study(){
            var tmp = document.getElementById('study_filter').classList.contains("button-border")
            if(tmp){
                this.showMarkers_study()
                if(!document.getElementById('like_filter').classList.contains("button-border")){
                    this.hideMarkers_like()
                }
            }
            else{
                this.hideMarkers_study()
            }
        },

        // DB에 저장되어 있는 키워드 가져오기
        async getkeywordfromcomment(placeid){
            var keywordList = {'result':'false', 'data':["조용함", "좌석이 편안한", "맛있는"]}              
            await axios_common.get('/place/'+placeid+'/keyword/')
            .then((res)=> {
                keywordList = res.data.data
            }).catch(error => console.log(error))
            return keywordList            
        },
        startDrag() {            
            this.dragging = true;
        },
        stopDrag() {            
            this.dragging = false;
        },        
    },
    
    async mounted() {
            
            await axios_common.get(`/place/`)
            .then((res)=> {
                this.db_place_data_all = res.data;
            })
            .catch(error => console.log(error))
            await axios_common.get(`/place/userreview_all/`)
            .then((res)=> {                    
                    var noi = []
                    var lig = []
                    var se = []
                    var count = []
                    var noiavg = []
                    var ligavg = []
                    var seavg = []
                    var max = 0;
                    for(var i = 0;i<res.data.length;i++){
                        if(max<res.data[i].place){
                            max = res.data[i].place
                        }
                        if(noi[res.data[i].place]==null){
                            noi[res.data[i].place] = res.data[i].noise;
                            lig[res.data[i].place] = res.data[i].light;
                            se[res.data[i].place] = res.data[i].seat;
                            count[res.data[i].place] = 1;
                        }
                        else{
                            noi[res.data[i].place] += res.data[i].noise;
                            lig[res.data[i].place] += res.data[i].light;
                            se[res.data[i].place] += res.data[i].seat;
                            count[res.data[i].place] += 1;
                        }
                    }
                    for(var j = 1;j<=max;j++){
                        if(noi[j]!=null){
                            noiavg[j] = noi[j]/count[j]
                            ligavg[j]= lig[j]/count[j]
                            seavg[j]= se[j]/count[j]
                        }
                    }
                    this.db_userview_noi = noiavg
                    this.db_userview_lig= ligavg
                    this.db_userview_se= seavg                    
            })
            .catch(error => console.log(error))
            if(this.isAuthenticated){
                await axios_common.get(`userInfo/${this.userid}/`,this.requestHeader)
                .then((res)=>{
                    this.db_my_data = res.data;
                })
                .catch(error => console.log(error))
            }


        // 마커를 클릭하면 장소명을 표출할 인포윈도우 입니다
        this.infowindow = new kakao.maps.InfoWindow({zIndex:1});
        this.CustomOverlay = new kakao.maps.CustomOverlay({zIndex:1});
        this.placeOverlay = new kakao.maps.CustomOverlay({zIndex:1});
        this.contentNode = document.createElement('div');        
        this.contentNode.id='contentNode'
        this.contentNode.className = 'wrap';
        var mapContainer = document.getElementById('map'), // 지도를 표시할 div 
            mapOption = {
                center: new kakao.maps.LatLng(37.566826, 126.9786567), // 지도의 중심좌표
                level: 3 // 지도의 확대 레벨
            };  
        // 지도를 생성합니다    
        this.container = document.getElementById('container'); // 지도와 로드뷰를 감싸고 있는 div 입니다
        this.mapWrapper = document.getElementById('mapWrapper'); // 지도를 감싸고 있는 div 입니다
        this.mapContainer = document.getElementById('map'); // 지도를 표시할 div 입니다 
        this.rvContainer = document.getElementById('roadview');
        this.map = new kakao.maps.Map(mapContainer, mapOption); 
        this.rv = new kakao.maps.Roadview(this.rvContainer); 
        this.rvClient = new kakao.maps.RoadviewClient(); 
        // 장소 검색 객체를 생성합니다


        //////////////// 맵 변화에 액션
        kakao.maps.event.addListener(this.map, 'idle', this.searchPlaces);



        //var ps = new kakao.maps.services.Places(); 
        this.ps = new kakao.maps.services.Places(); 
        this.listEl = document.getElementById('placesList'), 
        //this.menuEl = document.getElementById('menu_wrap'),
        this.fragment = document.createDocumentFragment();
        this.fragment_library = document.createDocumentFragment();
        this.fragment_study = document.createDocumentFragment();

        ////////////////////////////////////////////

        

        /////////////////////////////////////////////

        var map = this.map
        
        this.clusterer = new kakao.maps.MarkerClusterer({
            map: map, // 마커들을 클러스터로 관리하고 표시할 지도 객체 
            averageCenter: true, // 클러스터에 포함된 마커들의 평균 위치를 클러스터 마커 위치로 설정 
            minLevel: 13, // 클러스터 할 최소 지도 레벨 
            minClusterSize:1
        });
        // this.clusterer_cafe = new kakao.maps.MarkerClusterer({
        //     map: map, // 마커들을 클러스터로 관리하고 표시할 지도 객체 
        //     averageCenter: true, // 클러스터에 포함된 마커들의 평균 위치를 클러스터 마커 위치로 설정 
        //     minLevel: 10, // 클러스터 할 최소 지도 레벨 
        //     minClusterSize:1
        // });
        // this.clusterer_library = new kakao.maps.MarkerClusterer({
        //     map: map, // 마커들을 클러스터로 관리하고 표시할 지도 객체 
        //     averageCenter: true, // 클러스터에 포함된 마커들의 평균 위치를 클러스터 마커 위치로 설정 
        //     minLevel: 10, // 클러스터 할 최소 지도 레벨 
        //     minClusterSize:1
        // });
        // this.clusterer_study = new kakao.maps.MarkerClusterer({
        //     map: map, // 마커들을 클러스터로 관리하고 표시할 지도 객체 
        //     averageCenter: true, // 클러스터에 포함된 마커들의 평균 위치를 클러스터 마커 위치로 설정 
        //     minLevel: 10, // 클러스터 할 최소 지도 레벨 
        //     minClusterSize:1
        // });

        this.addEventHandle(this.contentNode, 'mousedown', kakao.maps.event.preventMap);
        this.addEventHandle(this.contentNode, 'touchstart', kakao.maps.event.preventMap);
        
        this.placeOverlay.setContent(this.contentNode); 

        this.data_filter();

        this.geolocation_me_first();        

        this.displayPlaces_db();        
        kakao.maps.event.addListener(this.map,'dragstart',this.startDrag)
        kakao.maps.event.addListener(this.map,'dragend',this.stopDrag)

        this.about_roadview();

        // window.addEventListener('resize', function() {
        //     this.window_width = $(window).width();
        //     console.log(this.window_wi)
        // }, true);
        
        
    },
}
</script>
<style>
    .map_wrap, .map_wrap * {margin:0; padding:0;font-family:'Malgun Gothic',dotum,'돋움',sans-serif;font-size:12px;}
    .map_wrap {position:relative;width:100%;height:100%;}
    .map_wrap a, .map_wrap a:hover, .map_wrap a:active{color:#000;text-decoration: none;}
    
    .wrap {position: absolute; left:-144px;bottom: 40px;width: 288px;height: 132px;margin-left: -144px;text-align: left;overflow: hidden;font-size: 12px;font-family: 'Malgun Gothic', dotum, '돋움', sans-serif;line-height: 1.5;}
    .wrap * {padding: 0;margin: 0;}
    .wrap .info {width: 286px;height: 120px;border-radius: 5px;border-bottom: 2px solid #ccc;border-right: 1px solid #ccc;overflow: hidden;background: #fff;}
    .wrap .info:nth-child(1) {border: 0;box-shadow: 0px 1px 2px #888;}
    .info .title {text-align: center;text-overflow: ellipsis; padding: 5px 0 0 10px;height: 30px;background: #eee;border-bottom: 1px solid #ddd;font-size: 15px;font-weight: bold;}
    .info .close {position: absolute;top: 10px;right: 10px;color: #888;width: 17px;height: 17px;background: url('http://t1.daumcdn.net/localimg/localimages/07/mapapidoc/overlay_close.png');}
    .info .close:hover {cursor: pointer;}
    .info .body {position: relative;overflow: hidden;}
    .info .desc {position: relative;margin: 13px 0 0 90px;height: 75px; text-align: center;}
    .desc .ellipsis {overflow: hidden;text-overflow: ellipsis;white-space: nowrap;}
    .desc .hashtag {font-size: 11px;color: #888;margin-top: -2px;}
    .desc .hr {padding: 0px;margin:0px;}
    .info .img {position: absolute;top: 6px;left: 5px;width: 73px;height: 71px;border: 1px solid #ddd;color: #888;overflow: hidden;}
    .info:after {content: '';position: absolute;margin-left: -12px;left: 50%;bottom: 0;width: 22px;height: 12px;background: url('http://t1.daumcdn.net/localimg/localimages/07/mapapidoc/vertex_white.png')}    


/* 메튜바 스타일 */

.label {margin-bottom: 96px;}
.label * {display: inline-block;vertical-align: top;}
.label .left {background: url("http://t1.daumcdn.net/localimg/localimages/07/2011/map/storeview/tip_l.png") no-repeat;display: inline-block;height: 24px;overflow: hidden;vertical-align: top;width: 7px;}
.label .center {background: url('http://t1.daumcdn.net/localimg/localimages/07/2011/map/storeview/tip_bg.png') repeat-x;display: inline-block;height: 24px;font-size: 12px;line-height: 24px;}
.label .right {background: url("http://t1.daumcdn.net/localimg/localimages/07/2011/map/storeview/tip_r.png") -1px 0  no-repeat;display: inline-block;height: 24px;overflow: hidden;width: 6px;}
.hide{visibility: hidden; opacity: 0;}

#container {overflow:hidden;height:100%;position:relative;}
#mapWrapper {width:100%;height:100%;;z-index:1;}
#rvWrapper {width:100%;height:100%;;top:0;right:0;position:absolute;z-index:0;}
#container.view_roadview #mapWrapper {height: 50%;}
#roadviewControl {position:absolute;top:80px;left:10px;width:35px;height:35px;z-index: 1;cursor: pointer; background-color: white; opacity: 0.8;}
#roadviewControl.active {background-position:0 -350px;}
#trafficviewControl {position:absolute;top:125px;left:10px;width:35px;height:35px;z-index: 1;cursor: pointer; background-color: white; opacity: 0.8;}
#trafficviewControl.active {background-position:0 -350px;}
#close {position: absolute;padding: 4px;top: 5px;left: 5px;cursor: pointer;background: #fff;border-radius: 4px;border: 1px solid #c8c8c8;box-shadow: 0px 1px #888;}
#close .img {display: block;background: url(http://t1.daumcdn.net/localimg/localimages/07/mapapidoc/rv_close.png) no-repeat;width: 14px;height: 14px;}



/*[ADD BY LEEK]*/
.button-like{
    width:35px;height:35px;position:absolute;right:13px;border-radius: 5px;z-index:1;cursor:pointer; background-color: pink; opacity: 0.8;
}
.button-border{
    border: 2px solid #FF4081;
}
</style>



