<template>
  <div class="row">
    <div class="col-6 m-auto text-left">
      <h1>Register</h1>
      
      <b-form @submit.prevent="sendRegistraion">
        <b-form-group>
          <b-form-input
            id="input-1"
            v-model="form.email"
            type="email"
            required
            placeholder="Email"
          ></b-form-input>
        </b-form-group>

        <b-form-group>
          <b-form-input
            id="input-2"
            v-model="form.name"
            required
            placeholder="Name"
          ></b-form-input>
        </b-form-group>

        <b-form-group>
          <b-form-input
            id="input-3"
            v-model="form.password"
            type="password"
            required
          ></b-form-input>
        </b-form-group>

        <b-button type="submit" variant="success">Submit</b-button>
      </b-form>
    </div>    
  </div>
</template>

<script>
import ApiService from '../services/ApiService';
  export default {
    data() {
      return {
        form: {
          email: '',
          name: '',
          password: ''
        },
        success: false,
        response: false
      }
    },
    methods: {
      sendRegistraion() {
        ApiService.registerUser({name:this.form.name, email: this.form.email, password: this.form.password})
          .then(response => {
            this.response = true
            if(response.data.success){
              this.success = true
              this.$router.push('/')
            }
            this.$store.dispatch('alertUser', response.data)
            this.resetForm();
          })
          .catch(e => {
            // eslint-disable-next-line
            console.log(e)
          })
      },
      resetForm(){
        this.form.name = '';
        this.form.email = '';
        this.form.password = '';
      }
    }
  }
</script>