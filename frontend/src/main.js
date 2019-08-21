import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'
import router from './router';
import axios from 'axios';

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

Vue.use(BootstrapVue)
Vue.config.productionTip = false


router.beforeEach((to, from, next) => {
  if(to.matched.some(record => record.meta.requiresAuth)){
    const token = localStorage.getItem('token');
    if(token){
      const path = 'http://localhost:5000/api/v1/authenticate';
      axios.get(path, {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      })
      .then(res=>{
        if(res.data.verified){
          next()
        }else{
          next('/')
        }
      })
      .catch(e=>{
        // eslint-disable-next-line
        console.log(e);
        next('/')
      })
    }else{
      next('/')
    }
  }else{
    next()
  }
})


new Vue({
  router,
  render: h => h(App),
}).$mount('#app')


let url = 'http://3.9.176.237';
// let url = 'http://localhost:5000';

export default {
  url
}