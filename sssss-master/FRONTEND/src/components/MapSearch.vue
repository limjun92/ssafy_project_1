<template>
    <div class="fixed-top">
        <nav class="search-info py-0 px-0 col-sm-5 col-md-4 ">
            <div class="container navbar-container navbar-nav p-0" style="">
                <a class="py-3 ml-3" href="/map">
                    <img src="../../public/img/logo41.png" width="25px" height="30px" style="min-width:25px;" alt="">
                </a>
                    <input
                        type="text" 
                        v-model="placename_type" 
                        class="search-input rounded form-control bg-transparent text-white border-0" 
                        placeholder="장소, 위치 검색"  
                        
                        @keyup.enter="search()"
                    >
                    <button class="btn" type="button" style="color:white; font-size:large" @click="search()">
                        <i class="fa fa-search" ></i>
                    </button>


                    <div>

                      <div v-if="isAuthenticated">
                        <div class="btn flex-column btn-sm pt-3" @click="userMypage()" style="outline">
                          <v-icon class='overline' style="color:white;">mdi-account-circle-outline</v-icon>
                            <p class='m-0' style="font-size: 10px; color:white;">
                              My page
                            </p>
                        </div>
                        <!-- <button class="btn btn-sm">
                          <a class="text-muted" href="#" @click.prevent="logout">logout</a>
                        </button> -->
                      </div>

                      <div v-else>
                          <div class="btn flex-column btn-sm pt-3"  @click="userLogin()">
                            <v-icon class='overline' style="color:white;">mdi-lock-outline</v-icon>
                            <p class='m-0' style="font-size: 10px; color:white;">
                              Login
                            </p>
                          </div>      
                      </div>  
             
                    </div>
                   
                        <div class="btn flex-column btn-sm  pt-3 mr-1">
                          <v-icon  
                            class="overline"
                            @click="expanded = !expanded"
                            style="color:white;"
                          >
                            mdi-alert-circle-outline
                          </v-icon>
                          <p class='m-0' style="font-size: 10px; color:white;">
                            Info
                          </p>
                        </div>
                    </div>
                    <v-list v-show="expanded" dense style="border-radius:0">
                      <div style="overflow:scroll; height:480px">
                        <v-container>
                         <img src="../../public/img/basicinfo/BasicInfo.png" alt="">
                      </v-container>
                      </div>
                    </v-list>


                <!-- <div v-if="isAuthenticated" class="d-flex flex-row">
                    <button class="btn" type="button" style="color:white;" @click="userMypage()">
                        {{ userName }}님
                    </button>
                    <a class="p-2 text-muted" href="#" @click.prevent="logout">logout</a>
                </div>
                <div v-else class="d-flex">
                    <button class="btn flex-row px-3px" type="button" style="color:white;" @click="userLogin()">
                        <i class="fas fa-user"></i>
                    </button>      
                    <button class="btn flex-row px-3px" type="button" style="color:white;" @click="userSignup()">
                        <i class="fas fa-user"></i>
                    </button>  
                </div>       -->
    
        </nav>
        
    </div>

</template>

<script>


export default {

    components:{

    },
	data() {
        return {
            expanded:false,
            items: [{ },],
            logo:'',
            placename_type: '', // 검색 키워드
            filter: {
                all: true
            }
        }
    },
    methods: {
        search() {
            this.$emit('search_placename_type', this.placename_type)
        },
        userMypage() {
            this.$router.push("/mypage");
        },
        userLogin() {
            this.$router.push("/temlogin");
        },
        userSignup() {
            this.$router.push("/temsignup");
        },
		// logout() {
		// 	this.$store.dispatch("logout");
		// 	this.$router.push("/");
		// },
    },
    computed: {
		isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
    userName() {
			return this.$store.getters.loggedInUser.username;
    },
  
    
	},
}
</script>

<style scoped>
.navbar-nav {
  flex-flow: nowrap;
  padding-bottom: 6px
}

.navbar {    
    /* padding: 0.rem,0.rem; */
    flex-flow: nowrap;
    display: inline-flex ;
    
   
}

.search-input{
    font-size:large; 
}

.search-input::placeholder{
    color: white;
}


@media screen and (max-width: 750px) {
	.search-info {
        background-color:#FF80AB;
	}
}
@media screen and (min-width: 750px) {
	.search-info {
        position: absolute;
        top: 20px;
        left: 20px;
        background-color:#FF80AB;

        /* border-radius: 10px; */
	}
}

.search-info {
  box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
  transition: all 0.3s cubic-bezier(.25,.8,.25,1);
}
.search-info:hover {
  box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
}

</style>
