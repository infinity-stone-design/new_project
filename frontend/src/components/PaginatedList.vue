<template>

<table>
 <span style="font-size:15pt; color: rgb(50, 99, 145); font-weight:bold;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[전체 {{totalNum}}건]</span><br><br>
 <tr v-for="d in paginatedData" :key="d.id">
    <table class = "table">
      <tr>
        <router-link :to="{name: 'detail', params: {id: d.id}}">
        <span id="tt">[{{d.id}}] {{d.title}}</span>
        </router-link>
      </tr>
      <tr>
        <span id="st">{{d.subtitle}}</span>
      </tr>
    </table>
  </tr>
   <div class="btn-cover">
    <button :disabled="pageNum === 0" @click="prevPage" class="page-btn">이전 </button> 
    <span class="page-count">{{ pageNum + 1 }} / {{ pageCount }} 페이지</span> 
    <button :disabled="pageNum >= pageCount - 1" @click="nextPage" class="page-btn">다음</button> 
  </div> 
  </table>

 
 </template> 

<script> 
export default {
  name: 'paginated-list',
  data () { 
     return { 
       pageNum: 0,
       checkArray: []
     } 
   }, 
  props: {
    message: {
      type: String,
      required : true,
    },
    listArray: {
      type: Array, 
      required: true 
    }, 
    pageSize: { 
      type: Number, 
      required: false, 
      default: 10 
    },
    checkArray: {
      type: Array, 
      required: true 
    }
  }, 
  methods: { 
    nextPage () { 
      this.pageNum += 1; 
    }, 
    prevPage () { 
      this.pageNum -= 1; 
    } 
  }, 
  computed: { 
    totalNum(){
      return this.filteredList.length;
    },
    pageCount () { 
      let listLeng = this.filteredList.length, 
      listSize = this.pageSize, 
      page = Math.floor(listLeng / listSize); 
  
      if (listLeng % listSize > 0) page += 1; 
      return page; 
    },
    addArray(){
      let arr = []
      for(var i = 0; i<this.checkArray.length; i++){
        if(this.checkArray[i] == "영유아"){
          arr.push("유아")
          arr.push("어린이")
          arr.push("유치원")
          arr.push("아이")
          arr.push("아동")
          arr.push("가정")
          arr.push("양육")
        }
        if(this.checkArray[i] == "청소년"){
          arr.push("학생")
          arr.push("가정")
          arr.push("청소년")
          arr.push("학교")
          arr.push("장학")
          arr.push("고시")
        }
        if(this.checkArray[i] == "청년"){
          arr.push("학생")
          arr.push("결혼")
          arr.push("취업")
          arr.push("학교")
          arr.push("장학")
          arr.push("자녀")
          arr.push("고시")
          arr.push("창업")
          arr.push("청년")
        }
        if(this.checkArray[i] == "노인"){
          arr.push("노인")
          arr.push("실버")
          arr.push("유공자")
          arr.push("노후")
          arr.push("연금")
          arr.push("노년")
        }
        if(this.checkArray[i] == "저소득층"){
          arr.push("저소득층")
          arr.push("기초")
        }
        if(this.checkArray[i] == "임산부"){
          arr.push("임산부")
          arr.push("임신")
          arr.push("해산")
          arr.push("출산")
          arr.push("신생아")
          arr.push("산부인과")
          arr.push("아기")
          arr.push("낙태")
        }
        if(this.checkArray[i] == "장애인"){
          arr.push("장애")
        }
        if(this.checkArray[i] == "취업"){
          arr.push("취업")
          arr.push("일자리")
        }
        if(this.checkArray[i] == "금전"){
          arr.push("금전")
          arr.push("만원")
          arr.push("경제")
          arr.push("장학")
        }
        if(this.checkArray[i] == "주거"){
          arr.push("주거")
          arr.push("주택")
          arr.push("집")
        }
        if(this.checkArray[i] == "교육"){
          arr.push("교육")
          arr.push("장학")
          arr.push("프로그램")
          arr.push("학습")
          arr.push("학교")
        }
        if(this.checkArray[i] == "의료"){
          arr.push("의료")
          arr.push("진찰")
          arr.push("보건")
          arr.push("진단")
          arr.push("검사")
        }
        if(this.checkArray[i] == "문화"){
          arr.push("문화")
          arr.push("박물관")
          arr.push("미술")
          arr.push("도서")
          arr.push("음악")
          arr.push("공연")
        }
        else{
          arr.push(this.checkArray[i]);
        }  
      }
      return arr;
    },
    searchFilter(){
      return this.listArray.filter(data => {
        var result = null;
        result += data.title.toLowerCase().includes(this.message.toLowerCase())
        result += data.subtitle.toLowerCase().includes(this.message.toLowerCase())
        result += data.target.toLowerCase().includes(this.message.toLowerCase())
        result += data.contents.toLowerCase().includes(this.message.toLowerCase())
        return result
      })
    },
    filteredList() {
      if(this.addArray.length==0) return this.searchFilter;   
      
      return this.searchFilter.filter(data => {
        var result=null;
        let i=0;
        while(i<this.addArray.length){
          result += data.title.toLowerCase().includes(this.addArray[i].toLowerCase())
          result += data.subtitle.toLowerCase().includes(this.addArray[i].toLowerCase())
          result += data.target.toLowerCase().includes(this.addArray[i].toLowerCase())
          result += data.contents.toLowerCase().includes(this.addArray[i].toLowerCase())
          i++
        }
        return result;
      });
    },
    paginatedData () { 
      const start = this.pageNum * this.pageSize, 
      end = start + this.pageSize; 
      return this.filteredList.slice(start, end); 
    }
  } 
} 
</script> 

<style>
  .btn-cover { 
  margin-top: 1.5rem; 
  margin-bottom: 1.5rem;
  text-align: center; 
  } 
 .btn-cover .page-btn { 
    width: 5rem; 
    height: 2rem; 
    letter-spacing: 0.5px; 
  }   
 .btn-cover .page-count { 
    padding: 0 1rem; 
  } 
  #tt{
    font-size : 20px;
  }
  #st{
    font-size : 15px;
  }
</style>