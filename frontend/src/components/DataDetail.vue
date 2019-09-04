
<!-- component -->
<template>
<table cellspacing = '10'>
  <tr>
    <table id = "title">
      <tr><strong>
       <span><category id="category">[{{$route.params.id}}]</category>{{d.title}}</span>
      </strong>
      </tr>
      <tr>
        <table id='side'>
        <side id="side">
        
        <div id = "listdiv">
           <router-link :to="{name: 'index'}" id = "list"><img src="../assets/list_button.png" id = "listimg"></router-link>
          <a id="a">
           작성자 : 관리자</a>
          </div>
        </side>
        </table>
        <hr size=2px noshade color=#BDBDBD></hr>
        <table id="content_table">
        <content id="content">
          <tr>
              
         <br/>
         <b id="one">Q. </b>
         <span ><strong>어떤 혜택인가요?</strong></br></br>
         <d id="q">A. {{d.subtitle}}</d>
         </span>
          <c style="font-size:1px">
         <br/>
         </c>
         </br>
        <hr id="youngin"></hr>
        <span></br><b id="one">Q. </b><strong>대상은 누구인가요?</strong></br></br><d id="q">A. {{d.target}}</d></span>
         <br/>
         </br>
        <hr id="youngin"></hr>
         <span></br><b id="one">Q. </b><strong>어떤 내용인가요?</strong></br></br><d id="q">A. {{d.contents}}</d></span>
        <br/>
        </br>
        <hr id="youngin"></hr>
         <span></br><b id="one">Q. </b><strong>어떻게 신청하나요?</strong></br></br><d id="q">A. {{d.how}}</d></span>
         <br/>
         <br/>
         <br/>
         
        </tr>
        </content>
        </table>
        <li id="detail"><a v-bind:href ="link" target ="_blank"><strong>링크(클릭하면 해당 페이지로 이동합니다)</strong></a></li>
              <!--<a v-bind:href ="link">링크</a>-->
        </br>
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
  method:
  {
    open(){
      window.open(this.d.url,'_blank')
    }
  },
  computed:
  {
    link() {
      return this.d.url
    }
  }
}
</script>
<style>
@import url('https://fonts.googleapis.com/css?family=Nanum+Gothic&display=swap&subset=korean');
@import url('https://fonts.googleapis.com/css?family=Sunflower:300&display=swap&subset=korean');
@import url('https://fonts.googleapis.com/css?family=Jua&display=swap');
#listimg{
  widows: 25px;
  height: 25px;
}
#list{
  float : left;
}
#listdiv{
  height : 12px;
  
}
#title{
  font-family: 'Nanum Gothic', sans-serif;
  width : 1000px;
  height : 80px;
  font-size : 35px;
  border : 1px solid #BDBDBD;
  padding : 20px;
  background-color : white;
  margin-left : 50px;
  margin-top: 10px;
  text-emphasis: emphas;
  
}
#side{
  font-family: 'Nanum Gothic', sans-serif;
  width : 1000px;
   height : 25px;
  font-size : 15px;
  padding : 10px;
  margin-left : 5px;
}
#a{
  font-family: 'Nanum Gothic', sans-serif;
  float : right;
  font-size : 15px;
  margin-right : 20px;
  
}
#category{
  font-size : 25px;
  margin-left: 10px;
  margin-right : 15px;
  color:rgb(42, 114, 156)
}
#content{
   font-family: 'Nanum Gothic', sans-serif;
   height : 30px;
   width : 500px;
  font-size : 23px;
  padding : 10px;
  word-break:keep-all;
}
#detail
{
  font-size : 15px;
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
  #content_table{
    word-break:keep-all;
  }
  #one{
    font-size:23px;
  }
  #q{
    font-size: 15px;
  }
  #youngin{
    border-top: 1px dashed #BDBDBD;
  }
</style>
