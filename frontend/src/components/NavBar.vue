<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand href="/">CompHero</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <li class="nav-item">
            <router-link class="nav-link" to="/">Home</router-link>
          </li>
          <li v-if="isloggedin" class="nav-item">
            <router-link class="nav-link" to="/scan">Scan URL</router-link>
          </li>
          <li v-if="isloggedin" class="nav-item">
            <router-link class="nav-link" to="/reports/1">My Reports</router-link>
          </li>
          <li v-if="isloggedin" class="nav-item">
            <router-link class="nav-link" to="#">
              <a @click="logout">Logout</a>
            </router-link>
          </li>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
/* eslint-disable */ 
import store from '../store';

export default {
  name: 'NavBar',
  computed: {
  isloggedin () {
    return store.getters.getstate.loggedIn;
    }
  },
  methods:{
    logout(){
      store.commit('logout');
    }
  }
}
</script>