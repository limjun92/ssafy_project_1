<template>
  <div id="app" style="height:100%">
    <!-- <Menu/> -->
    
    <!-- <div id="nav"> -->
      <!-- <router-link to="/">Home</router-link> |
      <router-link to="/signup">Signup</router-link> |
      <router-link to="/login">Login</router-link> -->
    <!-- </div> -->
    <!-- <div class="container">  -->
      <!-- <router-view/> -->
    <!-- </div> -->
    <button class="btn fixed-bottom ml-1" type="button" style="color:white; background-color: #FF80AB; bottom:20px; left:10px max-width:20px" @click="$router.go(-1)">
    <!-- <button class="btn fixed-bottom" type="button" style="color:white; background-color: #4d55b2; bottom:5px; left:5px" @click="$router.go(-1)"> -->
        <i class="fas fa-angle-left"></i>
    </button>
    <router-view style="height:100%"/>
  </div>
</template>

<script>
//import Menu from "./components/Menu";
export default {
  name: "app",
  components:{
  //  Menu,
  }
}
</script>
<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;

}

// #nav {
//   padding: 30px;

//   a {
//     font-weight: bold;
//     color: #2c3e50;

//     &.router-link-exact-active {
//       color: #42b983;
//     }
//   }
// }
</style>
