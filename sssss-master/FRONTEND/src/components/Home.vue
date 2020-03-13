<template>
    <div class="main_1 "  @click="get_map">
        <div class="container h-100">
            <div class="row h-100 align-items-center justify-content-center text-center">
                <div class="col-lg-10 align-self-end" >
                    <!-- <h1 class="text-uppercase text-white font-weight-bold">Your Favorite Source of Free Bootstrap Themes</h1> -->
                    <!-- <img src="../../public/img/start.png" alt="" height="20%" width="20%" class="rounded-circle" @click="get_map">  -->
                </div>
                <!-- <div class="col-lg-8 align-self-baseline" id="search_container">
                    <div class="searchbar">
                        <input class="form-control" type="text" placeholder="Search" aria-label="Search">
                    </div>
                </div> -->
            </div>
        </div>
    </div>
    <!-- nothing -->
</template>

<script>

import router from '../router'

export default {
    // mounted(){
    //     router.push('/map')
    // },
    methods: {
        get_map(){
            console.log("asdasd")
            router.push('/map')
        },
    }
}
</script>

<style >
.main_1{
    padding-top: 10rem;
    padding-bottom: calc(10rem - 72px);
    background: linear-gradient(to bottom,rgba(212, 182, 161, 0.0) 0,rgba(238, 166, 214, 0.3) 100%),url(../../public/img/landing_logo2.png);
    /* background: url(../../public/img/landing_logo2.png);  */
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: scroll;
    background-size: cover;
    height: 100vh;
    /* min-height: 40rem; */
    padding-top: 72px;
    padding-bottom: 0;
}
#search_container{
    padding-top: 3rem;
}
</style>