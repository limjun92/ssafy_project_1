import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import TemLogin from '../views/TemLogin.vue'
import TemSignup from '../views/TemSignup.vue'
// import Home from '../components/Home.vue'
//import Detail from '../views/Detail.vue'
import Detail from '../components/Detail.vue'
import Mypage from '../views/Mypage.vue'
import Map from '../views/Map.vue'
import NuneddineMap from '../views/NuneddineMap.vue'
import PlaceList from '../views/PlaceList.vue'

import testleek from '../views/testleek.vue'

import RegistForm from '../views/RegistForm.vue'
import RegistLibrary from '../views/RegistLibrary.vue'
import RegistStudycafe from '../views/RegistStudycafe.vue'
import temdetail from '../views/temdetail.vue'
import Overlay from '../views/Overlay.vue'


Vue.use(VueRouter)

export default new VueRouter({
  mode: "history",
  routes: [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/temlogin',
    name: 'temlogin',
    component: TemLogin
  },
  {
    path: '/temsignup',
    name: 'temsignup',
    component: TemSignup
  },
  {
    path:'/detail/:id/:name',
    //path:'/detail/:id',
    //path:'/detail',
    name: 'detail',
    props:true,
    component: Detail
  },
  {
    path: '/temdetail/:id/',
    name: 'temdetail',
    props:true,
    component: temdetail
  },
  {
    path:'/registform',
    name: 'registform',
    component: RegistForm
  },
  {
    path:'/registformstudycafe',
    name: 'registformstudycafe',
    component: RegistStudycafe
  },
  {
    path:'/registformlibrary',
    name: 'registformlibrary',
    component: RegistLibrary
  },
  {
    path:'/map',
    name: 'map',
    component: Map
  },
  {
    path:'/neneddinemap',
    name: 'neneddinemap',
    component: NuneddineMap
  },
  {
    path:'/placelist',
    name:'placelist',
    component: PlaceList
  },
  {
    path:'/testleek',
    name:'testleek',
    component: testleek
  },
  {
    path:'/Overlay',
    name:'Overlay',
    component: Overlay
  },
  {
    path:'/mypage',
    name:'mypage',
    component: Mypage
  },
]
})

// const router = new VueRouter({
//   routes
// })

// export default router
