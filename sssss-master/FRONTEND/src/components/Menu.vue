<template>

	<div class="container">
		<div class="nav-scroller py-1 mb-2">
			<nav class="nav d-flex justify-content-center">
				<!-- <router-link class="p-2 text-muted" to="/">홈</router-link> -->
				<!-- <router-link class="p-2 text-muted" to="#" data-toggle="modal" data-target="#myModal">검색</router-link> -->
				<router-link class="p-2 text-muted" to="/map">맵</router-link>
				<!-- <router-link class="p-2 text-muted" to="/Detail">상세정보</router-link> -->
				<router-link class="p-2 text-muted" to="/placelist">전체장소</router-link>
				<!-- <router-link class="p-2 text-muted" to="/registdetail">건물등록</router-link> -->
				
				<div v-if="isAuthenticated" class="mt-2">
					<router-link class="p-2 text-muted" to="/mypage">{{ userName }}님 페이지</router-link>
					<a class="p-2 text-muted" href="#" @click.prevent="logout">로그아웃</a>
					<router-link class="p-2 text-muted" to="/registForm">건물등록</router-link>
				</div>
				<div v-else class="mt-2">
					<router-link class="p-2 text-muted" to="/temlogin">로그인</router-link>
					<router-link class="p-2 text-muted" to="/temsignup">회원가입</router-link>
				</div>
				<!-- <a class="p-2 text-muted" href="/testleek">test</a> -->
				<button class="btn" type="button" style="color:black;" @click="$router.go(-1)">
						<i class="fas fa-angle-left"></i>
				</button>
			</nav>
		</div>
		<!-- <SearchModal/> -->
	</div>
</template>


<script>
// import SearchModal from './SearchModal';

export default {    
	// components: {
	// 	SearchModal
	// },
	methods: {
		logout() {
			this.$store.dispatch("logout");
			this.$router.push("/");
		},
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

<style>
</style>
