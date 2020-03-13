<template>
<body>
  

  <v-app>
    <v-container cols="6" sm="6">
      <form method="post" @submit.prevent="registdetail" enctype="multipart/form-data">
      <v-row justify="center">
      <v-card
        col='12'
        class="mx-auto"
        width= "800px"
        :elevation='10'
      >
        <v-img
          v-bind:src="coffeImg4"
          height="280px"
          dark
        >
    
        <v-row class="fill-height d-flex justify-end mx-auto">
          <v-card-title class="white--text d-flex justify-end">
            <div class="d-reverse mx-2 ">
              <h3>
                Please Register Your Place
              </h3>
            </div>
          </v-card-title>
        </v-row>
      </v-img>

      <v-divider class='mx-2'></v-divider>

      

        <h5 class='d-flex justify-start px-4 pt-4'>Basic Information
        </h5>
        <p class="d-flex justify-start px-8 font-weight-light caption grey--text lighten-4--text">
          <v-icon class="font-weight-light body-2 amber--text lighten-2--text mr-2">mdi-book-open-page-variant</v-icon>
            필수 등록 정보 입니다.
        </p>
      <v-divider class='mx-2'></v-divider>

      

      <v-list two-line>


        <v-list-item>
          <v-list-item>
            <v-icon color="light-green darken-2">mdi-home-heart</v-icon>
            <v-list-item-title>매장명 검색</v-list-item-title>
            <v-list-item-title class='mx-2'>
              <div class="form-inline mb-2">
                <label for="inputPassword2" class="sr-only">Password</label>
                <span class="d-flex flex-row">
                <input type="text" class="form-control" style="max-width:166px" v-model="search_keyword" placeholder="지역 장소명">
                <button type="submit" class="btn  ml-2" @click="place_search" style='color:white; background-color:#689F38'><i class="fa fa-search"></i></button> 
                </span>
              </div>
              
            </v-list-item-title>
<!-- 
            <v-list-item-title class='mx-2'>
                  <input type="text" class="form-control text-center" style="max" placeholder="메뉴명" v-model="me.name">
            </v-list-item-title> -->
          </v-list-item>
        </v-list-item>
        <ul>
                <li v-for="(item) in search_result_data" v-bind:key="item.id">
                   {{ item.address_name }} ( {{ item.place_name }} ) <input type="button" value="선택" style="color:blue" @click="place_choice(item)">
                </li>
              </ul>


        <v-list-item>
          <v-list-item>
            <v-icon color="transparent">mdi-home-heart</v-icon>
            <v-list-item-title>매장명</v-list-item-title>
            <v-list-item-title>
              <v-text-field
                ref="name"
                color='light-green lighten-4'
                v-model="Place.placename"
                :rules="[() => !!Place.placename || '매장명을 입력해주세요']"
                required
                placeholder="싸피 스터디카페"
              ></v-text-field>
            </v-list-item-title>
          </v-list-item>
        </v-list-item>

        <v-divider class='mx-2'></v-divider>

        <v-list-item>
          <v-list-item>
            <v-icon color="light-green darken-2">mdi-map-marker-radius-outline</v-icon>
            <v-list-item-title>주소</v-list-item-title>
            <v-list-item-title>
              <v-text-field
                color='light-green lighten-4'
                v-model="Place.location"
                :rules="[() => !!Place.location || '주소를 입력해주세요']"
                placeholder="광주 광역시 하남산단 6번로"
                required
              ></v-text-field>
            </v-list-item-title>
          </v-list-item>
        </v-list-item>

        <v-divider class='mx-2'></v-divider>

        <v-list-item>
          <v-list-item>
            <v-icon color="light-green darken-2">mdi-clock-check-outline</v-icon>
            <v-list-item-title>Opentime</v-list-item-title>
            <v-list-item-title>
              <!-- <v-text-field
                color='light-green lighten-4'
                type='number'
                v-model="Place.opentime"
                :rules="[() => !!Place.opentime || '오픈시간을 입력해주세요']"
                placeholder=""
                required
                min="0"
                max="24"
              ></v-text-field> -->
              <!-- dialog 시작 -->
              <v-dialog
                ref="dialog1"
                id='text'
                v-model="modal1"
                :return-value.sync="time"
                persistent
                color='light-green lighten-4'
                width="290px"
              >
                <template v-slot:activator="{ on }">
                  <v-text-field
                    id='test'
                    v-model="Place.opentime"
                    readonly
                    v-on="on"
                    :rules="[() => !!Place.opentime || '오픈시간을 입력해주세요']"
                    :aria-required="true"
                  ></v-text-field>
                </template>
                <v-time-picker
                  v-if="modal1"
                  v-model="Place.opentime"
                  full-width
                  color='light-green lighten-1'
                  header-color='light-green lighten-2'
                >
                  <v-spacer></v-spacer>
                  <v-btn text color="light-green darken-3" @click="modal1 = false">Cancel</v-btn>
                  <v-btn text color="light-green darken-3" @click="$refs.dialog1.save(Place.opentime)">OK</v-btn>
                </v-time-picker>
              </v-dialog>
              <!-- dialog 끝 -->
              </v-list-item-title>
          </v-list-item>
        </v-list-item>



        <v-list-item>
          <v-list-item>
            <v-icon color="transparent">mdi-table-chair</v-icon>
            <v-list-item-title>Closetime</v-list-item-title>
            <v-list-item-title>
              <!-- dialog 시작 -->
              <v-dialog
                ref="dialog2"
                v-model="modal2"
                :return-value.sync="time"
                persistent
                color='light-green lighten-4'
                width="290px"
                required
              >
                <template v-slot:activator="{ on }">
                  <v-text-field
                    v-model="Place.closetime"
                    readonly
                    v-on="on"
                    :rules="[() => !!Place.opentime || '마감시간을 입력해주세요']"
                    :aria-required="true"
                  ></v-text-field>
                </template>
                <v-time-picker
                  v-if="modal2"
                  v-model="Place.closetime"
                  full-width
                  color='light-green lighten-1'
                  header-color='light-green lighten-2'
                >
                  <v-spacer></v-spacer>
                  <v-btn text color="light-green darken-3" @click="modal2 = false">Cancel</v-btn>
                  <v-btn text color="light-green darken-3" @click="$refs.dialog2.save(Place.closetime)">OK</v-btn>
                </v-time-picker>
              </v-dialog>

            </v-list-item-title>
          </v-list-item>
        </v-list-item>

        <v-divider class='mx-2'></v-divider>

        <v-list-item>
          <v-list-item>
            <v-icon color="light-green darken-2">mdi-phone-classic</v-icon>
            <v-list-item-title>전화번호</v-list-item-title>
            <v-list-item-title>
              <v-text-field
                color='light-green lighten-4'
                v-model="Place.phonenumber"
                :rules="[() => !!Place.phonenumber || '전화번호를 입력해주세요']"
                placeholder="062-123-1234"
                required
              ></v-text-field>
            </v-list-item-title>
          </v-list-item>
        </v-list-item>

        <v-divider class='mx-2'></v-divider>
    
        <v-list-item>
          <v-list-item>
            <v-icon color="light-green darken-2">mdi-image-filter</v-icon>
            <v-list-item-title>사진등록</v-list-item-title>
            <v-list-item-title>
            <!-- 사진등록 leek 시작 -->
              <div class="col-md-12 px-0">
                <div id="demo" class="carousel slide" data-ride="carousel">
                  <div class= "justify-content-center text-center">
                    <button type="button" class="btn btn-sm btn-outline-secondary " data-toggle="modal" data-target="#ImageModal">
                      <v-icon>mdi-file-image</v-icon>
                      UPLOAD
                    </button>
                    <div class="modal" id="ImageModal">
                      <div class="modal-dialog">
                        <div class="modal-content">                                    
                          <!-- Modal Header -->
                          <div class="modal-header justify-content-between">
                            <div class="input-group mb-3 px-2 rounded-pill bg-white shadow-sm" style="margin:0 auto;">
                              <input id="upload" type="file" ref="file" @change="handleFileUpload" style="display:none;">
                              <label for="upload" class="btn btn-light m-0 rounded-pill text-center"> 
                                <small class="">
                                  <v-icon>mdi-folder-open-outline</v-icon>
                                    파일 찾기
                                </small>
                              </label>
                            </div>
                            <button type="button" class="close" data-dismiss="modal">&times;</button>
                          </div>
                          
                          <!-- Modal body -->
                          <div class="modal-body">                                            
                            <!-- 등록된 사진이 있는지 확인하고 -->
                            <p class='block'>여러장 등록 가능합니다.</p>
                            <div id = "PlaceImages" class="row text-center text-lg-left">                                                   
                              <div v-for="(img, index) in Place.placepicture" :key="index"  class="col-lg-3 col-md-4 col-6">
                                <div class="image-container" color='black'>
                                  <img class="image img-fluid img-thumbnail" :id ="index" :src="img.data" alt=""/>
                                  <div class="hidden">
                                    <button type = 'button' class="m-2" @click="deleteImage(index)">
                                      <v-icon class="headline">mdi-delete-forever</v-icon>
                                      삭제
                                      </button>
                                  </div>
                                </div>
                              </div>
                            </div>
                            <button type="submit" class="btn btn-sm btn-outline-secondary mr-3" data-dismiss="modal">확인</button>
                            <button type="button" class="btn btn-sm btn-outline-secondary mr-3" @click="ResetImage" data-dismiss="modal">취소</button>                                            
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>                        
                </div>                          
              </div>
              <!-- 사진등록 leek 끝 -->
            </v-list-item-title>
          </v-list-item>
        </v-list-item>

   
        

  
        <v-divider class='mx-2'></v-divider>
          <h5 class='d-flex justify-start px-4 pt-4'>Detail Information</h5>
          <p class="d-flex justify-start px-8 font-weight-light caption grey--text lighten-4--text">
          <v-icon class="font-weight-light body-2 amber--text lighten-2--text mr-2">mdi-book-open-page-variant</v-icon>
            세부사항 등록 정보 입니다.
        </p>
        <v-divider class='mx-2'></v-divider>


        <v-list-item>
          <v-list-item>
            <v-icon color="light-green darken-2">mdi-parking</v-icon>
            <v-list-item-title>주차장</v-list-item-title>
            <v-list-item-title>
              <v-radio-group v-model="Place.parkinglot" row fluid color="light-green darken-2">
                <v-radio name='parkinglot' color="grey darken-1" label="있음" value="O" required></v-radio>
                <v-radio name='parkinglot' color="grey darken-1" label="없음" value="X" required></v-radio>
              </v-radio-group> 
            </v-list-item-title>
          </v-list-item>
        </v-list-item>
        <v-divider class='mx-2'></v-divider>
        <v-list-item>
          <v-list-item>
            <v-icon color="light-green darken-2">mdi-coin-outline</v-icon>
            <v-list-item-title>가격</v-list-item-title>
            <v-list-item-title>
                <v-text-field
                  color='light-green lighten-4'
                  v-model="Place.studycafe.price"
                  type="text"
                  placeholder="하루 7000원"
                ></v-text-field>
                </v-list-item-title>
          </v-list-item>
        </v-list-item>
        <v-divider class='mx-2'></v-divider>
        <v-list-item>
          <v-list-item>
            <v-icon color="light-green darken-2">mdi-comment-outline</v-icon>
            <v-list-item-title>설명</v-list-item-title>
            <v-list-item-title>
                <v-text-field
                  color='light-green lighten-4'
                  v-model="Place.studycafe.explanation"
                  type="text"
                  placeholder="설명"
                ></v-text-field>
            </v-list-item-title>
          </v-list-item>
        </v-list-item>

        <v-divider class='mx-2'></v-divider>

        <v-list-item>
          <v-list-item>
            <v-icon color="light-green darken-2">mdi-table-chair</v-icon>
            <v-list-item-title>테이블 개수</v-list-item-title>
            <v-list-item-title>
              <v-list-item-title>
                
            </v-list-item-title>
            </v-list-item-title>
          </v-list-item>
        </v-list-item>
        <v-list-item>
          <v-list-item>
            <v-icon color="transparent">mdi-table-chair</v-icon>
            <v-list-item-title>1인</v-list-item-title>
            <v-list-item-title><v-text-field
                  color='light-green lighten-4'
                  v-model="Place.tableinfo1"
                  type="number"
                  placeholder="10"
                  :rules="[() => !!Place.placename || '테이블 개수를 입력해주세요']"
                  required
                ></v-text-field></v-list-item-title>
          </v-list-item>
        </v-list-item>
        <v-list-item>
          <v-list-item>
            <v-icon color="transparent">mdi-table-chair</v-icon>
            <v-list-item-title>2인</v-list-item-title>
            <v-list-item-title>
              <v-text-field
                  color='light-green lighten-4'
                  v-model="Place.tableinfo2"
                  type="number"
                  placeholder="10"
                  :rules="[() => !!Place.placename || '테이블 개수를 입력해주세요']"
                  required
                ></v-text-field>
            </v-list-item-title>
          </v-list-item>
        </v-list-item>
        <v-list-item>
          <v-list-item>
            <v-icon color="transparent">mdi-table-chair</v-icon>
            <v-list-item-title>4인</v-list-item-title>
            <v-list-item-title>
              <v-text-field
                  color='light-green lighten-4'
                  v-model="Place.tableinfo4"
                  type="number"
                  placeholder="10"
                  :rules="[() => !!Place.placename || '테이블 개수를 입력해주세요']"
                  required
                ></v-text-field>
            </v-list-item-title>
          </v-list-item>
        </v-list-item>
        <v-list-item>
          <v-list-item>
            <v-icon color="transparent">mdi-table-chair</v-icon>
            <v-list-item-title>5인 이상</v-list-item-title>
            <v-list-item-title>
              <v-text-field
                  color='light-green lighten-4'
                  v-model="Place.tableinfo5"
                  type="number"
                  placeholder="10"
                  :rules="[() => !!Place.placename || '테이블 개수를 입력해주세요']"
                  required
                ></v-text-field>
            </v-list-item-title>
          </v-list-item>
        </v-list-item>



      </v-list>


      </v-card>
      </v-row>
      <div class='text-center'>
        <v-btn 
          class="m-4" 
          large
          tile
          outlined=""
          color="grey darken-1"
          type="reset">
          <v-icon left>mdi-close-circle-outline</v-icon>
          취소
        </v-btn>
        <v-btn 
          class="m-4 white--text" 
          large
          tile 
          color="light-green darken-3"
          type="submit">
          <v-icon left>mdi-pencil-circle-outline</v-icon>
          등록
        </v-btn>
      </div>
      
    </form>
    </v-container>
  </v-app>
  </body>

 
</template>


<script>
import axios from 'axios'
import axios_common from "../axios_common";
import router from '../router'
export default {
    
    data() {            
		return {
        search_keyword:'',
        search_result_data:[],
        files:[],       
        time: null,
        menu2: false,
        modal1: false,
        modal2: false,     
        coffeImg1: 'https://image.freepik.com/free-photo/_23-2148336762.jpg',
        coffeImg2: 'https://image.freepik.com/free-photo/_23-2148336734.jpg' ,          
        coffeImg3: 'https://image.freepik.com/free-photo/_23-2148336757.jpg',
        coffeImg4: 'https://image.freepik.com/free-photo/_1253-1584.jpg',
        Place:{
            placeid:"",
            placename:"",
            latitude: '',
            longitude: '',  
            location:"",
            phonenumber:"",
            parkinglot:"",
            tableinfo1:'',
            tableinfo2:'',
            tableinfo4:'',
            tableinfo5:'',
            opentime:'',
            closetime:'',
            placepicture:[],
            studycafe:{
                price:'',
				explanation:''               
            },
        },
			
		};
    },

    methods:{                  
        preprocess(){
            if( this.Place.parkinglot =="X")
                this.Place.parkinglot="False";
            else
                this.Place.parkinglot="True";
        },
        registdetail(){
            this.preprocess();    
            console.log(this.Place)        
            axios_common            
            .post('/registdetail/2/',this.Place                        
            ).then(response=>{
                if(response.valid=='True')
                    window.console.log('Success!!');
                else
                    window.console.log(response.valid);
                router.push('/map')
            })
            .catch(response=>{
                window.console.log(response.valid);
            });
        },       
        ResetImage()
        {
            this.Place.placepicture = [];            
        },
        handleFileUpload(){           
            var file = this.$refs.file.files[0];            
            // window.console.log("file:");
            // window.console.log(file);            
            var reader = new FileReader();
            var vm = this;
            reader.onload = (e) => {
                window.console.log(e.target);
                vm.Place.placepicture.push({"picture":file['name'],"data":e.target.result});
                //window.console.log(vm.Place.placepicture[0]);
                // window.console.log("onload :");
                // window.console.log(e.target.result);
            };            
            reader.readAsDataURL(file);            
        },
        deleteImage(index){
            //this.Place.uploadImg.splice(index, 1);
            //  window.console.log(event.target);
             window.console.log(this.Place.placepicture);
             this.$delete(this.Place.placepicture,index);             
            // this.Place.uploadImg.pop(event.target);
             window.console.log("after");
             window.console.log(this.Place.placepicture);
            // window.console.log(this.Place.uploadImg);
             var uploadInputElement = document.getElementById("upload");
             uploadInputElement.value="";
        },
        // 장소 검색
        place_search() {
            axios.get('https://dapi.kakao.com/v2/local/search/keyword.json',
              {
                params: { query: this.search_keyword },
                headers: { "Authorization": "KakaoAK dcec71e023f9c1ef32498ea45540e114" }
              }).then((res) => {
                this.search_result_data = res.data.documents
              }).catch((e)=>{
                console.log(e)
              })
        },
        place_choice(place) {
          console.log(place)
            this.Place.placeid = place.id
            this.Place.placename = place.place_name
            this.Place.location = place.address_name
            this.Place.phonenumber = place.phone
            this.Place.longitude = place.x
            this.Place.latitude = place.y
        }        
    }
}

</script>

<style scoped>
  body {
    background-color:brown;
    border: 0;
    padding: 0; 
    /* background-image: url('image.jpg'); */
    min-height: 100%;
    background-position: center;
    background-size: cover;
  }
</style>
