<!-- component -->

<template>
<div class="wrap">
  <paginated-list v-bind:listArray="pageArray" v-bind:checkArray="checkArray" v-bind:message ="message"/>
</div>
  
</template>

<script>
import axios from 'axios'
import PaginatedList from './PaginatedList'
export default {
    name: 'data-index-page',
    components:{
      PaginatedList
    },
    props: {
      message:{
        type:String,
        required : true,
      },
    checkArray: {
      type: Array, 
      required: true 
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
      pageArray: [],
      checkArray: []

    }
  },
  computed:{
      returnArray(){
        return this.checkArray;
      }
      
    }
}

</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Nanum+Gothic&display=swap&subset=korean');

.table{
  font-family: 'Nanum Gothic', sans-serif;
  width : 1000px;
  height : 80px;
  font-size : 20px;
  border : 1px solid #BDBDBD;
  padding : 10px;
  background-color : white;
  margin-left : 50px;
  font-weight:bold;

}
 a:link {
	color: rgb(51, 172, 228, 0.808);
	white-space: nowrap;
	text-decoration: none;
}

a:visited {
  text-decoration: none;
	color: rgb(44, 34, 102, 0.808);
}

a:hover {
  text-decoration: none;
	background-repeat: repeat-x;
	background-position: 100% 100%;
	padding-bottom: 3px;
	color: rgb(9, 80, 172, 0.808);
}

a:active {
  text-decoration: none;
}
</style>