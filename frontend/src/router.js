import Vue from 'vue';
import Router from 'vue-router';


import Home from './components/Home.vue';
import Checkpoints from './components/Checkpoints.vue';
import NotFound from './components/NotFound.vue';
import Register from './components/Register.vue';
import Tester from './components/Tester.vue';



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
      path: '/checkpoints',
      name: 'Checkpoints',
      component: Checkpoints,
    },
    {
      path: '/scan-url',
      name: 'Tester',
      component: Tester,
    },
    {
      path: '*',
      name: 'NotFound',
      component: NotFound
    }
  ],
});