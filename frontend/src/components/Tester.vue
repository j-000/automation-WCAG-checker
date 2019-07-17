<template>
  <div class="row">
    <div class="col text-left">
      <h1>Scan a website</h1>
      <b-form @submit="runTester">
        <b-form-group id="input-group-1" label="URL" label-for="input-1">
          <p>Only one page is scanned. To scan multiple pages, you need to run the scan for each page individually.</p>
          <b-form-input
          id="input-1"
          v-model="form.url"
          type="text"
          required
          ></b-form-input>
        </b-form-group>
        <b-button type="submit" variant="success">Scan</b-button>
      </b-form>
      <br>
      <div class="alert-danger alert" v-if="error">
        {{ error }}
      </div>
    </div>
    <div class="col text-left">
      <h1>Results table</h1>
      <div class="result">
        <table class="table">
          <thead>
            <tr>
              <th>Checkpoint</th>
              <th>Result</th>
              <th>More info</th>
            </tr>
          </thead>
          <tbody>
            <tr 
            v-for="result in results"
            v-bind:key="result.id"
            >
              <td>{{ result.id }} - {{ result.info.name }}</td>
              <td>
                <span class="badge" 
                v-bind:class="{'badge-success': result.info.result == 'passed', 'badge-danger': result.info.result == 'failed'}">
                {{ result.info.result }}
                </span>
              </td>
              <td></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  
  data(){
    return {
      form:{
        url:''
      }, 
      results: [],
      error: false
    }
  },
  methods:{
    runTester(evt){
      const path = 'http://localhost:5000/api/scan';
      evt.preventDefault();
      axios.post(path, {
        url: this.form.url
      })
      .then((res) => {
        this.results = res.data.results;
        this.error = res.data.error;
      })
      .catch((e) => {
        alert(e);
      })
    }
  }
}
</script>
