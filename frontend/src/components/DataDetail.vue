<!-- component -->
<template>
<table cellspacing = '10'>
  <tr>
    <table id = "title">
      <tr>
        <category id="category">[{{$route.params.id}}]</category>
       <span>{{d.title}}</span>
      </tr>
      <tr>
        <table id='side'>
        <side id="side">
         <a id="a">작성자 : 관리자</a>  <a id="a"> | </a>  <a id="a">접수기간 : 2019.08.09 ~ 2019.08.20</a>
        </side>
        </table>
        <content id="content">
          <tr>
              <c id="detail">세부페이지<링크></c>
         <br/>
         <span>{{d.subtitle}}</span>
          <c style="font-size:1px">
         <br/>
         </c>
        <span>{{d.target}}</span>
         <br/>
         <span>{{d.contents}}</span>
        <br/>
         <span>{{d.how}}</span>
         <br/>
         <br/>
         <br/>
         <br/>
        </tr>
        </content>
        
      </tr>
    
      
    </table>
  </tr>
 
</table>

  
  
</template>
<script>


export default {
  created (){
    var id = this.$route.params.id
    this.$http.get('/api/datas/'+id)
        .then((response) => {
          this.d = response.data[0]
        })
  },
  data () {
    return {
      d: [],
    }
  },
   
}

</script>
<style>
@import url('https://fonts.googleapis.com/css?family=Nanum+Gothic&display=swap&subset=korean');
@import url('https://fonts.googleapis.com/css?family=Sunflower:300&display=swap&subset=korean');

#title{
  font-family: 'Nanum Gothic', sans-serif;
  width : 1000px;
  height : 80px;
  font-size : 25px;
  border : 1px solid #BDBDBD;
  padding : 20px;
  background-color : white;
  margin-left : 50px;
  margin-top: 10px
}
#side{
  font-family: 'Nanum Gothic', sans-serif;
  width : 1000px;
   height : 25px;
  font-size : 15px;
  text-align: right;
  
  padding : 10px;
 
  margin-left : 5px;
}
#a{
  font-family: 'Nanum Gothic', sans-serif;
  width : 1000px;
  font-size : 15px;
 
  margin-right : 20px;
}
#category{
  font-size : 20px;
  margin-left: 10px;
  margin-right : 15px;
  color:rgb(42, 114, 156)
}
#content{
   font-family: 'Nanum Gothic', sans-serif;
   height : 30px;
   width : 800px;
  font-size : 25px;
  padding : 10px;
  margin-left : 50px;
}
#detail
{
  
  font-size : 15px;
  color:blue;
}

</style>