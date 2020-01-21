<template>
    <div class="main_1">
        <div class="container h-100">
            <div class="row h-100 align-items-center justify-content-center text-center">
                <div class="col-lg-10 align-self-end">
                    <!-- <h1 class="text-uppercase text-white font-weight-bold">Your Favorite Source of Free Bootstrap Themes</h1> -->
                    <img src="../../public/project1_study_main.jpg" alt="" height="50%" width="50%" class="img-responsive center-block img-circle"> 
                    
                </div>
                <div class="col-lg-8 align-self-baseline" id="search_container">
                    <div class="searchbar">
                        <input class="form-control" type="text" placeholder="Search" aria-label="Search">
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- nothing -->
</template>

<script>
export default {
    
}
</script>

<style >
.main_1{
    padding-top: 10rem;
    padding-bottom: calc(10rem - 72px);
    background: linear-gradient(to bottom,rgba(92,77,66,.8) 0,rgba(92,77,66,.8) 100%),url(../../public/project1_study_main.jpg);
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: scroll;
    background-size: cover;
    height: 100vh;
    min-height: 40rem;
    padding-top: 72px;
    padding-bottom: 0;
}
#search_container{
    padding-top: 3rem;
}
</style>