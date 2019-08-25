<template>
  <div class="row">
    <div class="col text-left">
      <h1>Scan a website</h1>
      <b-form >
        <b-form-group id="input-group-1">
          <p>Once your scan finishes, you will receive an email with a unique link to view your report.</p>
          <b-form-input id="input-1" v-model="form.url" type="text" placeholder="URL" required></b-form-input>
        </b-form-group>
        <b-button type="submit" variant="success">Scan</b-button>
      </b-form>
      <br>
      <div :class="message.level" >{{ message.text }}</div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'Tester',
  data(){
    return {
      form:{
        url:''
      }, 
      message: {}
    }
  },
  methods:{
  
  }
}
</script>
