<template>
<v-app>
  <div class="breadcumb-area" style="background-image: url(../../img/bg-img/bg-coffee8.jpg);">
        <div class="container h-100">
            <div class="row h-100 align-items-center">
                <div class="col-12">
                    <div class="logo_area text-center">
                        <h2 style="color:white;">Sign up</h2>
                    </div>
                </div>
            </div>
        </div>
    </div>
  <v-container>
    <v-row justify="center" cols='12'>
    <v-card width= "800px">
        <v-col
          class='px-12 mt-3'
        >
        <p class="display-1 mt-3 text-center">
        </p>
        <v-form
          ref="form"
          v-model="form" 
        >
          <v-text-field
            v-model="credential.username"
            :rules="[rules.id_required, rules.length(3)]"
            :counter="3"
            class="m-3"
            label="ID"
            type="text"
            color="purple lighten-2"
          ></v-text-field>
          <v-text-field
            v-model="credential.password"
            :rules="[rules.length(8)]"
            :counter="8"
            class="m-3"
            label="Password"
            type="password"
            color="purple lighten-2"
          ></v-text-field>
          <v-text-field
            v-model="credential.password2"
            :rules="[rules.pwconfirm]"
            class="m-3"
            label="Password Confirm"
            type="password"
            color="purple lighten-2"
          ></v-text-field>
          <v-text-field
            v-model="credential.name"
            :rules="[rules.name_required]"
            class="m-3"
            label="Name"
            type="text"
            color="purple lighten-2"
          ></v-text-field>

          <v-col cols="12">
            <v-slider
              v-model="credential.age"
              color="purple lighten-2"
              track-color="brown lighten-4"
              label="Age"
              hint=""
              min="1"
              max="100"
              thumb-label
            >
           
            </v-slider>
          </v-col>
          
          
          <v-switch
            label="사장님이신가요?"
            class="m-3"
            color="purple lighten-2"
            value="true"
            v-model="credential.ceo"
            @keyup.enter="signup" 
            hide-details
          ></v-switch>

          <v-container fluid v-if="this.credential.ceo!='true'">
            <v-container fluid>
              <v-checkbox color="purple lighten-3" v-model="credential.noise1" label="음악이 잔잔함" value="1"></v-checkbox>
            </v-container>
            <v-container fluid>
              <v-checkbox color="purple lighten-3" v-model="credential.noise2" label="백색소음이 있는" value="2"></v-checkbox>
            </v-container>
            <v-container fluid>
              <v-checkbox color="purple lighten-3" v-model="credential.noise3" label="소음이 있어 대화하기 편함" value="3"></v-checkbox>
            </v-container>
            <v-container fluid>
              <v-checkbox color="purple lighten-3" v-model="credential.light1" label="백색등" value="3"></v-checkbox>
            </v-container>
            <v-container fluid>
              <v-checkbox color="purple lighten-3" v-model="credential.light2" label="황색등" value="2"></v-checkbox>
            </v-container>
            <v-container fluid>
              <v-checkbox color="purple lighten-3" v-model="credential.light3" label="어두움" value="1"></v-checkbox>
            </v-container>
            <v-container fluid>
              <v-checkbox color="purple lighten-3" v-model="credential.seat1" label="의자가 딱닥함" value="1"></v-checkbox>
            </v-container>
            <v-container fluid>
              <v-checkbox color="purple lighten-3" v-model="credential.seat2" label="의자가 푹신함" value="3"></v-checkbox>
            </v-container>
            <v-container fluid>
              <v-checkbox color="purple lighten-3" v-model="credential.seat3" label="책상이 넓음" value="3"></v-checkbox>
            </v-container>
        </v-container>
        </v-form>

        <v-row
          justify='space-around'
        >
          <v-btn
            
            @click="$refs.form.reset()"
          >
            Clear
          </v-btn>
            <v-btn 
              class="purple lighten-2 white--text"
              @click="signup"
            >
              회원가입
            </v-btn>
        </v-row>

        </v-col>

    </v-card>
    </v-row>
  </v-container>
</v-app>

</template>

<script>

import axios_common from '../axios_common';
import router from '../router'
export default {
  data: function(){
    return {
      credential: {
        username: '',
        password: '',
        password2: '',
        age: '',
        name: '',
        ceo: '',
        noise1: '',
        noise2: '',
        noise3: '',
        light1: '',
        light2: '',
        light3: '',
        seat1: '',
        seat2: '',
        seat3: '',
      },
      form: false,
      error: {
				username: '',
				password: '',
				password2: '',
        age: '',
        name: '',
        ceo: '',
      },
      
      rules: {
        email: v => (v || '').match(/@/) || 'Please enter a valid email',
        length: len => v => (v || '').length >= len || `${len} 글자 이상입력해주세요`,
        password: v => (v || '').match(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*(_|[^\w])).+$/) ||
          'Password must contain an upper case letter, a numeric character, and a special character',
        pwconfirm: v => (v || '') == this.credential.password || `비밀번호가 맞지 않습니다.`,
        id_required: v => !!v || '아이디를 입력해주세요.',
        name_required: v => !!v || '이름을 입력해주세요.',
        age_required: v => !!v || '나이를 입력해주세요.',
        min_age: (len) => v => (v || '') >= len || `${len} 이상으로 입력하세요`,
        max_age: (len) => v => (v || '') <= len || `${len} 이하로 입력하세요`,
      },

      // form 모양 바꿀 수 있음
      loading: true,
      shaped: false,
      outlined: false,
      rounded: false,
      solo: false,
      singleLine: false,
      filled: false,
      clearable: true,
      persistentHint: true,
      flat: false,
      counterEn: false,
      counter: 0,
      dense: false,
    }
  },
  methods: {
    signup(){
      if (this.credential.ceo == "" || this.credential.ceo == null) {
        // 일반 사용자 일때
        this.credential.ceo = false;
        if (this.credential.noise1 == "")
        {
          this.credential.noise1 = "0"
        }
        if (this.credential.noise2 == "")
        {
          this.credential.noise2 = "0"
        }
        if (this.credential.noise3 == "")
        {
          this.credential.noise3 = "0"
        }
        if (this.credential.light1 == "")
        {
          this.credential.light1 = "0"
        }
        if (this.credential.light2 == "")
        {
          this.credential.light2 = "0"
        }
        if (this.credential.light3 == "")
        {
          this.credential.light3 = "0"
        }
        if (this.credential.seat1 == "")
        {
          this.credential.seat1 = "0"
        }
        if (this.credential.seat2 == "")
        {
          this.credential.seat2 = "0"
        }
        if (this.credential.seat3 == "")
        {
          this.credential.seat3 = "0"
        }
      } else {
        // 사장님일때 설문항목을 죄다 default값 '1'로..
        this.credential.noise1 = "0"
        this.credential.noise2 = "0"
        this.credential.noise3 = "0"
        this.credential.light1 = "0"
        this.credential.light2 = "0"
        this.credential.light3 = "0"
        this.credential.seat1 = "0"
        this.credential.seat2 = "0"
        this.credential.seat3 = "0"
      }
      axios_common.post('/signup/', this.credential)
      .then( res =>{
        const { token } = res.data;
        console.log(token)
        router.push('/temlogin')
      })
      .catch((e)=>{
        this.loading = true
        console.log(e)
      })
    },
    clear () {
        this.username = ''
        this.password = ''
        this.password2 = ''
        this.age = ''
        this.ceo = null
        this.$validator.reset()
      },
  },

}
</script>

<style>
</style>
