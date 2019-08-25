<template>
  <div>
    <!-- Profile -->
    <div class="row" v-if="isloggedin">
      <div class="col text-left">
        <h1>Hi, {{ user.name }}</h1>
        <p><span class="badge badge-success" v-if="user.admin">Admin user</span><span v-else class="badge badge-info">Standard user</span></p>
      </div>
    </div>

    <!-- Login -->
    <div v-if="!isloggedin" class="row">
      <div class="col-6 m-auto text-left">
        <h1>Login</h1>
        <form  action="/authenticate" @submit.prevent="doLogin">
          <input v-model="email" class="form-control" type="text" placeholder="Email"><br>
          <input v-model="password" type="password" class="form-control" name="password" id="password"><br>
          <input type="submit" value="Login" class="btn btn-success">
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name:'Home',
  data(){
    return {
      email: '',
      password:''
    }
  },
  computed: mapState({
    user: state => state.user,
    isloggedin: state => state.loggedIn 
  }),
  methods:{
    doLogin(){
      this.$store.dispatch('authenticate', {email: this.email, password: this.password})
    }
  }
}
</script>
