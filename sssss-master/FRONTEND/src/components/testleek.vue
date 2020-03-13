<template>
    <div>        
        <button type="submit" class="btn btn-sm btn-outline-secondary mr-3" @click="test">등록</button>
    </div>
</template>

<script>
import axios_common from "../axios_common";
export default {
    data() {            
		return {
            place:{
                board_name:"asdfasdf",
                comment:["abc","def","asdf","asdf"],
            }            
		}
    },
    methods:{
        test(){
            window.console.log(this.place)            
            axios_common.
            post("/test/",this.place   
            )
            .then(response=>{
                    if(response.valid=='True')
                        window.console.log('Success!!');
                    else
                        window.console.log(response.valid);
            })
        },
        handleFileUpload(){
            var file = this.$refs.file.files[0];            
            var reader = new FileReader();
            var vm = this;
            reader.onload = (e) => {
                window.console.log(e.target);
                vm.Place.image.push({"name":file['name'],"img":e.target.result})                
                //window.console.log(vm.Place.placepicture[0]);
                // window.console.log("onload :");
                 window.console.log(e.target.result);
            };            
            reader.readAsDataURL(file); 
        }
    }
    

}
</script>