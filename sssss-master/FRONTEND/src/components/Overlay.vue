<template>
    <div class="container">
        <div class="row">
            <div class="col-sm-4 col-6">
                <img class="test" src="../../public/img/beer.svg" @click="makeEffect($event)">
                <div class="sub mt-3">
                    매장 넓이: 132
                </div>
            </div>
            <div class="col-sm-4 col-6">
                <img class="test" src="../../public/img/beer.svg" @click="makeEffect($event)">
                <div class="sub mt-3">
                    매장 넓이: 132
                </div>
            </div>
            <div class="col-sm-4 col-6">
                <img class="test" src="../../public/img/beer.svg" @click="makeEffect($event)">
               <div class="sub mt-3">
                    매장 넓이: 132
                </div>
            </div>
            <div class="col-sm-4 col-6">
                <img class="test" src="../../public/img/beer.svg" @click="makeEffect($event)">
                <div class="sub mt-3">
                    매장 넓이: 132
                </div>               
            </div>
            <div class="col-sm-4 col-6">
                <img class="test" src="../../public/img/beer.svg" @click="makeEffect($event)">
                <div class="sub mt-3">
                    매장 넓이: 132
                </div>
            </div>
            <div class="col-sm-4 col-6">
                <img class="test" src="../../public/img/information.png" @click="makeEffect($event)">
                <div class="sub mt-3">
                    매장 넓이: 132
                </div>
            </div>
        </div>
        
    </div>
</template>

<script>
export default {
    methods:{
        makeEffect(e){
            var target = e.target;
            target.classList.add('animation')
            var subdivs = document.getElementsByClassName('sub')
            for(var i = 0 ; i < subdivs.length; i++)
            {
                if(subdivs[i].style.display=="block")
                    subdivs[i].style.display="none"
            }
            var sub = target.nextSibling
            sub.style.display="block"
            setTimeout(function(){
                target.classList.remove('animation')
            },1000)
        }
    }

}
</script>

<style scoped>
.sub{
    display: none;
    /* width:100px;
    height:50px; */
    background-color: pink;    
    border-radius: 10px;
    opacity: 8;    
    margin:0 auto;
}

.animation{
   transform: scale(1.2);
   -webkit-transition: all 1s ease;  
   -moz-transition: all 1s ease;  
   -o-transition: all 1s ease;  
   -ms-transition: all 1s ease;  
   transition: all 1s ease;  
}

</style>