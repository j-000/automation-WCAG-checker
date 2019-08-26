<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand href="/">CompHero <span v-if="haspremium" class="badge badge-warning">Premium</span></b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'home'}">Home</router-link>
          </li>
          <li v-if="isloggedin" class="nav-item">
            <router-link class="nav-link" :to="{ name: 'scan'}">Scan URL</router-link>
          </li>
          <li v-if="isloggedin" class="nav-item">
            <router-link class="nav-link" :to="{ name: 'reports'}">My Reports</router-link>
          </li>
          <li v-if="isloggedin" class="nav-item">
            <a class="nav-link" @click="logout">Logout</a>              
          </li>
          <li v-if="isloggedin" class="nav-item">
            <a class="nav-link">Support</a>              
          </li>
          <li v-else class="nav-item">
            <router-link class="nav-link" :to="{ name: 'register'}">Register</router-link>
          </li>
          <li v-if="isadmin" class="nav-item">
            <a class="nav-link" @click="logout">Admin</a>              
          </li>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
import { mapState } from 'vuex';
export default {
  name: 'NavBar',
  computed:mapState({
    isloggedin: state => state.loggedIn,
    isadmin: ({user}) => user.admin,
    haspremium: ({user}) => user.has_premium
  }),
  methods:{
    logout(){
      this.$store.dispatch('doLogout');
    }
  }
}
</script>