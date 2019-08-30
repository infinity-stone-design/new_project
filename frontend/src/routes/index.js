import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/DataIndexPage'
import Detail from '@/components/DataDetail'
Vue.use(Router)

export const router = new Router({
 mode: 'history',
 routes: [
  {
    path: '/',
    name: 'index',
    component: Index
  },
  {
    path: '/:id',
    name: 'detail',
    component: Detail
  }
]
})