<template>
  <div class="row">
    <div class="col text-left">
      <h1>Scan a website</h1>
      <b-form @submit="runTester">
        <b-form-group id="input-group-1">
          <p>Once your scan finishes, you will receive an email with a unique link to view your report.</p>
          <b-form-input id="input-1" v-model="form.url" type="text" placeholder="URL" required></b-form-input>
          <br>
          <b-form-input id="input-2" v-model="form.email" type="text" placeholder="Email"></b-form-input>
        </b-form-group>
        <b-button type="submit" variant="success">Scan</b-button>
      </b-form>
      <br>
      <div :class="message.level" >{{ message.text }}</div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import url from '../main';

export default {
  name: 'Tester',
  data(){
    return {
      form:{
        url:'',
        email: ''
      }, 
      message: {}
    }
  },
  methods:{
    runTester(evt){
      const path = `${url.url}/api/v1/scans`;
      evt.preventDefault();
      axios.post(path, {
        url: this.form.url,
        email: this.form.email
      })
      .then((res) => {
        this.message = {level:res.data.level, text:res.data.message}
        setTimeout(() => {
          this.message = {}
        }, 1000)
      })
      .catch((e) => {
        alert(e);
      })
    }
  }
}
</script>
