<template>
    <button type="button" @click="testyye">전송</button>
</template>

<script>
import axios_common from "../axios_common"
export default {
    
    data(){
        return{
            Place:{
                cafe: {
                    name: "서영카페",
                    storearea: 24,
                    alcoholonoff: false,
                    dessertonoff: true,
                    smokingroom: false,
                    powersoket: 2,
                    menu: [
                        {
                            name: "아메리카노",
                            price: 3000,
                            menupicture: "/media/200113_%EC%B6%9C%EA%B2%B0%ED%99%95%EC%9D%B8%EC%84%9C_%EA%B4%91%EC%A3%BC_1%EB%B0%98_%EC%96%91%EC%98%88%EC%9D%80_HvtGJFl.jpg"
                        },
                        {
                            name: "아메리카노좋아좋아",
                            price: 3333,
                            menupicture: "/media/%EC%BA%A1%EC%B2%98.PNG"
                        }
                    ],
                    subdetail: "22"
                },
                location: "ssss",
                placepicture: [
                    {
                        image: "/media/%EC%BA%A1%EC%B2%98_5SgS7KE.PNG"
                    },
                    {
                        image: "/media/%EC%BA%A1%EC%B2%98_bF4o0EO.PNG"
                    }
                ],
                phonenumber: "111111111111",
                parkinglot: true,
                tableinfo1: 1,
                tableinfo2: 1,
                tableinfo4: 2,
                tableinfo5: 2,
                opentime: 2,
                closetime: 4
            }
            
        }
    },
    methods:{
        testyye()
        {
            axios_common            
            .post('/testyye/',this.Place                        
            ).then(response=>{
                if(response.valid=='True')
                    window.console.log('Success!!');
                else
                    window.console.log(response.valid);
            })
            .catch(response=>{
                window.console.log(response.valid);
            });
        }
    }
}
</script>