<template>
  <div class="row">
    <div class="col-6 m-auto text-left">
      <h1>Register</h1>
      
      <b-form @submit.prevent="register">
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
  export default {
    data() {
      return {
        form: {
          email: '',
          name: '',
          password: ''
        }
      }
    },
    methods: {
      register(){
        this.$store.dispatch('register_user', this.form)
        .then(()=>{
          this.$router.push('/')
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