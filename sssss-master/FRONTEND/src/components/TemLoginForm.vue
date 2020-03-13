<template>
  <v-app id="app">
    <!-- ver.1 시장 -->
    <div class="breadcumb-area" style="background-image: url(../../img/bg-img/bg-coffee10.jpg);">
        <div class="container h-100">
            <div class="row h-100 align-items-center">
                <div class="col-12">
                    <div class="logo_area text-center">
                        <h2 style="color:white;">Login</h2>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <v-app id="inspire">
      <v-content>
        <v-container
          fluid
        >
          <v-layout
            align-center
            justify-center
          >
            <v-flex
              xs12
              sm8
              md4
            >
              <v-card class=""> 
                <v-card
                  color="white"
                  dark
                  flat
                  height="70px"
                >
              
                  <v-card-text style="height:70px; " justify-center>
                  <!-- <p class="display-1 black--text text-center">Login</p> -->
                  <p v-if="errorMessage.length > 0" class="text-right" style="color:red">{{ errorMessage }}</p>
                  <!-- <p v-if="!errorMessage.length" class="brown--text">아이디/비밀번호를 입력해주세요</p> -->
                  </v-card-text>
                  <v-spacer></v-spacer>
                  <v-tooltip bottom>
                    <template v-slot:activator="{ on }">
                      <v-btn
                        
                        icon
                        large
                        target="_blank"
                        v-on="on"
                      >
                        <v-icon>mdi-code-tags</v-icon>
                      </v-btn>
                    </template>
                    <span>Source</span>
                  </v-tooltip>
                  
                </v-card>
                <v-card-text>
                  <v-form>
                    <v-text-field
                      color="purple lighten-2"
                      label="ID"
                      name="ID"
                      type="text"
                      v-model="credential.username"
                    
                      required
                      
                    ></v-text-field>

                    <v-text-field
                      color="purple lighten-2"
                      id="password"
                      label="Password"
                      name="password"
                      type="password"
                      v-model="credential.password"
                     
                    ></v-text-field>
                  </v-form>
                </v-card-text>
                  
                <v-card-actions>
                  <div class="button">
                    <v-btn class="m-3 purple lighten-2 white--text" @click="login">로그인</v-btn>
                    <v-btn class="m-3 purple lighten-3 white--text" @click="signup">회원가입</v-btn>
                  </div>
                  <v-spacer></v-spacer>
                  <!--
                    <div class="m">
                      <v-btn
                        x-small
                        class="mr-4 brown lighten-5"
                      
                      >
                        아이디 찾기
                      </v-btn>

                      <v-btn
                        x-small
                        class="mr-4 brown lighten-4"
                       
                      >
                        비밀번호 찾기
                      </v-btn>
                    </div>
                  -->
                </v-card-actions>
                
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
      </v-content>
    </v-app>
    <!-- ver.1 끝 -->

   

  </v-app>
  

</template>


<script>
// import axios from 'axios'
import axios_common from '../axios_common'
import router from '../router' // 라우터 폴더를 import 하면 자동으로 index.js가 불러와진다

export default {
  data: function() {
    return {
      credential: {
        username: '',
        password: '',
      },
      errorMessage: ""
    }
  },
  methods:{
    login() {
        axios_common.post('/login/', this.credential)
        .then((res)=>{ // 로그인 성공
          this.loading = true
          this.$store.dispatch('login', res.data.token)
          router.push('/map')
        })
        .catch((e)=>{
          this.loginAlert();
          console.log(e)
        })
    },
    signup() {
      router.push('/temsignup')
    },
    // 사용자가 넣은 로그인 정보 validation(django와 다르게 일일히 해주어야한다. 결과적으로 front에서 한 번(vue), backend에서 한 번(django))
    loginAlert() {
      this.errorMessage =
        "아이디 또는 비밀번호가 올바르지 않습니다.";
    },
    onUsername(e) {
      this.credential.username = e.target.value;
    },
    onPassword(e) {
      this.credential.password = e.target.value;
    },
  }
}
</script>

<style>
div.button

{

  margin: auto;
  text-align: center;
  width: 100%;

}


</style>
