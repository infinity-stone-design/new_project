<!-- src -->

<template>
  <div id="app">
  <div>  
    <img src = "./assets/1511.jpg" id = "bg">
  </div>
    <div id = "top">
      <form id = "search">
        <router-link :to="{name: 'index'}"><img src = "./assets/logo.png" id = "logo"></router-link>

        <input type = "text" v-model = "message" id = "text" placeholder="  검색어를 입력해주세요">

        <img src = "./assets/search.png" id = "img">
        

      </form>
    </div>
      <div id = "side">
        <div id = "side_title">
          <div style = "padding: 10px;" align=left>
          분류별 찾기
          </div>
        </div><br>
        <form id = "form">
          연령<br/>
          <div class = "detail">
          <input type = "checkbox" id="영유아" value= "영유아" v-model="checkedAge">
          <label for="영유아"> 영유아 </label>
           <br/>
          <input type = "checkbox" id="청소년" value="청소년" v-model="checkedAge"> 
          <label for="청소년"> 청소년 </label>
          <br/>
          <input type = "checkbox" id="노인" value="노인" v-model="checkedAge"> 
          <label for ="노인"> 노인 </label>
           <br/>
           ------------------------
          </div>
          지역 <br/>
          <div class = "detail">
          <input type = "checkbox" id="서울" value="서울" v-model="checkedAge"> 
          <label for="서울"> 서울특별시 </label>
          <br/>
          <input type = "checkbox" id="부산" value="부산" v-model="checkedAge">
          <label for="부산"> 부산광역시 </label>
          <br/>
          <input type = "checkbox" id="광주" value="광주" v-model="checkedAge"> 
          <label for ="광주"> 광주광역시 </label>
          <br/>
          <input type = "checkbox" id="대구" value="대구" v-model="checkedAge">
          <label for ="대구"> 대구광역시 </label>
          <br/>
          <input type = "checkbox" id="인천" value="인천" v-model="checkedAge">
          <label> 인천광역시 </label>
          <br/>
          <input type = "checkbox" id="대전" value="대전" v-model="checkedAge">
          <label for = "대전"> 대전광역시 </label>
          <br/>
          <input type = "checkbox" id="울산" value="울산" v-model="checkedAge">
          <label for="울산"> 울산광역시 </label>
          <br/>
          <input type = "checkbox" id="경기" value="경기" v-model="checkedAge">
          <label for="경기"> 경기도 </label>
          <br/>
          <input type = "checkbox" id="충청북" value="충청북" v-model="checkedAge">
          <label for="충북"> 충청북도 </label>
          <br/>
          <input type = "checkbox" id="충청남" value="충청남" v-model="checkedAge">
          <label for="충남"> 충청남도 </label>
          <br/>
          <input type = "checkbox" id="강원" value="강원" v-model="checkedAge">
          <label for="강원"> 강원도 </label>
          <br/>
          <input type = "checkbox" id="경상북" value="경상북" v-model="checkedAge">
          <label for="경북"> 경상북도 </label>
          <br/>
          <input type = "checkbox" id="경상남" value="경상남" v-model="checkedAge">
          <label for="경남"> 경상남도 </label>
          <br/>
          <input type = "checkbox" id="전라북" value="전라북" v-model="checkedAge">
          <label for="전북"> 전라북도 </label>
          <br/>
          <input type = "checkbox" id="전라남" value="전라남" v-model="checkedAge">
          <label for="전남"> 전라남도 </label>
          <br/>
          <input type = "checkbox" id="제주" value="제주" v-model="checkedAge">
          <label for="제주"> 제주도 </label>
          <br/>
          ------------------------
          </div>
          목적 <br/>
          <div class = "detail">
          <input type = "checkbox" id="취업" value="취업" v-model="checkedAge">
          <label for="취업"> 취업 </label>
          <br/>
          <input type = "checkbox" id="금전" value="금전" v-model="checkedAge">
          <lable for="금전"> 금전 </lable>
          <br/>
          <input type = "checkbox" id="주거" value="주거" v-model="checkedAge">
          <label for="주거"> 주거 </label>
          <br/>
          <input type = "checkbox" id="교육" value="교육" v-model="checkedAge">
          <label for="교육"> 교육 </label>
          <br/>
          <input type = "checkbox" id="의료" value="의료" v-model="checkedAge">
          <label for="의료"> 의료 </label>
          <br/>
          <input type = "checkbox" id="문화" value="문화" v-model="checkedAge">
          <label for="문화"> 문화 </label>
          <br/>
          ------------------------
          </div> 
          기타 <br/>
          <div class = "detail">
          <input type = "checkbox" id="저소득층" value="저소득층" v-model="checkedAge">
          <label for="저소득층"> 저소득층 </label>
          <br/>
          <input type = "checkbox" id="임산부" value="임산부" v-model="checkedAge">
          <label for="임산부"> 임산부 </label>
          <br/>
          <input type = "checkbox" id="장애인" value="장애인" v-model="checkedAge">
          <label for="장애인"> 장애인 </label>
          <br/>
  <data-index-page :check-list="checkedAge"/>
  
 
          </div> 
        </form> 
      </div>

      <div id = "next">
        <router-view v-bind:checkArray="checkedAge" v-bind:message="message"/>
        
      </div>
    
   

  </div>
</template>

<script>

document.addEventListener("keydown",function(event){
  if(event.keyCode === 13){
    event.preventDefault();
  }
},true);

export default {
    name:"app",
   data() {
     return{
      checkedAge: [],
      message : ''
     }
  }
}

</script>


<style>
@import url('https://fonts.googleapis.com/css?family=Nanum+Gothic&display=swap&subset=korean');

#bg{
  position : absolute; top:0; left:0;
  opacity : 0.25;
  width : 100%;
  height : 100%;
  z-index: -1;
}

#logo{
  position : relative;
  right : 10px;
  height : 70px;
  width : 150px;
}
#img{
  position : relative;
  width : 42px;
  height : 42px;
  top : -16px;
  left : -3px;
  border : 2px solid #3b78a3;
}
#search{
  margin-top : 50px;
}
.detail{
  font-size : 15px;
  margin-left : 5px;
  color : rgb(90, 91, 153);
  font-weight:bold;
  line-height: 25px;
}

#form{
  margin-left:10px;
  text-align: left;
  font-size: 20px;
  width : 150px;
  height : 850px;
  color : rgb(81, 121, 156);
  font-weight:bold;
  line-height: 30px;
}

#side_title{
  color : rgb(50, 99, 145);
  font-size : 25px;
  font-weight:bold;
  border-bottom : 2px solid rgb(9, 80, 172, 0.808);
  width : 160px; 
}

#side{
  width : 150px;
}
#top{
  width : 1600px;
  height : 100px;
  text-align : center;
}

#text{
  position : relative;
  top : -35px;
  width : 450px;
  height : 40px;
  border : 2px solid #3b78a3;
}

#button{
  height : 37px;
  width : 150px;
}

#next{
  margin-left: 175px;
}

</style>
