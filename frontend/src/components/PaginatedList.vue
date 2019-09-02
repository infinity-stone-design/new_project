<template>
<table>
  <span>체크한 나이2: {{ checkArray }}</span>
  <br/>
  <span> filter: {{ filteredList }}</span>
  <br/>
  <span> filter??: {{ paginatedData[0] }}</span>
  
 <tr v-for="d in paginatedData" :key="d.id">
    <table class = "table">
      <tr>
        <router-link :to="{name: 'detail', params: {id: d.id}}">
        <span>{{d.title}}</span>
        </router-link>
      </tr>
      <tr>
        <span>{{d.subtitle}}</span>
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
    pageCount () { 
      let listLeng = this.listArray.length, 
      listSize = this.pageSize, 
      page = Math.floor(listLeng / listSize); 
  
      if (listLeng % listSize > 0) page += 1; 
      return page; 
    }, 
   filteredList() {
    if(this.checkArray.length===0) return this.listArray;
    var arr=[];
    /*for(let i=0; i<this.checkArray.length; i++)
    {
        arr.push(this.listArray.filter(data => {
        return data.title.toLowerCase().includes(this.checkArray[i].toLowerCase())
      }))
    }*/
    let i=0;
    while(i<this.checkArray.length)
    {
      arr.push(this.listArray.filter(data => {
        return data.title.toLowerCase().includes(this.checkArray[i].toLowerCase())
      }));
      i++
    }
  //  JSON.parse(arr);
    return arr;
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
</style>