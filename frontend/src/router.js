import Vue from 'vue';
import Router from 'vue-router';


import Home from './components/Home.vue';
import Ping from './components/Ping.vue';
import NotFound from './components/NotFound.vue';
import Register from './components/Register.vue';



Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '',
      name: 'Home',
      component: Home
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
    {
      path: '*',
      name: 'NotFound',
      component: NotFound
    }
  ],
});