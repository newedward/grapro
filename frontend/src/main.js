// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import ElementUI from 'element-ui'	// 添加
import 'element-ui/lib/theme-chalk/index.css'	// 添加
import axios from 'axios'	// 添加
import home from './pages/home.vue'
import process from './pages/process.vue'
import personinfo from './pages/personinfo'

axios.defaults.baseURL = 'http://127.0.0.1:8000'	// 指定后端的地址，也就是django运行的地址
Vue.prototype.$http = axios	// 添加
axios.defaults.headers.post['Content-Type'] = 'application/json'
Vue.use(ElementUI)	// 添加
Vue.use(VueRouter)
Vue.config.productionTip = false
const router = new VueRouter({
  routes: [
    {
      path: '/home',
      name: 'home',
      component: home
    },
    {
      path: '/process',
      name: 'process',
      component: process
    },
    {
      path: '/personinfo',
      name: 'personinfo',
      component: personinfo
    }
  ],
  mode: 'history'
})
new Vue({
  render: h => h(App),
  router,
}).$mount('#app')
