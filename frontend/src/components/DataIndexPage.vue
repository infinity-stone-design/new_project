<!-- component -->

<template>
<div class="wrap">
  <paginated-list v-bind:listArray="pageArray" v-bind:message="message"/>
  

</div>

  
  
</template>

<script>
import axios from 'axios'
import PaginatedList from './PaginatedList'
export default {
    name: 'simple-pagination',
    components:{
      PaginatedList
    },
    props:{
      message: { 
        type: String, 
        required: true,
      } 
    },
    created () {
      // 컴포넌트가 생성될 때, /api/movies에 요청을 보냅니다.   
        this.$http.get('/api/datas')
          .then((response) => {
            this.pageArray = response.data;
        })
    },
    data () {
    return {
      message : '',
      pageArray: []
    }
    }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Sunflower:300&display=swap&subset=korean');
.table{
  font-family: 'Sunflower', sans-serif;
  width : 1000px;
  height : 80px;
  font-size : 20px;
  border : 1px solid #BDBDBD;
  padding : 10px;
  background-color : white;
  margin-left : 50px;
}
</style>