<template>
  <div class="Detail">    
    <Detail/>
  </div>
</template>
<script>

import Detail from '../components/Detail.vue';
// import axios from 'axios';

export default {  
  props:['id'],
  components: {
    Detail,
  },
}
</script>
