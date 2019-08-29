import Vue from 'vue'
import App from './App.vue'
import {router}  from './routes/index.js'
import axios from 'axios'
import { PaginationControl, PaginationPage } from 'vue-smart-pagination'

Vue.component('PaginationControl', PaginationControl)
Vue.component('PaginationPage', PaginationPage)

Vue.config.productionTip = false

Vue.prototype.$http = axios;
new Vue({
  render: h => h(App),
  router,
}).$mount('#app')
