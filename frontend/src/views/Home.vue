<template>
  <div>
    <!-- Profile -->
    <div class="row" v-if="isloggedin">
      <div class="col">
        <h1>Hi, {{ user.name }}.</h1>
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
import ApiService from '../services/ApiService';
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
      ApiService.authenticate(this.email,this.password)
      .then(res =>{
        if(res.data.success){
          localStorage.setItem('token', res.data.token);
          localStorage.setItem('user', JSON.stringify(res.data.user));
          this.$store.dispatch('doLogin');
        }
        this.$store.dispatch('alertUser', res.data)
      })
      .catch(e=>{
        alert(e);
      })
    }
  }
}
</script>
