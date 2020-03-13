<template>
  <div class="container">
    <h1 >DB 장소 목록</h1>
      <div class="row" >


        <div v-for="placeData in placeDatas" :key="placeData.id">
          <p>{{placeData}}</p>
        </div>

        <button v-for="simpleData in simpleDatas" v-bind:key="simpleData[1]" class="p-2 text-muted">
          {{simpleData[0]}}
          <router-link :to="`/detail/${simpleData[4]}/`">
          {{ simpleData[2] }} 
          </router-link>
          {{ simpleData[3] }}
        </button>
      </div>
  </div>
</template>

<script>
import axios from 'axios'


export default {
  name: 'PlaceList',
  components: {
  },
  data () {
    return {
      placeDatas:{},
      simpleDatas:[], // 종류, id, 이름, 장소 순서대로 들어가 있음
    }
  },
  methods:{
  },
  
  mounted() {
    axios.get('http://localhost:8000/api/v1/place/')
        .then((res)=>{
          this.placeDatas = res.data
          for (var i=0; i<this.placeDatas.length; i++){
            if (this.placeDatas[i].cafe.length > 0) {
              this.simpleDatas.push(['cafe', this.placeDatas[i].id, this.placeDatas[i].placename, this.placeDatas[i].location, this.placeDatas[i].placeid])
            } else if (this.placeDatas[i].library.length > 0) {
              this.simpleDatas.push(['library', this.placeDatas[i].id, this.placeDatas[i].placename, this.placeDatas[i].location, this.placeDatas[i].placeid])
            } else if (this.placeDatas[i].studycafe.length > 0) {
              this.simpleDatas.push(['studycafe', this.placeDatas[i].id, this.placeDatas[i].placename, this.placeDatas[i].location, this.placeDatas[i].placeid])
            }
          }
        })

    
   
  },

  computed: {

  }

}
</script>

<style>
select {
  display: block;
  width: 50% !important;
  margin: 2rem auto !important;
}
</style>
