<template>
  <div id="app">
    <!-- <div class='headtitle'><h2>SSAFY HRM LIST</h2></div>
    <div class='search_box'>
      <nav>
        <router-link class="btn btn-primary" to="/">Q and A 보기</router-link> |
        <router-link class="btn btn-primary" to="/add">사원질문추가</router-link> |
        <router-link class="btn btn-primary" to="/searchTitle">제목으로 질문 찾기</router-link> |
        <router-link class="btn btn-primary" to="/searchUserid">아이디로 질문 찾기</router-link> |
        <router-link class="btn btn-primary" to="/chartcustomer">부서별ㅁㄴㅇㄹ 인원보기</router-link> |
        <router-link class="btn btn-primary" to="/chartpiecustomer">부서별ㅁㄴㅇㄹ 인원보기2</router-link>
      </nav>
    </div>
    <router-view/> -->
    <Menu/>    
    <Main/>
  </div>
</template>

<script>
import Main from './components/Main.vue'
import Menu from './components/Menu.vue'
export default {
  name: 'app',
  components: {
    Main,
    Menu
  }
}
</script>

<style>
#app {
  
  
}
</style>
