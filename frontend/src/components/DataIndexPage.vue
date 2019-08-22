<!-- component -->

<template>
  <div>
    <div class="wrap">
      <table  cellspacing = '10'>
        <tr v-for="d in datas">
          <table class = "table">
            <tr>
              <strong>
                <span id=title>{{d.title}}</span>
              </strong>
            </tr>
            <tr>
              <span>{{d.subtitle}}</span>
            </tr>
          </table>
        </tr>
      </table>
    </div>
    <div>
      <paginated-list :list-array="pageArray"/>
    </div>
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
    created () {
      // 컴포넌트가 생성될 때, /api/movies에 요청을 보냅니다.          
        this.$http.get('/api/datas')
          .then((response) => {
            this.datas = response.data
            this.pageArray = response.data;
        })
    },
    data () {
    return {
      datas: [],
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