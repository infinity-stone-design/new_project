<!-- src -->

<template>
  <div id="app">
    <div id = "top">
      <form id = "search">
        <router-link :to="{name: 'index'}"><img src = "./assets/logo.png" id = "logo"></router-link>
        <input type = "text" id = "text">
        <img src = "./assets/search.png" id = "img">
      </form>
    </div>
      <div id = "side">
        <div id = "side_title">
          <div style = "padding: 5px;">
          필터링 목록
          </div>
        </div>
        <form id = "form">
          연령 </br>
          <div class = "detail">
          <input type = "checkbox"> 영유아 </br>
          <input type = "checkbox"> 청소년 </br>
          <input type = "checkbox"> 노인 </br>
          </div>
          지역 </br>
          <div class = "detail">
          <input type = "checkbox"> 서울특별시 </br>
          <input type = "checkbox"> 부산광역시 </br>
          <input type = "checkbox"> 광주광역시 </br>
          <input type = "checkbox"> 대구광역시 </br>
          <input type = "checkbox"> 인천광역시 </br>
          <input type = "checkbox"> 대전광역시 </br>
          <input type = "checkbox"> 울산광역시 </br>
          <input type = "checkbox"> 경기도 </br>
          <input type = "checkbox"> 충청북도 </br>
          <input type = "checkbox"> 충청남도 </br>
          <input type = "checkbox"> 강원도 </br>
          <input type = "checkbox"> 경상북도 </br>
          <input type = "checkbox"> 경상남도 </br>
          <input type = "checkbox"> 전라북도 </br>
          <input type = "checkbox"> 전라남도 </br>
          <input type = "checkbox"> 제주도 </br>
          </div>
        
          목적 </br>
          <div class = "detail">
          <input type = "checkbox"> 취업 </br>
          <input type = "checkbox"> 금액 </br>
          <input type = "checkbox"> 주거 </br>
          <input type = "checkbox"> 교육 </br>
          <input type = "checkbox"> 의료 </br>
          <input type = "checkbox"> 문화 </br>
          </div> 
          기타 </br>
          <div class = "detail">
          <input type = "checkbox"> 저소득층 </br>
          <input type = "checkbox"> 임산부 </br>
          <input type = "checkbox"> 장애인 </br>
          </div> 
        </form> 
      </div>

      <div id = "next">
        <router-view/>
      </div>
    
   

  </div>
</template>


<style>
@import url('https://fonts.googleapis.com/css?family=Nanum+Gothic&display=swap&subset=korean');

#logo{
  position : relative;
  right : 50px;
  height : 70px;
  width : 150px;
}
#img{
  position : relative;
  width : 42px;
  height : 42px;
  top : -16px;
  left : -3px;
  border : 2px solid #58ACFA;
}
#search{
  margin-top : 50px;
}
.detail{
  font-size : 15px;
  margin-left : 10px;
}
#side_title{
  background-color : white;
  color : #58ACFA;
  font-size : 25px;
  border-bottom : 2px solid #BDBDBD;
   width : 150px;
   
}
#form{
 text-align: left;
  font-size: 20px;
  line-height: 1.5em;
  width : 150px;
  height : 850px;
  
}
#side{
  width : 150px;
}
#top{
  width : 1500px;
  height : 100px;
  text-align : center;
  background-color : white;
}

#text{
  position : relative;
  top : -35px;
  width : 450px;
  height : 40px;
  border : 2px solid #58ACFA;
}
#button{
  height : 37px;
  width : 150px;
}
#next{
  width : 1300px;
  height : 960px;
  margin-left: 175px;
  background-color : #F2F2F2;
  
}


</style>
