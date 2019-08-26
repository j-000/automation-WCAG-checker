import Vue from 'vue';
import Router from 'vue-router';

import RunScan from './views/RunScan';
import NotFound from './views/NotFound';
import Home from './views/Home';
import ReportView from './views/ReportView';
import ListReports from './views/ListReports';
import Registration from './views/Registration';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name:'home',
      component: Home
    },
    {
      path: '/register',
      name:'register',
      component: Registration
    },
    {
      path: '/scan',
      name: 'scan',
      component: RunScan,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/reports/:hashid',
      name: 'report-details',
      component: ReportView,
      props:true,
      meta: {
        requiresAuth: true
      }
    }, {
      path: '/reports',
      name: 'reports',
      component: ListReports,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/logout',
      name: 'logout',
      component: Home,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '*',
      name: 'not-found',
      component: NotFound
    }
  ],
});