<!-- component -->

<template>
<div class="wrap">
  
    <table class = "table">
      <tr>
        <span>{{d.title}}</span>
      </tr>
      <tr>
        <span>{{d.subtitle}}</span>
      </tr>
    </table>
 
</div>
  
  
</template>

<script>


export default {
  created (){
    var id = this.$route.params.id;
    this.$http.get('/api/datas/'+id)
        .then((response) => {
          this.d = response.data[0]
        })
  },
  data () {
    return {
      d: []
    }
  },
   
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