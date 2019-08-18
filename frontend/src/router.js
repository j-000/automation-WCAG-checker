import Vue from 'vue';
import Router from 'vue-router';



import RunScan from './views/RunScan';
import NotFound from './views/NotFound';
import Home from './views/Home';
import ReportView from './views/ReportView';


Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name:'Home',
      component: Home
    },
    {
      path: '/scan',
      name: 'RunScan',
      component: RunScan
    },
    {
      path: '/reports/:reportid',
      name: 'Report',
      component: ReportView
    },
    {
      path: '/*',
      name: 'NotFound',
      component: NotFound
    }
  ],
});