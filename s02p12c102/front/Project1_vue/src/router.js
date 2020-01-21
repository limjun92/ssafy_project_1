import Vue from "vue";
import Router from "vue-router";
import Main from "./components/Main.vue";
// import listboardAll from "./components/listboardAll.vue";
// import Listitem from "./components/Listitem.vue";
// import Main from "./components/Main.vue";
// import Intake from "./components/Intake.vue";
// import searchTitle from "./components/searchTitle.vue";
// import searchUserid from "./components/searchUserid.vue";
// import ChartPieCustomer2 from "./components/ChartPieCustomer2.vue";
Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "Main",
      alias: "/Main",
      component: Main
    },
    // {
    //   path: "/listboardAll",
    //   name: "listboardAll",
    //   alias: "/listboardAll",
    //   component: listboardAll
    // },
    // {
    //   path:"/listitem",
    //   name: "Listitem",
    //   alias: "/Listitem",
    //   component: Listitem
    // },   
    // {
    //   path: "/searchTitle",
    //   name: "searchTitle",
    //   component: searchTitle
    // },
    // {
    //   path: "/searchUserid",
    //   name: "searchUserid",
    //   component: searchUserid
    // },    
    // {
    //   path:"/intake",
    //   name: "Intake",
    //   alias: "/Intake",
    //   component: Intake
    // }, 
    
  ]
});
