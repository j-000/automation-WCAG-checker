<template>
  <div>
    <h1>Home</h1>
    <form action="/authenticate" @submit="doLogin">
      <input v-model="email" type="text" placeholder="Email"><br>
      <input v-model="password" type="password" name="password" id="password"><br>
      <input type="submit" value="Login">
    </form>
    <p>{{ loginmessage }}</p>
  </div>
</template>

<script>
import axios from 'axios';
import store from '../store';

export default {
  name: 'Home',
  data(){
    return {
      email: '',
      password:'',
      loginmessage: '',
    }
  },
  methods:{
    doLogin(e){
      e.preventDefault();
      const path = 'http://localhost:5000/api/v1/authenticate';
      axios.post(path, {
        email: this.email,
        password: this.password
      })
      .then(res =>{
        if(res.data.success){
          localStorage.setItem('token', res.data.token);
          store.commit('login');
          this.$router.push('/scan');
        }
        this.loginmessage = res.data.message;
      })
      .catch(e=>{
        alert(e);
      })
    }
  }
}
</script>
