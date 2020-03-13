<template>
<v-app>
  
    <div class="breadcumb-area" style="background-image: url(../../img/bg-img/bg-coffee10.jpg);">
            <div class="container h-100">
                <div class="row h-100 align-items-center">
                    <div class="col-12">
                        <div class="logo_area text-center">
                            <h2 style="color:white;">My Page</h2>
                            <h6 class="mb-3" style="color:white;">  {{userInfo.id}}님 안녕하세요 </h6>
                            <v-btn x-small flat>
                              <a class="text-muted" href="#" @click.prevent="logout" style="color: white">logout</a>
                            </v-btn>
                        </div>
                    </div>
                </div>
            </div>
        </div>
  <v-container class='mt-3'>
    <v-row justify="center" cols='12'>
    <v-card width= "800px">
        <v-col
          class='px-12'
        >

				

        <v-form class='mt-4'>
          <v-text-field
            v-model="userInfo.id"
            class="m-3"
            label="ID"
            type="text"
            color="pink lighten-3"
			readonly
          ></v-text-field>
			<v-text-field
            v-model="userInfo.name"
            class="m-3"
            label="이름"
            type="text"
            color="pink lighten-3"
			readonly
          ></v-text-field>
			<v-text-field
            v-model="userInfo.age"
            class="m-3"
            label="나이"
            type="text"
            color="pink lighten-3"
			readonly
          ></v-text-field>
			<div class="text-center d-flex flex-column" v-if="userInfo.ceo">
				<router-link to="/registForm"><v-btn class="col-12 col-sm-4 purple lighten-2 white--text ma-2">cafe 등록</v-btn></router-link>
				<router-link to="/registformlibrary"><v-btn class="col-12 col-sm-4 purple lighten-2 white--text ma-2">library 등록</v-btn></router-link>
				<router-link to="/registformstudycafe"><v-btn class="col-12 col-sm-4 purple lighten-2 white--text ma-2">study cafe 등록</v-btn></router-link>
			</div>

			<v-container fluid v-else>
      <div class="d-flex justify-content-center"> 
        <v-btn class="purple lighten-2 white--text mr-3" @click.native="show = !show">{{ show ? '설문 항목 가리기' : '설문 항목 보이기' }}</v-btn>
      </div>
			<v-slide-y-transition>
			<v-card-text v-show="show">
        <v-container fluid>
          <v-checkbox color="purple lighten-3" v-model="userInfo.noise1" label="음악이 잔잔함" value="1"></v-checkbox>
        </v-container>
        <v-container fluid>
          <v-checkbox color="purple lighten-3" v-model="userInfo.noise2" label="백색소음이 있는" value="2"></v-checkbox>
        </v-container>
        <v-container fluid>
          <v-checkbox color="purple lighten-3" v-model="userInfo.noise3" label="소음이 있어 대화하기 편함" value="3"></v-checkbox>
        </v-container>
        <v-container fluid>
          <v-checkbox color="purple lighten-3" v-model="userInfo.light1" label="백색등" value="3"></v-checkbox>
        </v-container>
        <v-container fluid>
          <v-checkbox color="purple lighten-3" v-model="userInfo.light2" label="황색등" value="2"></v-checkbox>
        </v-container>
        <v-container fluid>
          <v-checkbox color="purple lighten-3" v-model="userInfo.light3" label="어두움" value="1"></v-checkbox>
        </v-container>
        <v-container fluid>
          <v-checkbox color="purple lighten-3" v-model="userInfo.seat1" label="의자가 딱닥함" value="1"></v-checkbox>
        </v-container>
        <v-container fluid>
          <v-checkbox color="purple lighten-3" v-model="userInfo.seat2" label="의자가 푹신함" value="3"></v-checkbox>
        </v-container>
        <v-container fluid>
          <v-checkbox color="purple lighten-3" v-model="userInfo.seat3" label="책상이 넓음" value="3"></v-checkbox>
        </v-container>
        <div class="d-flex justify-content-end"> 
          <v-btn  color="purple darken-3 white--text" @click="updateinfo">수정</v-btn>
        </div>
        </v-card-text>
        </v-slide-y-transition>
		</v-container>
			
        </v-form>
        </v-col>

    </v-card>
    </v-row>
  </v-container>
</v-app>

</template>

<script>
import axios_common from '../axios_common';

export default {
	data() {
		return {
			userInfo: {
				id: '',
				password: '',
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
			show: false
		}
	},
	computed: {
    requestHeader() {
			return this.$store.getters.requestHeader;
		},
		userId() {
			return this.$store.getters.userId;
		} 
	},
	methods: {
    updateinfo(){
		if (this.userInfo.noise1 == "")
        {
          this.userInfo.noise1 = "0"
        }
        if (this.userInfo.noise2 == "")
        {
          this.userInfo.noise2 = "0"
        }
        if (this.userInfo.noise3 == "")
        {
          this.userInfo.noise3 = "0"
        }
        if (this.userInfo.light1 == "")
        {
          this.userInfo.light1 = "0"
        }
        if (this.userInfo.light2 == "")
        {
          this.userInfo.light2 = "0"
        }
        if (this.userInfo.light3 == "")
        {
          this.userInfo.light3 = "0"
        }
        if (this.userInfo.seat1 == "")
        {
          this.userInfo.seat1 = "0"
        }
        if (this.userInfo.seat2 == "")
        {
          this.userInfo.seat2 = "0"
        }
        if (this.userInfo.seat3 == "")
        {
          this.userInfo.seat3 = "0"
        }
			axios_common.put(`/mypage/${this.userId}/`, this.userInfo, this.requestHeader)
			.then( res => {
				console.log(res)
			})
			.catch(() => {
				this.errMessage = "항목에 빠진게 있는지 확인해주세요.";
			});
		},
		logout() {
			this.$store.dispatch("logout");
			this.$router.push("/map");
		},
	},
	mounted(){
			axios_common.get(`/mypage/${this.userId}/`, this.requestHeader)
			.then( res => {
				console.log(res)
				this.userInfo.id = res.data.username;
				this.userInfo.age = res.data.age;
				this.userInfo.name = res.data.name;
				this.userInfo.ceo = res.data.ceo;
				this.userInfo.noise1 = res.data.noise1;
				this.userInfo.noise2 = res.data.noise2;
				this.userInfo.noise3 = res.data.noise3;
				this.userInfo.light1 = res.data.light1;
				this.userInfo.light2 = res.data.light2;
				this.userInfo.light3 = res.data.light3;
				this.userInfo.seat1 = res.data.seat1;
				this.userInfo.seat2 = res.data.seat2;
				this.userInfo.seat3 = res.data.seat3;
			})
			.catch(error => console.log(error))
	}
}
</script>

<style>

</style>
