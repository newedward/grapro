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
import selectstu from './pages/selectstu'
import selectTea from './pages/selectTea'
import mystudents from './pages/mystudents'
import startTea from './pages/startTea'
import startStu from './pages/startStu'
import mediumStu from "./pages/mediumStu";
import endStu from "./pages/endStu";
import mediunTea from "./pages/mediunTea";
import endTea from "./pages/endTea";
import register from "./pages/register";
import login from "./pages/login"
import VueResource from 'vue-resource';

axios.defaults.baseURL = 'http://127.0.0.1:8000'	// 指定后端的地址，也就是django运行的地址
Vue.prototype.$axios = axios	// 添加
axios.defaults.headers.post['Content-Type'] = 'application/json'
Vue.use(ElementUI)	// 添加
Vue.use(VueRouter)
Vue.use(VueResource)
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
    },
    {
      path: '/selectstu',
      name: 'selectstu',
      component: selectstu
    },
    {
      path: '/selectTea',
      name: 'selectTea',
      component: selectTea
    },
    {
      path: '/mystudents',
      name: 'mystudents',
      component: mystudents
    },
    {
      path: '/startTea',
      name: 'startTea',
      component: startTea
    },
    {
      path: '/startStu',
      name: 'startStu',
      component: startStu
    },
    {
      path: '/mediumStu',
      name: 'meidumStu',
      component: mediumStu
    },
    {
      path: '/endStu',
      name: 'endStu',
      component: endStu
    },
    {
      path: '/mediumTea',
      name: 'meidumTea',
      component: mediunTea
    },
    {
      path: '/endTea',
      name: 'endTea',
      component: endTea
    },
    {
      path: '/register',
      name: 'register',
      component: register
    },
    {
      path: '/login',
      name: 'login',
      component: login
    }
  ],
  mode: 'history'
})
new Vue({
  render: h => h(App),
  router,
}).$mount('#app')
