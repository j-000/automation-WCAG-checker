import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'
import router from './router';
import VueCookies from 'vue-cookies';
import ApiService from './services/ApiService';

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import store from './store';

Vue.use(VueCookies)
Vue.use(BootstrapVue)
Vue.config.productionTip = false

router.beforeEach((to, from, next) => {
  if(to.matched.some(record => record.meta.requiresAuth)){
    const token = localStorage.getItem('token');
    if(token){
      ApiService.verify(token)
        .then(res=>{
          if(res.data.verified){
            store.dispatch('doLogin');
            next()
          }else{
            store.dispatch('doLogout');
            next('/')
          }
        })
        .catch(e=>{
          // eslint-disable-next-line
          console.log(e);
          store.dispatch('doLogout');
          next('/')
        })
    }else{
      store.dispatch('doLogout');
      next('/')
    }
  }else{
    next()
  }
})

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')


export default {
}