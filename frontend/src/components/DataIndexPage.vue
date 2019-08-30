<!-- component -->

<template>
<div class="wrap">
  <input type = "text" v-model = "search" placeholder = "Search title.."/>

  <div>
    <div v-for="data in filteredList">
      <a v-bind:href="data.id" target="_blank">
        {{data.title}}</br>
        {{data.subtitle}}
      </a>
    </div>
  </div>
</div>

  
  
</template>

<script>

export default {
  created () {
    // 컴포넌트가 생성될 때, /api/movies에 요청을 보냅니다.        
    this.search = ''  
    this.$http.get('/api/datas')
        .then((response) => {
          this.datas = response.data
        })
  },
  data () {
    return {
      
      datas: []
    }
  },
  computed : {
    filteredList(){
      return this.datas.filter(data => {
        return data.title.toLowerCase().includes(this.search.toLowerCase())
      })
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