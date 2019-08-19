<template>
  <div class="row">
    <div class="col-6 m-auto text-left">
      <h1>Register</h1>
      <div class="alert" v-if="response" v-bind:class="{ 'alert-success': success, 'alert-danger': error  }">
        <p>{{ response }}</p>
      </div>
      <b-form @submit="onSubmit" v-if="show">
        <b-form-group
          id="input-group-1"
          label="Email address"
          label-for="input-1"
          description="We'll never share your email with anyone else."
        >
          <b-form-input
            id="input-1"
            v-model="form.email"
            type="email"
            required
            placeholder="Enter email"
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-2" label="Your name" label-for="input-2">
          <b-form-input
            id="input-2"
            v-model="form.name"
            required
            placeholder="Enter name"
          ></b-form-input>
        </b-form-group>

        <b-button type="submit" variant="success">Submit</b-button>
      </b-form>
    </div>    
  </div>
</template>

<script>
  import axios from 'axios';
  import url from '../main';

  export default {
    data() {
      return {
        form: {
          email: '',
          name: ''
        },
        show: true,
        response: false,
        success: false,
        error: false
      }
    },
    methods: {
      onSubmit(evt) {
        evt.preventDefault()
        const data = this.form;
        const path = `${url.url}/api/register`;
        
        axios.post(path, {
          name: data.name,
          email: data.email
        })
        .then((res) => {
          this.response = res.data;
          this.error = true;
          if(this.response.success){
            this.success = true;
            this.resetForm();
          }
        })
        .catch((e) => {
          this.error = true;
          alert(e);
        });
      },
      resetForm(){
        this.form.name = '';
        this.form.email = '';
      }
    }
  }
</script>