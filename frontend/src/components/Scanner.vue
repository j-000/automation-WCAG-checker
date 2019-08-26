<template>
  <div class="row">
    <div class="col text-left">
      <h1>Scan a website</h1>
      <b-form v-if="scan_quota > 29" @submit.prevent="start_scan">
        <b-form-group>
          <p>Once your scan finishes, you will receive an email with a unique link to view your report.</p>
          <b-form-input class="mb-2" v-model="form.url" type="text" placeholder="URL"></b-form-input>
          <b-form-input v-model="form.alias" type="text" placeholder="Alias"></b-form-input>
        </b-form-group>
        <b-button type="submit" variant="success">Scan</b-button>
      </b-form>
      <div v-else>
        <p>Oh no! You have used all your scans. Your allowance will reset in 5 days.</p>
        <p>You can purchase 3 new extra scans for £0.99.</p>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: 'Tester',
  data(){
    return {
      form:{
        url:'',
        alias: ''
      }
    }
  },
  methods:{
    start_scan(){
      this.$store.dispatch('start_scan', this.form).then((data)=>{
        if(data.success){
          this.clear_form()
        }
      })
    },
    clear_form(){
      this.form = {url:'',alias:''}
    }
  },
  computed:mapState({
    scan_quota: (state) => state.user.scan_quota
  })
  
}
</script>
