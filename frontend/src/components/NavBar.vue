<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand href="/">CompHero</b-navbar-brand>
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
          <li v-else class="nav-item">
            <router-link class="nav-link" :to="{ name: 'register'}">Register</router-link>
          </li>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: 'NavBar',
  computed: {  
    isloggedin () {
      return this.$store.getters.getstate.loggedIn;
    }
  },
  methods:{
    logout(){
      this.$store.dispatch('doLogout');
    }
  }
}
</script>