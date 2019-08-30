<template>

<table>
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
       pageNum: 0 
     } 
   }, 
  props: {
    message: {
      type: String,
      required: true
    },
    listArray: {
      type: Array, 
      required: true 
    }, 
    pageSize: { 
      type: Number, 
      required: false, 
      default: 10 
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
      return this.listArray.filter(data => {
        return data.title.toLowerCase().includes(this.message.toLowerCase())
      })
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