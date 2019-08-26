<template>
  <div>
    <!-- Profile -->
    <div class="row" v-if="isloggedin">
      <div class="col text-left">
        <h1>Hi, {{ user.name }}</h1>
        <p>{{ user.email }}</p>
        <p>
          <span class="badge badge-success" v-if="user.admin">Admin user</span>
          <span v-else class="badge badge-info">Standard user</span>
        </p>
        <p>You have <strong> {{ user.scan_quota }} </strong> more scans to use until the end of the month.</p>
        <hr>
        <div v-if="!haspremium" class="text-center ">
          <h2 class="border border-warning p-2">Get more with <span class="badge badge-warning">Premium</span></h2>
          <div class="row mt-4">
            <div class="col m-3">
              <div class="m-auto card text-black" style="width: 18rem; ">
                <h2 class="card-header bg-warning">Checkpoints</h2>
                <div class="card-body">
                  <h5 class="card-title">Custom Checkpoint</h5>
                  <p class="card-text">Meet your own company's standards and guidelines.</p>
                </div>
              </div>
            </div>
            <div class="col m-3">
              <div class="m-auto card text-black" style="width: 18rem;">
                <h2 class="card-header bg-warning">Scans</h2>
                <div class="card-body">
                  <h5 class="card-title">Unlimited</h5>
                  <p class="card-text">That's right, you can run as many scans as your company needs.</p>
                </div>
              </div>
            </div>
            <div class="col m-3">
              <div class="m-auto card text-black" style="width: 18rem;">
                <h2 class="card-header bg-warning">Support</h2>
                <div class="card-body">
                  <h5 class="card-title">Dedicated Support</h5>
                  <p class="card-text">We have humans working 24/7 ready to help you.</p>
                </div>
              </div>
            </div>
          </div>
          <br>
          <h3>£ 50 per month</h3>
          <a href="#" class="btn btn-warning">Get Premium!</a>
        </div>
      </div>
    </div>
    <!-- Login -->
    <div v-else class="row">
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
    isloggedin: state => state.loggedIn ,
    haspremium: state => state.user.has_premium
  }),
  methods:{
    doLogin(){
      this.$store.dispatch('authenticate', {email: this.email, password: this.password})
    }
  },
  created(){
    if(this.$store.state.loggedIn){
      this.$store.dispatch('update_user')
    }
  }
}
</script>
