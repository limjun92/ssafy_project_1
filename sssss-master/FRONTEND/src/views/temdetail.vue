<template>
    <v-app>
        <!-- ****** Breadcumb Area Start ****** -->
        <div class="breadcumb-area" style="background-image: url(../img/bg-img/bg-coffee9.jpg);">
            <div class="container h-100">
                <div class="row h-100 align-items-center">
                    <div class="col-12">
                        <div class="logo_area text-center">
                            <h2 style="color:white;  text-shadow: 2px 2px 2px gray;">{{placeInfo.placename}}</h2>

                            <h5 style="color:white;">| {{this.placeCategory}} |</h5>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- ****** Breadcumb Area End ****** -->


        <div class="breadcumb-nav">
        <div class="container">
            <div class="row">
                <div class="col-12">
                    <nav aria-label="breadcrumb">
                        <ol class="breadcrumb">
                            <li class="breadcrumb-item"><router-link :to="'map/'"><i class="fa fa-home" aria-hidden="true"></i> Map</router-link></li>
                            <li class="breadcrumb-item"><a href="#">{{placeCategory}}</a></li>
                            <li class="breadcrumb-item active" aria-current="page"><a style="color:gray;">{{placeInfo.placename}}</a></li>
                        </ol>
                    </nav>
                </div>
            </div>
        </div>
    </div>

        <!-- ****** Single Blog Area Start ****** -->
        <section class="single_blog_area " >
            <div class="container">
                <div class="row justify-content-center">
                  
                    <div class="col-12 col-lg-8">
                        <div class="row">
                            <!-- ****** Instagram Area Start ****** -->
                            <div class="col-12 col-sm-11">
                                <div class="single-post">
                                  
                                    <!-- 사진 시작 -->
                                    <!-- [ADD BY LEEK] Error in vuetify image not working on responsive -->
                                    <!-- <div class="col-md-12 px-0"> -->
                    
                                    <!-- <div class="jumbotron p-md-5 col-md-12 px-0 rounded"  style="background-color:white;">
                                        <div id="demo" class="carousel slide" data-ride="carousel">                                            
                                            <ul class="carousel-indicators" v-for="(item,i) in placeInfo.placepicture" :key="i">
                                                <li data-target="#demo" :data-slide-to="i" class="active"></li>                                                    
                                            </ul>
                                            <div>                                            
                                                <div class="carousel-inner" v-for="(item,i) in placeInfo.placepicture" :key="i">
                                                    <div class="carousel-item active">
                                                        <img class ="img-fluid" :src="item">
                                                    </div>
                                                </div>
                                            </div>                                            
                                            <a class="carousel-control-prev" href="#demo" data-slide="prev">
                                                    <span class="carousel-control-prev-icon"></span>
                                            </a>
                                            <a class="carousel-control-next" href="#demo" data-slide="next">
                                                    <span class="carousel-control-next-icon"></span>
                                            </a>
                                        </div> -->
                                    
                                    
                                        <v-card
                                        flat                                 
                                        >
                                        <v-carousel 
                                        :show-arrows="false"
                                        :continuous="true"                                        
                                        height="300px"
                                        hide-delimiter-background
                                        delimiter-icon="mdi-minus"
                                        style="position: relative; height;300px;"
                                        >
                                      
                                        <v-carousel-item
                                            v-for="(item,i) in placeInfo.placepicture"
                                            :key="i"
                                            class="../../public/imgbox fluid"
                                            style="object-fit:cover; text-align:center;"
                                            
                                        >
                                            <img :src="item" style="height:300px !important; width: auto; resize: both; float: center; object-fit:cover;"/>
                                        </v-carousel-item>                                    
                                        </v-carousel>                                        
                                        </v-card>
                                    

                                    <!-- Post Content -->
                                    <div class="post-content ml-2">
                                        <div class="post-meta d-flex mt-3 mx-3">
                                            <div class="post-author-date-area d-flex">
                                                <!-- Post Author -->
                                                
                                                <div class="post-author">
                                                    <a href="#">{{placeInfo.placename}}</a>
                                                </div>
                                                <!-- Post Date -->
                                                <div class="post-date">
                                                    <a href="#">Fab 18, 2020</a>
                                                </div>
                                            </div>
                                            
                                            <!-- Post Comment & Share Area -->
                                            <div class="post-comment-share-area d-flex mt-2">
                                                <!-- Post Favourite -->
                                                <div @click="like" class="post-favourite">
                                                    <v-btn icon color="#C62828" style="outline:0">
                                                      <v-icon 
                                                        v-if="onLike"
                                                      >
                                                        mdi-heart
                                                      </v-icon>
                                                      <v-icon 
                                                      v-if="!onLike"
                                                      >
                                                      mdi-heart-outline
                                                      </v-icon>

                                                    </v-btn>
                                                </div>

                                                <div>
                                                  <h1 @click="like">
                                                    
                                                  </h1>
                                                  <p>{{countLike}}</p>

                                              </div>
                                            </div>
                                        </div>                                        

                                        <!-- <a href="#">
                                            <h2 class="post-headline" style="text-align: left;">Information</h2>
                                        </a>							 -->
                                        <div class="widget-title" style="text-align:center; color:#f2987c !important;">
                                          <h6>Information</h6>
                                      </div>

										<!-- {{placeInfo}} -->
                                        <!-- <p>카테고리 : {{placeCategory}}</p> -->
                                        <div class="ml-3">
                                            <p v-if="placeInfo.location"> 
                                                <v-icon class="mr-1" style="font-size:20px" color="deep-orange lighten-2">mdi-map-marker-radius-outline</v-icon>
                                                {{placeInfo.location}}
                                            </p>
                                            <p v-if="placeInfo.phonenumber">
                                                <v-icon class="mr-1" style="font-size:20px" color="deep-orange lighten-2">mdi-phone-classic</v-icon>
                                                {{placeInfo.phonenumber}}</p>
                                            
                                            <p v-if="placeInfo.phonenumber">
                                                <v-icon class="mr-1" style="font-size:20px" color="deep-orange lighten-2">mdi-clock-check-outline</v-icon>
                                                운영시간
                                                {{placeInfo.opentime}} ~ {{placeInfo.closetime}}
                                            </p>
                                            <p v-if="placeInfo.cafe.subdetail">
                                                <v-icon class="mr-1" style="font-size:20px" color="deep-orange lighten-2">mdi-note-text-outline</v-icon>
                                                {{placeInfo.cafe.subdetail}}
                                            </p>

                                            <div class="m-6" v-if="placeInfo.cafe.menu.length > 0">
                                                <div class="widget-title mt-5">
                                                    <p> 
                                                        <v-icon class="mr-1" style="font-size:20px" color="deep-orange lighten-2">mdi-book-open-page-variant</v-icon>
                                                        메뉴
                                                        <v-btn x-small :elevation='0' class="ml-3" @click.native="show = !show">{{ show ? '메뉴 가리기' : '메뉴 보기' }}</v-btn>
                                                    </p>
                                                </div>
                                                <div  v-show="show" class="ml-6" v-for="menu in placeInfo.cafe.menu" :key=menu.id>
                                                    <p style="font-size:13px; margin-bottom:3px" ><span class="mdi mdi-coffee mr-1" style="color:#F4511E;"></span>{{menu['name']}} : {{menu['price']}} 원</p> 
                                                </div>

                                              
                                            </div>  
                                        
                                        </div>

                                        <!-- 여러분 placeategroy로 if문 바꿔주세요 -->
                                        <!-- db들어가면 placecategory가 없어서 분기처리를 할 수 없습니다. -->
                                        <!-- cafe library studycafe안에 값이 있는지로 확인해서 넣어주세요 -->
										<div v-if="flag==1 & !placeInfo.tableinfo1==''">
											<div class="container panel">
												
                                                <div class="" v-if="placeCategory=='스터디카페'">
                                                    <div class="col-sm-4 col-6" style="text-align: center;">
                                                        <img class="test" src="../../public/img/money.svg" @click="makeEffect($event)">
                                                        <div class="sub mt-3">
                                                            가격: {{placeInfo.studycafe.price}}
                                                        </div>
                                                    </div>
                                                    <div class="col-sm-4 col-6" style="text-align: center;">
                                                        <img class="test" src="../../public/img/desk.svg" @click="makeEffect($event)">
                                                        <div class="sub mt-3">
                                                            1인: {{placeInfo.tableinfo1}}/2인: {{placeInfo.tableinfo2}}/4인: {{placeInfo.tableinfo4}}/5인이상: {{placeInfo.tableinfo5}}
                                                        </div>
                                                    </div>
                                                    <div class="col-sm-4 col-6" style="text-align: center;">
                                                        <img class="test" src="../../public/img/park.svg" @click="makeEffect($event)">
                                                        <div class="sub mt-3">
                                                            주차:
                                                            <span v-if="placeInfo.parkinglot == true">
                                                                O
                                                            </span>
                                                            <span v-else>
                                                                X
                                                            </span>
                                                        </div>
                                                    </div>
                                                </div>
<!-- 카페 카페 카페 카페 카페 카페 카페 카페 카페 카페 카페 카페 카페 카페 카페 카페 카페 카페 카페 카페 카페 카페 카페 카페 카페 카페 -->
                                                <div class="row" v-if="placeCategory=='카페'">
                                                    <div class="col-sm-4 col-6" style="text-align: center;">
                                                        <img class="test" src="../../public/img/socket.svg" @click="makeEffect($event)">
                                                        <div class="sub mt-3">
                                                            콘센트 수 {{placeInfo.cafe.powersoket}}
                                                        </div>
                                                    </div>
                                                    <div class="col-sm-4 col-6" style="text-align: center;">
                                                        <img class="test" src="../../public/img/desk.svg" @click="makeEffect($event)">
                                                        <div class="sub mt-3">
                                                            <p>1인 좌석: {{placeInfo.tableinfo1}}개</p>
                                                            <p>2인 좌석: {{placeInfo.tableinfo2}}개</p>
                                                            <p>4인 좌석: {{placeInfo.tableinfo4}}개</p>
                                                            <p>5인이상 좌석: {{placeInfo.tableinfo5}}개</p>
                                                        </div>
                                                    </div>
                                                    
                                                    <div class="col-sm-4 col-6" style="text-align: center;">
                                                        <img class="test" src="../../public/img/beer.svg" @click="makeEffect($event)">
                                                        <div class="sub mt-3">
                                                            주류 판매:
                                                            <span v-if="placeInfo.cafe.alcoholonoff == true">
                                                                O
                                                            </span>
                                                            <span v-else>
                                                                X
                                                            </span>
                                                        </div>
                                                    </div>
                                                    <div class="col-sm-4 col-6" style="text-align: center;">
                                                        <img class="test" src="../../public/img/cigarette.svg" @click="makeEffect($event)">
                                                        <div class="sub mt-3">
                                                            흡연실:
                                                            <span v-if="placeInfo.cafe.smokingroom == true">
                                                                O
                                                            </span>
                                                            <span v-else>
                                                                X
                                                            </span>
                                                        </div>
                                                    </div>
                                                    <div class="col-sm-4 col-6" style="text-align: center;">
                                                        <img class="test" src="../../public/img/sandwich.svg" @click="makeEffect($event)">
                                                        <div class="sub mt-3">
                                                            디저트:
                                                            <span v-if="placeInfo.cafe.dessertonoff == true">
                                                                O
                                                            </span>
                                                            <span v-else>
                                                                X
                                                            </span>
                                                        </div>
                                                    </div>
                                                    
                                                    
                                                    <div class="col-sm-4 col-6" style="text-align: center;">
                                                        <img class="test" src="../../public/img/park.svg" @click="makeEffect($event)">
                                                        <div class="sub mt-3">
                                                            주차:
                                                            <span v-if="placeInfo.cafe.parkinglot == true">
                                                                O
                                                            </span>
                                                            <span v-else>
                                                                X
                                                            </span>
                                                        </div>
                                                    </div>
                                                    <div class="col-sm-4 col-6" style="text-align: center;">
                                                    
                                                        <img class="test" src="../../public/img/area.svg" @click="makeEffect($event)">


                                                        <div class="sub mt-3">
                                                            매장 면적: {{placeInfo.cafe.storearea}}
                                                        </div>
                                                    </div>
                                                </div>


                                                <div class="row" v-if="placeCategory=='도서관'">
                                                   
                                                    <div class="col-sm-4 col-6" style="text-align: center;">
                                                        <img class="test" src="../../public/img/store.svg" @click="makeEffect($event)">
                                                        <div class="sub mt-3">
                                                            매점 유무: 
                                                            <span v-if="placeInfo.library.convenience == 'True'">
                                                                O
                                                            </span>
                                                            <span v-else>
                                                                X
                                                            </span>
                                                        </div>
                                                    </div>
                                                    <div class="col-sm-4 col-6" style="text-align: center;">
                                                        <img class="test" src="../../public/img/laptop.svg" @click="makeEffect($event)">
                                                        <div class="sub mt-3">
                                                            노트북열람실 유무: 
                                                            <span v-if="placeInfo.library.notebook == 'True'">
                                                                O
                                                            </span>
                                                            <span v-else>
                                                                X
                                                            </span>
                                                        </div>
                                                    </div>
                                                    <div class="col-sm-4 col-6" style="text-align: center;">
                                                        <img class="test" src="../../public/img/desk.svg" @click="makeEffect($event)">
                                                        <div class="sub mt-3">
                                                            1인: {{placeInfo.tableinfo1}}/2인: {{placeInfo.tableinfo2}}/4인: {{placeInfo.tableinfo4}}/5인이상: {{placeInfo.tableinfo5}}
                                                        </div>
                                                    </div>
                                                    <!-- <div class="col-sm-4 col-6" style="text-align: center;">
                                                        <img class="test" src="../../public/img/socket.svg" @click="makeEffect($event)">
                                                        <div class="sub mt-3">
                                                            좌석당 콘센트 수 {{socketperdesk}}
                                                        </div>
                                                    </div> -->
                                                    <div class="col-sm-4 col-6" style="text-align: center;">
                                                        <img class="test" src="../../public/img/park.svg" @click="makeEffect($event)">
                                                        <div class="sub mt-3">
                                                            주차: {{placeInfo.parkinglot}}
                                                            <span v-if="placeInfo.parkinglot == 'True'">
                                                                O
                                                            </span>
                                                            <span v-else>
                                                                X
                                                            </span>
                                                        </div>
                                                    </div>
                                                </div>												
                                            </div>

                                        </div>                                     
                                    </div>
                                </div>
                              </div>
                            </div>
                          </div>                        

                                <!-- ****** Blog Sidebar ****** -->
                          <div class="col-12 col-sm-8 col-md-6 col-lg-4">
                              <div class="blog-sidebar mt-5 mt-lg-0">

                             <!-- Single Widget Area -->
                                  <div class="widget-title" style="text-align:center;">
                                          <h6>사용자 평가</h6>
                                      </div>
										<!-- <v-card class="mx-auto" max-width="500"> -->
										<v-card class="mx-auto col-sm-12 d-flex flex-column justify-content-center">						
                                            <div v-show="this.placeInfo.review.length==0">					
                                                <h5>등록된 리뷰 정보가 없습니다.</h5>
                                            </div>
                                            <div v-show="this.placeInfo.review.length!=0" style="min-length:500px; margin:0 auto; left:50%;">	    
                                                <div style="text-align:center;">
                                                    <canvas id="myChart" class="col-sm-12" style="height:200px"></canvas>
                                                </div>
                                            </div>
												<!-- <div class="my-3"></div> -->

												<v-card-text class="text--primary">
													<div v-if="isAuthenticated">
														<form  method="post"  @submit.prevent="registreview" action="/action_page.php" >
															<div class="form-group">
																<v-slider v-model="review.noise" label="Noise" hint="" min="0" max="3" thumb-label color="#8eb2e8" track-color="#e8b58e"></v-slider>
																<v-slider v-model="review.light" label="Light" hint="" min="0" max="3" thumb-label color="#8eb2e8" track-color="#e8b58e"></v-slider>
																<v-slider v-model="review.seat" label="Seat" hint="" min="0" max="3" thumb-label color="#8eb2e8" track-color="#e8b58e"></v-slider>
															</div>
                                                            <div style="text-align:center;">
															<button type="submit" class="btn" id="EC407A">평가하기</button>
                                                            </div>
														</form>
													</div>
													<div v-else>
															로그인 후 리뷰 등록할 수 있습니다.
													</div>
												</v-card-text>					
										</v-card>

                                  <!-- Single Widget Area -->
                                  <div class="single-widget-area subscribe_widget text-center mt-5">
                                      <div class="widget-title">
                                          <h6>키워드 분석</h6>
                                      </div>
                                      <div class="row justify-content-center">
                                          <div class="hastag-css" v-for="(ele,i) in keyword" :key="i">
                                              <i class="fas fa-hashtag ml-2" style="font-size:90%; margin-left:2px;"></i>&nbsp;&nbsp;<span class="mr-2" style="font-size:90%;">{{ele}}</span>
                                          </div>                                        
                                      </div>
                                  </div>
       
                                  </div>
                              </div>
                          </div>
                </div>
            
        </section>
        
      <section class="single_blog_area">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="row justify-content-center">                    
                      <div class="col-12 col-lg-8">
                        <div class="row">
                            <!-- ****** Instagram Area Start ****** -->
                            <div class="col-12 col-sm-11">
                                <!-- Leave A Comment -->          
                                                      
                                <div class="single-widget-area subscribe_widget text-center mt-5 mx-3">
                                    <div class="comment-form widget-title" style="text-align:center;">
                                        <h6>댓글</h6>

                                        <!-- Comment Form -->
                                        <form class="mt-5" @submit.prevent="registcomment">                                            
                                            <div class="form-group ml-2 mr-2">
                                                <textarea @click="preventComment" class="form-control" cols="30" rows="5" v-model="comments.comment" placeholder="댓글을 입력해주세요."></textarea>
                                            </div>
                                            <div class="d-flex justify-content-end pr-3">
                                                <button type="submit" class="btn contact-btn mt-5" style="background-color:#f79b54">
                                                    <h6 style="color:white">등록</h6>
                                                </button>

                                            </div>
                                        </form>
                                    </div>
                                </div>
                                <!-- Comment Area Start -->
                                <div class="comment_area section_padding_50 clearfix">
                                    <!-- <h2 class="post-headline pl-3" style="text-align: left;">Comments</h2> -->
                                    <ol>
                                        <!-- Single Comment Area -->
                                        <li class="single_comment_area" v-for="(comment) in placeInfo.commentss" :key="comment.id">
                                            <div class="comment-wrapper d-flex">
                                                <div class="comment-author">
                                                                                    
                                                    <img src="../../public/img/basicinfo/anyone0.png">
                                                    <!-- <img :src="`comment_img[0]`"> -->

                                                </div>                                               
                                                <div class="comment-content">
                                                    <span class="comment-date text-muted">{{comment.create_at}}</span>
                                                    <h5>{{comment.review_user['username']}}</h5>
                                                    <p>{{comment.comment}}</p>
                                                    <!-- <a href="#">Like</a> -->
                                                </div>
                                            </div>                                            
                                        </li>                                        
                                    </ol>
                                </div>


                            </div>
                        </div>
                    </div>

                    <div class="col-12 col-sm-8 col-md-6 col-lg-4">
                              <div class="blog-sidebar mt-5 mt-lg-0">
                                  <!-- Single Widget Area -->
                                  <div class="single-widget-area about-me-widget text-center">
                                  </div>
                              </div>
                          </div>
                  </div>  
                </div>
            </div>
        </section>
        <!-- ****** Single Blog Area End ****** -->
        
        <!-- ****** Footer Menu Area Start ****** -->
        <footer class="footer_area">
            <div class="container">
                <div class="row">
                    <div class="col-12">
                        <!-- Copywrite Text -->
                        <div class="copy_right_text text-center">
                            <p>Copyright @2020 All rights reserved | This website is made with <i class="fa fa-heart-o" aria-hidden="true"></i> by <a href="#" target="_blank">Nuneddine</a></p>
                        </div>
                    </div>
                </div>
            </div>
        </footer>

        <div class="text-center">
            <v-bottom-sheet v-model="bottomSheet" inset>
            
            <v-sheet class="text-center" height="150px">
                <v-btn
                class="mt-3"
                text
                color="error"
                @click="bottomSheet = !bottomSheet"
                >close</v-btn>
                <div class="my-3">
                    <p>🌻 리뷰를 남겨주세요 🌻 </p>
                    <p>리뷰를 남겨주시면 100point를 드립니다. </p>
                    <p> </p>
                </div>
            </v-sheet>
            </v-bottom-sheet>
        </div>
    </v-app>    
		
</template>
<script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>
<script>
import axios_common from '../axios_common';
import Chart from 'chart.js';
import swal from 'sweetalert';
/* eslint-disable */
export default {
    props:['id','place_lat','place_lng','place_name','address_name','category_group_name'],    
    components: {
    
    },
    data: function() 
    {
        return {
                    show: false,
                    bottomSheet: false,
					userId:'',
					flag:'',
					// 장소 고유의 id
					//placeId: this.$router.app._route.params.id, 
					placeId: '',
					placeInfo: {       
							latitude: '',
							longitude: '',         
							review: [],
							cafe:{
									storearea:"",
									alcoholonoff: "X",
									dessertonoff: "X",
									smokingroom: "X",
									powersoket: "X",
									menu: [],
									subdetail: ""
							},
							placename:'',
							library:{
								convenience: false,
								notebook: false
							},
							studycafe: {
								price:'',
								explanation:''
							},
							location: "",
							phonenumber: "",
							placepicture: [],
							parkinglot: '',
							tableinfo1: '',
							tableinfo2: '',
							tableinfo4: '',
							tableinfo5: '',
							opentime: '',
							closetime: '',
							like_users: [],
							commentss: [] 
					},            
					placeCategory: '', // cafe인지 도서관인지 스터디카페인지 
					comments:{
							review_user: {
											username: this.$store.getters.userId
									},
							placeid: '',
							comment: '',
							placeinfo: [],
							category: '',
					},
					review: {
							review_user: {
									username: this.$store.getters.userId
							},
							placeid: '',
							noise: '',
							light: '',
							seat: '',
							placeinfo: [],
							category: '',
					},
					onLike:'',
					countLike:'',
					//commentss: [],            
					// reviewscore: [],
					likes: {
							placeid: '',
							placeinfo: [],
							category: '',
                    },                    
					socketperdesk:'',
                    reviewlen:'',
                    comment_img: [
                        "../../public/img/basicinfo/anyone0.png",  
                        "../../public/img/basicinfo/anyone1.png"
                    ],
                    keyword : []

                    
                }
                    
                    
	}, 
    computed: {
        getplaceid(){
            return this.$router.props['id'];
        },
        requestHeader() {
                return this.$store.getters.requestHeader;
            },
				userName() {
						return this.$store.getters.loggedInUser.username;
				},
				isAuthenticated() {
            return this.$store.getters.isAuthenticated;
				},
    },
    methods: {
        makeEffect(e){
            var target = e.target;
            target.classList.add('animation')
            var subdivs = document.getElementsByClassName('sub')
            for(var i = 0 ; i < subdivs.length; i++)
            {
                if(subdivs[i].style.display=="block")
                    subdivs[i].style.display="none"
            }
            var sub = target.nextSibling
            sub.style.display="block"
            setTimeout(function(){
                target.classList.remove('animation')
            },1000)
        },
        like(){
				this.likes.placename = this.placeInfo.placename
				this.likes.placeid = this.id
				this.likes.placeinfo = this.placeInfo
				this.likes.category = this.placeCategory
					const token = this.$store.getters.requestHeader.headers.Authorization 
					if (token != 'JWT null'){ 
							this.userId=this.$store.getters.loggedInUser.user_id
							axios_common.post('/like/', this.likes, this.requestHeader)
							.then( res => {
									this.onLike = res.data.on_like
									this.countLike = res.data.count_like
							})
					} else {
                            swal({text:"로그인 후 이용해주세요",
                                icon: "warning",
                                dangerMode: true,
                            });
					}                
		},
        registcomment() {
            if(!this.preventComment())
                return
            this.comments.placeid = this.id
            this.comments.placeinfo = this.placeInfo
            this.comments.category = this.placeCategory
            axios_common
            .post(`/comment/`, this.comments, this.requestHeader)
            .then(response=>{
                const data = response.data;
                this.placeInfo.commentss.unshift(data);
                this.comments.comment = ""
            })
            .catch(response=>{
                window.console.log(response.valid);
            });
        },
        deletecomment(comment) {
            axios_common
            .delete(`/place/${this.placeId}/comment/${comment.id}/`, this.requestHeader)
            .then(() => {
            const targetcomment = this.commentss.find(function(el) {
                return el.id == comment.id;
                        });
                        console.log(targetcomment)
            const idx = this.commentss.indexOf(targetcomment);
            if (idx > -1) {
                            this.commentss.splice(idx, 1);
                        }
            })
            .catch(error => console.log(error));
        },
        registreview() {
     
            //console.log("this.placeInfo",this.placeInfo)
            //  console.log("adsfasdf",this.userId)

            var user_review_again_check = true;
            if(this.placeInfo.review.length>0){
            for(var i = 0; i<this.placeInfo.review.length;i++){
                console.log(i,(this.placeInfo.review[i].review_user.username))
                 if(this.placeInfo.review[i].review_user!=null&&this.placeInfo.review[i].review_user.username==this.username_review){
                     user_review_again_check = false;
                 }
            }
            }
            //console.log("안녕",user_review_again_check)
            if(user_review_again_check){
                this.review.placeid = this.id
                this.review.placeinfo = this.placeInfo
                this.review.category = this.placeCategory
                axios_common            
                .post('userreview/', this.review, this.requestHeader)
                .then(response=>{
                        this.placeInfo.review = response.data.review
                        this.evaluateChart()
                })
                .catch(response=>{
                    console.log("에러 : ", response)
                });
            }
            // 
            user_review_again_check = true;
		},

        preventComment()
        {
            const token = this.$store.getters.requestHeader.headers.Authorization //token가져오기
            if (token == 'JWT null'){ // 로그인이 되어있으면
                this.comments.comment=''
                swal({text:"로그인 후 이용해주세요",
                        icon: "warning",
                        dangerMode: true,
                    });
                return false
            }
            return true
        },

        async getkeywordfromcomment(){
            var keywordList = []
            // var keywordList =["조용함", "좌석이 편안한", "맛있는"]
            await axios_common.get('/place/'+this.placeId+'/keyword/')
            .then((res)=> {
                keywordList = res.data.data
            }).catch(error => console.log(error))
            return keywordList            
        },

        evaluateChart() {
            var noi = 0
                var lig = 0
                var se = 0
				var reviewlen = this.placeInfo.review.length
                for (var j = 0; j < reviewlen; j++) {
                    noi += this.placeInfo.review[j]['noise']
                    lig += this.placeInfo.review[j]['light']
                    se += this.placeInfo.review[j]['seat']
                }

                var resultnoi = (noi/reviewlen)*(10/3) -5
                var resultlig = (lig/reviewlen)*(10/3) -5
                var resultse = (se/reviewlen)*(10/3) -5


                var ctx = document.getElementById('myChart');
                var myChart = new Chart(ctx, {
                    type: 'horizontalBar',
                    data: {
                            labels: ['소음', '빛', '편안함'],
                            datasets: [{
                                    data: [resultnoi, resultlig, resultse],
                                    backgroundColor: [
                                            'rgba(255, 99, 132, 0.2)',
                                            'rgba(54, 162, 235, 0.2)',
                                            'rgba(255, 206, 86, 0.2)',
                                    ],
                                    borderColor: [
                                            'rgba(255, 99, 132, 1)',
                                            'rgba(54, 162, 235, 1)',
                                            'rgba(255, 206, 86, 1)',
                                    ],
                                    borderWidth: 2
                            }]
                    },
                    options: {
                        responsive: false,

                        scales: {
                            yAxes: [{
                                position: 'left',
                                type: "category",
                                gridLines: { offsetGridLines: true }
                            }],
                            xAxes: [{
                                ticks: {
                                    beginAtZero: true
                                },
                                position: 'bottom',
                                // type: "linear",
                                categoryPercentage: 0.5,
                                barPercentage: 0.7,
                                ticks: {
                                    suggestedMin: -5,
                                    suggestedMax:5,
                                },
                            }],
                        }
                    },                    
                });
        },

    },
    async mounted()
    {
        this.placeId = this.id        
        var url = '/place/'+this.placeId+'/'        
        var firstTrial = true
        await axios_common.get(url)
        .then((res)=> 
        {            
            console.log(res)
            if(res.data.result=="true")
            {
                console.log("trueeeeee")
				this.flag = 1
                var resultdata = res.data.data
                console.log(resultdata)
                this.placeInfo.latitude = resultdata.latitude
                this.placeInfo.longitude = resultdata.longitude
                this.placeInfo.placename = resultdata.placename
                this.placeInfo.review = resultdata.review
                if(resultdata.cafe.length >0)
                {                    
                    this.placeInfo.cafe.storearea = resultdata.cafe[0].storearea
                    this.placeInfo.cafe.alcoholonoff = resultdata.cafe[0].alcoholonoff
                    this.placeInfo.cafe.dessertonoff = resultdata.cafe[0].dessertonoff
                    this.placeInfo.cafe.smokingroom = resultdata.cafe[0].smokingroom
                    this.placeInfo.cafe.menu = resultdata.cafe[0].menu
                     if(resultdata.cafe[0].subdetail != 'False'){
                        this.placeInfo.cafe.subdetail = resultdata.cafe[0].subdetail
                    }

                    this.placeInfo.cafe.powersoket = resultdata.cafe[0].powersoket

                    this.placeCategory = '카페'
				}
                if (resultdata.library.length > 0){
                    this.placeInfo.library.convenience = resultdata.library[0].convenience
                    this.placeInfo.library.notebook = resultdata.library[0].notebook
                    this.placeCategory = '도서관'
                }
                if (resultdata.studycafe.length > 0){
                    this.placeInfo.studycafe.price = resultdata.studycafe[0].price
                    this.placeInfo.studycafe.explanation = resultdata.studycafe[0].explanation
                    this.placeCategory = '스터디카페'
                }
                this.placeInfo.location = resultdata.location
                this.placeInfo.phonenumber = resultdata.phonenumber
                console.log(this.placeCategory)
                
                
                var serverdomain = "http://localhost:8000"
                //var serverdomain = "https://i02c102.p.ssafy.io:8000"
                for(var i = 0 ; i < resultdata.placepicture.length; i++)
                    this.placeInfo.placepicture.push(serverdomain + resultdata.placepicture[i].name)
                this.placeInfo.parkinglot = resultdata.parkinglot
                this.placeInfo.tableinfo1 = resultdata.tableinfo1
                this.placeInfo.tableinfo2 = resultdata.tableinfo2
                this.placeInfo.tableinfo4 = resultdata.tableinfo4
                this.placeInfo.tableinfo5 = resultdata.tableinfo5
                this.placeInfo.opentime = resultdata.opentime
                this.placeInfo.closetime = resultdata.closetime
                this.placeInfo.like_users = resultdata.like_users
        
                for (var i=0; i <res.data.data2.length; i++){
                    this.placeInfo.commentss.push(res.data.data2[i])
                }
               


                var noi = 0
                var lig = 0
                var se = 0
				var reviewlen = this.placeInfo.review.length
				console.log(reviewlen)
                for (var j = 0; j < reviewlen; j++) {
                    noi += this.placeInfo.review[j]['noise']
                    lig += this.placeInfo.review[j]['light']
                    se += this.placeInfo.review[j]['seat']
                }
                var resultnoi = (noi/reviewlen)*(10/3) -5
                var resultlig = (lig/reviewlen)*(10/3) -5
                var resultse = (se/reviewlen)*(10/3) -5
								
                var ctx = document.getElementById('myChart');
                var myChart = new Chart(ctx, {
                    type: 'horizontalBar',
                    data: {
                            labels: ['소음', '빛', '편안함'],
                            datasets: [{
                                    data: [resultnoi, resultlig, resultse],
                                    backgroundColor: [
                                            'rgba(255, 99, 132, 0.2)',
                                            'rgba(54, 162, 235, 0.2)',
                                            'rgba(255, 206, 86, 0.2)',
                                    ],
                                    borderColor: [
                                            'rgba(255, 99, 132, 1)',
                                            'rgba(54, 162, 235, 1)',
                                            'rgba(255, 206, 86, 1)',
                                    ],
                                    borderWidth: 2
                            }]
                    },
                    options: {
                        responsive: false,
                        title: {
                                    display: true,
                                    text: '사용자 리뷰'
                        },
                        scales: {
                            yAxes: [{
                                position: 'left',
                                type: "category",
                                gridLines: { offsetGridLines: true }
                            }],
                            xAxes: [{
                                ticks: {
                                    beginAtZero: true
                                },
                                position: 'bottom',
                                // type: "linear",
                                categoryPercentage: 0.5,
                                barPercentage: 0.7,
                                ticks: {
                                    suggestedMin: -5,
                                    suggestedMax:5,
                                },
                            }],
                        }
                    },                    
                });                
                this.countLike = Object.keys(this.placeInfo.like_users).length 
                const token = this.$store.getters.requestHeader.headers.Authorization //token가져오기

                if (token != 'JWT null'){ // 로그인이 되어있으면
                    this.userId=this.$store.getters.loggedInUser.user_id
                    for (var i=0; i<this.countLike; i++){
                        if (this.placeInfo.like_users[i].id === this.userId) {
                                this.onLike = true
                        }
                    }
                }
                if(this.placeInfo.cafe.storearea)
                {
                    if(this.placeInfo.cafe.storearea>0)
                        this.socketperdesk = this.placeInfo.powersoket / this.placeInfo.cafe.storearea            
                }
                else if(this.placeInfo.library.storearea)
                {
                    if(this.placeInfo.library.storearea>0)
                        this.socketperdesk = this.placeInfo.powersoket / this.placeInfo.library.storearea            
                }
                if(this.placeInfo.studycafe.storearea)
                {
                    if(this.placeInfo.studycafe.storearea>0)
                        this.socketperdesk = this.placeInfo.powersoket / this.placeInfo.studycafe.storearea            
                }
                if(!this.placeInfo.parkinglot)
                    this.placeInfo.parkinglot = 'X'
                else
                    this.placeInfo.parkinglot = 'O'
            }
            else{
                firstTrial = false                
            }
                
        })
        .catch(error => console.log(error))
        console.log("firstTrial"+firstTrial)
        if(!firstTrial)
        {            
            this.placeInfo.placename = this.place_name
            this.placeInfo.location = this.address_name            
            this.placeCategory = this.category_group_name
            this.placeInfo.latitude = this.place_lat
            this.placeInfo.longitude = this.place_lng
            console.log(this.category_group_name)
        }
        this.keyword = await this.getkeywordfromcomment()
       if(this.placeInfo.placepicture.length ==0)
            this.placeInfo.placepicture.push("../../img/information.png")       
        if(this.placeInfo.review.length < 10)
            this.bottomSheet = true
            
            
        
    }
}

</script>

<style>
.hastag-css{
    text-align: center;
    color: white;
    border-radius: 10px;
    opacity: 0.8;
    background-color: #FF7043;
    justify-content: center;
    margin:5px;
}
.test{
    max-width: 100px;
    max-height: 100px;
}
.panel{
    /* border-style: solid; */
  /* border-color: #92a8d1;     */
    background-color: #FCE4EC;  
    border-radius: 10px;
    opacity: 0.8;  
}
.panel1{    
    border-style: solid;
    border-color: #FCE4EC;
    /* background-color:#FCE4EC;     */
    border-radius: 10px;
    opacity: 0.8;  
}
.sub{
    display: none;       
    background-color: white;    
    border-radius: 10px;
    opacity: 8;    
    margin:0 auto;
}
.animation{
   transform: scale(1.2);
   -webkit-transition: all 1s ease;  
   -moz-transition: all 1s ease;  
   -o-transition: all 1s ease;  
   -ms-transition: all 1s ease;  
   transition: all 1s ease;  
}

#EC407A {
    background-color : #FF80AB;
    color: white;
    padding: 10px 20px;
    border-radius: 4px;
    border-color: #46b8da;
}

</style>
