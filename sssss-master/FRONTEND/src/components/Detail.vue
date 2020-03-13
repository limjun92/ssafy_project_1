<template>
    <v-app class="container">
        <head>
            <link href="https://cdn.jsdelivr.net/npm/@mdi/font@4.x/css/materialdesignicons.min.css" rel="stylesheet">
        </head>	

        <header class="blog-header py-3">
            <div class="row flex-nowrap justify-content-between align-items-center">
                <div class="col-4 pt-1">
                  
                </div>
                <div class="col-4 text-center">
                    <!-- <a class="blog-header-logo text-dark" href="#">{{placeCategory.name}}</a> -->
                   <h1 class="blog-header-logo text-dark" href="#">{{this.name}}</h1>
             
                    <hr>
                </div>
                
                <div class="col-4 d-flex justify-content-end align-items-center">
                    <a class="text-muted" href="#">
                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="mx-3"><circle cx="10.5" cy="10.5" r="7.5"></circle><line x1="21" y1="21" x2="15.8" y2="15.8"></line></svg>
                    </a>                    
                </div>
            </div>

            <div>
							<!-- <div v-if="isAuthenticated"> -->
                <h1 @click="like">
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
                </h1>
							<!-- </div> -->
							<!-- <div v-else> -->
								<!-- <p>login 후 좋아요 기능을 누를 수 있습니다.</p> -->
								<p>{{countLike}}명이 좋아요를 눌렀습니다.</p>
							<!-- </div> -->
            </div>

        </header>


        <div class="jumbotron p-md-5 rounded">
					<div class="col-md-12 px-0">
						<div id="demo" class="carousel slide" data-ride="carousel">
							<!-- Indicators -->
							<ul class="carousel-indicators">
									<li data-target="#demo" data-slide-to="0" class="active"></li>
									<li data-target="#demo" data-slide-to="1"></li>
									<li data-target="#demo" data-slide-to="2"></li>
							</ul>
							<div>
							<!-- The slideshow						 -->
									<div class="carousel-inner" if="placeInfo.placepicture">

										<div class="carousel-item active">
											<!-- <img class ="img-fluid" :src="`http://localhost:8000${placeInfo.placepicture[0]['name']}`"> -->
                                            <img class ="img-fluid" src = "../../public/img/information.png">
										</div>
                                        <div class="carousel-item">
											<!-- <img class ="img-fluid" :src="`http://localhost:8000${placeInfo.placepicture[0]['name']}`"> -->
                                            <img class ="img-fluid" src = "../../public/img/information.png">
										</div>
                                        <div class="carousel-item">
											<!-- <img class ="img-fluid" :src="`http://localhost:8000${placeInfo.placepicture[0]['name']}`"> -->
                                            <img class ="img-fluid" src = "../../public/img/information.png">
										</div>
										<!-- <div v-for="idx in placeInfo.placepicture.length" :key="idx.id">
											<div v-if="idx !=1">
												{{idx}}
												<div class="carousel-item">
													<img class ="img-fluid" :src="`http://localhost:8000${placeInfo.placepicture[idx-1]['name']}`">
												</div>
											</div>
										</div> 
										<div class="carousel-item">
											<img class ="img-fluid" :src="`http://localhost:8000${placeInfo.placepicture[2]['name']}`">
										</div> -->
									</div>								
							</div>
							<!-- Left and right controls -->
							<a class="carousel-control-prev" href="#demo" data-slide="prev">
									<span class="carousel-control-prev-icon"></span>
							</a>
							<a class="carousel-control-next" href="#demo" data-slide="next">
									<span class="carousel-control-next-icon"></span>
							</a>
						</div>
					</div>
        </div>

        <div class="row mb-2">
            <div class="col-md-6">
                <div class="card flex-md-row mb-4 box-shadow h-md-250">
                    <div class="card-body d-flex flex-column align-items-start">                        
                        <h3 class="mb-0">                            
                            사용자 리뷰 결과
														{{reviewscore}}
														여기에 떠야되는데
														
                            <div>
                                <div v-if="placeInfo.review">
                                    <h6>
                                        noise : {{reviewscore[0]}}
                                        light : {{reviewscore[1]}}
                                        seat : {{reviewscore[2]}}
                                    </h6>
                                </div>
                                <div v-else>
                                    <h6>
                                        아직 등록된 정보가 없습니다.
                                    </h6>
                                </div>
                                <div v-if="isAuthenticated">
                                    <form  method="post"  @submit.prevent="registreview" action="/action_page.php" >
                                        <div class="form-group">
                                            <v-slider v-model="review.noise" label="noise" hint="" min="1" max="3" thumb-label></v-slider>
                                            <v-slider v-model="review.light" label="light" hint="" min="1" max="3" thumb-label></v-slider>
                                            <v-slider v-model="review.seat" label="seat" hint="" min="1" max="3" thumb-label></v-slider>
                                        </div>
                                        <button type="submit" class="btn btn-primary">Submit</button>
                                    </form>
                                </div>
                                <div v-else>
                                    로그인 후 리뷰 등록할 수 있습니다.
                                </div>
							</div>
                        </h3>                        
                    </div>
                    
                </div>
            </div>
            <div class="col-md-6">
                <div class="card flex-md-row mb-4 box-shadow h-md-250">
                    <div class="card-body d-flex flex-column align-items-start">
                        <div class ="row">                            
                            <h3 class="mb-0 ml-3">사장님 설명</h3>
                                <div v-if="placeInfo">
                                    <div v-if="placeInfo.cafe[0]" class="container">
                                        <p>면적 : {{placeInfo.cafe[0].storearea}}
                                        알콜판매 : {{placeInfo.cafe[0].alcoholonoff}}</p>
                                        <p>디저트 판매 : {{placeInfo.cafe[0].dessertonoff}}
                                        흡연실 : {{placeInfo.cafe[0].smokingroom}}</p>
                                        <p>powersoket : {{placeInfo.cafe[0].powersoket}}
                                        parkinglot : {{placeInfo.cafe[0].parkinglot}}</p>
                                        <p>tableinfo1 : {{placeInfo.tableinfo1}}
                                        tableinfo2 : {{placeInfo.tableinfo2}}</p>
                                        <p>tableinfo4 : {{placeInfo.tableinfo4}}
                                        tableinfo5 : {{placeInfo.tableinfo5}}</p>
                                        <p>영업시간 : {{placeInfo.opentime}} ~ {{placeInfo.closetime}}</p>
                                    </div>
                                </div>
                            <!-- The Modal -->
                            <div class="modal" id="myModal">
                                <div class="modal-dialog">
                                    <div class="modal-content">                                    
                                        <!-- Modal Header -->
                                        <div class="modal-header">
                                            <h4 class="modal-title">건물 정보</h4>
                                            <button type="button" class="close" data-dismiss="modal">&times;</button>
                                        </div>                                        
                                        <!-- Modal body -->
                                        <div class="modal-body">
                                            <form>
                                                <button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
                                            </form>
                                        </div>                                        
                                    </div>
                                </div>
                            </div>
                        <!-- 사장님 설명 끝-->
                        </div>                    
                    </div>
                    
                </div>
            </div>
        </div>

        <div class="row mb-2">
            <div class="col-md-6">
                <div class="card flex-md-row mb-4 box-shadow h-md-250">
                    <div class="card-body d-flex flex-column align-items-start">                        
                        <h3 class="mb-0">
                            메뉴
                            <div v-if="!placeInfo.cafe.length">
                                <p v-for="data in placeInfo.cafe.menu" :key="data">
                                    {{data['name']}} {{data['price']}}
                                </p>
                            </div>
                        </h3>                        
                    </div>
                    
                </div>
            </div>
            <div class="col-md-6">
                <div class="card flex-md-row mb-4 box-shadow h-md-250">
                    <div class="card-body d-flex flex-column align-items-start">
                        <div class ="row">                            
                            <h3 class="mb-0 ml-3">주변 정보</h3>                               
                        </div>                    
                    </div>
                    
                </div>
            </div>
        </div>


<!-- 댓글 -->
		<div class="col-md-12">
			<div class="card mb-4 box-shadow">
				<h3>댓글 정보</h3>   
				<div class="card-body flex-column align-items-start">
					<div class="col-md-12 card box-shadow" v-for="comment in commentss[0]" :key="comment">
						{{comment}}
						<h6>{{comment.review_user['username']}}</h6>
						<hr>
						<h6>{{comment.comment}}</h6>
						<h6>[{{comment.create_at}}]</h6>
						<div v-if="comment.review_user['username'] === userName">
							<button @click="deletecomment(comment)">삭제</button>                        
						</div>
					</div>

					<div class="col-md-12" v-if="isAuthenticated">
						<form  method="post"  @submit.prevent="registcomment" action="/action_page.php">
							<div class="form-group">
							<label for="comment">Comment:</label>
							<textarea class="form-control" rows="5" id="comment" name="text" v-model="comments.comment"></textarea>
							</div>
							<button type="submit" class="btn btn-primary">Submit</button>
						</form>
                        
					</div>
					<div  v-if="isAuthenticated == false">
									로그인 후 댓글 가능
					</div>
				</div>                    
			</div>
		</div>
	</v-app>
</template>

<script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>
<script>
import axios_common from '../axios_common';
import swal from 'sweetalert';
export default {
    props:['id','name'],
    components: {
    
    },
    data: function() {
        return {
            userId:'',
            placeId : '',
            placeInfo: {               
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
               library:[],
               studycafe: [],
               location: "",
               phonenumber: "",
               placepicture: [],
               parkinglot: false,
               tableinfo1: '',
               tableinfo2: '',
               tableinfo4: '',
               tableinfo5: '',
               opentime: '',
               closetime: '',
               like_users: [],
               comments: [] 
            },            
            placeCategory: '', // cafe인지 도서관인지 스터디카페인지 
            comments:{
				placename: "",
                comment:"",
				placeId:"",
                review_user: {
                    username: this.$store.getters.userId
                }
            },
            review: {
                review_user: {
                    username: this.$store.getters.userId
                },
				placeid : '',
				placename: '',
                noise: '',
                light: '',
                seat: ''
            },
            onLike:'',
            countLike:'',
            likes: {
                placename: '',
                placeid: ''
            },
            commentss: [],            
            reviewscore: [],
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
        }
    },
    methods: {
			like(){
				this.likes.placename = this.name
				this.likes.placeid = this.id
					const token = this.$store.getters.requestHeader.headers.Authorization //token가져오기
					if (token != 'JWT null'){ // 로그인이 되어있으면
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
				this.comments.placeId = this.id
				this.comments.placename = this.name
					axios_common            
					.post(`/comment/`, this.comments, this.requestHeader)
					.then(response=>{
						const data = response.data;
						this.commentss.push(data);

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
				this.review.placeid = this.id
				this.review.placename = this.name
				console.log(this.review)
				axios_common            
				.post('userreview/', this.review, this.requestHeader)
				.then(response=>{
						console.log(response)
						// 추가하기
				})
				.catch(response=>{
								window.console.log(response.valid);
				});
		}
			},
  mounted(){        
        this.placeId = this.id
								
        var url = '/place/'+this.placeId+'/'        
        axios_common.get(url)
        .then((res)=> {            
            // console.log(res)
            if(res.data.result=="true"){
                var resultdata = res.data.data
                this.name = resultdata.placename
                this.placeInfo.review = resultdata.review
                if(resultdata.cafe.length >0)
                {                    
                    this.placeInfo.cafe.storearea = resultdata.cafe[0].storearea
                    this.placeInfo.cafe.alcoholonoff = resultdata.cafe[0].alcoholonoff
                    this.placeInfo.cafe.dessertonoff = resultdata.cafe[0].dessertonoff
                    this.placeInfo.cafe.smokingroom = resultdata.cafe[0].smokingroom
                    this.placeInfo.cafe.menu = resultdata.cafe[0].menu
                    this.placeInfo.cafe.subdetail = resultdata.cafe[0].subdetail                    
                }
                this.placeInfo.library = resultdata.library
                this.placeInfo.studycafe = resultdata.studycafe 
                this.placeInfo.placepicture = resultdata.placepicture
                this.placeInfo.parkinglot = resultdata.parkinglot
                this.placeInfo.tableinfo1 = resultdata.tableinfo1
                this.placeInfo.tableinfo2 = resultdata.tableinfo2
                this.placeInfo.tableinfo4 = resultdata.tableinfo4
                this.placeInfo.tableinfo5 = resultdata.tableinfo5
                this.placeInfo.opentime = resultdata.opentime
                this.placeInfo.closetime = resultdata.closetime
                this.placeInfo.like_users = resultdata.like_users
								this.placeInfo.comments = resultdata.comments
								this.commentss = resultdata.comments

                var noi = 0
                var lig = 0
                var se = 0
                var reviewlen = this.placeInfo.review.length
                for (var j = 0; j < reviewlen; j++) {
                    noi += this.placeInfo.review[j]['noise']
                    lig += this.placeInfo.review[j]['light']
                    se += this.placeInfo.review[j]['seat']
                }
                var resultnoi = (noi/reviewlen)*(10/3)
								var resultlig = (lig/reviewlen)*(10/3)
								var resultse = (se/reviewlen)*(10/3)
								console.log("주님1")
								this.reviewscore.push(resultnoi.toFixed(0))
								console.log(this.reviewscore)
								this.reviewscore.push(resultlig.toFixed(0))
								console.log(this.reviewscore)
								this.reviewscore.push(resultse.toFixed(0))
								console.log("주님2")
								console.log(this.reviewscore)
								
                this.placeCategory = res.data.cafe || res.data.library || res.data.studycafe
                this.countLike = Object.keys(this.placeInfo.like_users).length 
                // console.log(this.placeInfo)
                // console.log(this.placeInfo.opentime.type())
                const token = this.$store.getters.requestHeader.headers.Authorization //token가져오기

                if (token != 'JWT null'){ // 로그인이 되어있으면
                    this.userId=this.$store.getters.loggedInUser.user_id
                    for (var i=0; i<this.countLike; i++){
                        if (this.placeInfo.like_users[i].id === this.userId) {
                                this.onLike = true
                        }
                    }
                }
            }
            else if(res.data.result=="kakaoInfo") {
                this.placeInfo.subdetail = res.data.placeIntroduction
                this.placeInfo.placepicture = res.data.placeImg
                this.placeInfo.location = res.data.placeAddress
            } else {
                console.log("else")
            }
        })
				.catch(error => console.log(error))
				console.log("asd",this.reviewscore)
		}
}

</script>

<style>
</style>
