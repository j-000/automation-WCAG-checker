<template>
  <div>
    <h1>Checkpoints</h1>
    <table class="table">
      <thead>
        <tr>
          <th>Id</th>
          <th>Name</th>
          <th>WCAG Levels</th>
          <th>Benefits</th>
          <th>Regex</th>
        </tr> 
      </thead>
      <tbody>
        <tr 
        v-for="checkpoint in checkpoints"
        v-bind:key="checkpoint.id"
        >
          <td>{{ checkpoint.id }}</td>
          <td>{{ checkpoint.name }}</td>
          <td>{{ checkpoint.wcaglevels }}</td>
          <td>{{ checkpoint.benefits }}</td>
          <td>{{ checkpoint.regex }}</td>
        </tr>
      </tbody>
    </table>
    <hr>
    <div class="addForm">
      <b-form @submit="addCheckpoint">
        <b-form-group id="input-group-1" label="Id:" label-for="input-1">
          <b-form-input
          id="input-1"
          v-model="form.id"
          type="number"
          required
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-2" label="Checkpoint Name:" label-for="input-2">
          <b-form-input
          id="input-2"
          v-model="form.name"
          required
          placeholder="Checkpoint name"
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-3" label="WCAG Levels:" label-for="input-3">
          <b-form-input
          id="input-3"
          v-model="form.wcaglevels"
          required
          placeholder="A, AA, AAA"
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-4" label="Benefits:" label-for="input-4">
          <b-form-input
          id="input-4"
          v-model="form.benefits"
          required
          placeholder="Accessibility, SEO, Usability"
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-5" label="Regex:" label-for="input-5" description="Please escape the backslahsh with another backslash.">
          <b-form-input
          id="input-5"
          v-model="form.regex"
          required
          placeholder="(?si)\\b"
          ></b-form-input>
        </b-form-group>

        <b-button type="submit" variant="primary">Add</b-button>
      </b-form>
    </div>
    <div class="alert" v-bind:class="{ 'alert-success': success, 'alert-danger': error  }">
      <p>{{ add_form_message }}</p>
    </div>
  </div>
</template>


<script>
import axios from 'axios';

export default {
    data(){
        return {
          success: '',
          error: '',
          add_form_message: '',
          form:{
            id:'',
            name:'',
            wcaglevels:'',
            benefits:'',
            regex:''
          },
          checkpoints: []
        };
    },
    methods: {
        getCheckpoints(){
            const BASE_URL = 'http://localhost:5000/api';
            const path =  `${BASE_URL}/checkpoints`;
            axios.get(path)
            .then((res) => {
                this.checkpoints = res.data.checkpoints;
            })
            .catch((error) => {
                alert(error);
            });
        },
        resetForm(){
          this.form.id = '',
          this.form.name = '',
          this.form.wcaglevels = '',
          this.form.benefits = '',
          this.form.regex = ''
        },
        addCheckpoint(evt){
          evt.preventDefault();
          const path = 'http://localhost:5000/api/checkpoints';
          axios.post(path, {
            id: this.form.id,
            name: this.form.name,
            wcaglevels: this.form.wcaglevels, 
            benefits: this.form.benefits, 
            regex: this.form.regex
          })
          .then((res) => {
            if(res.data.success){
              this.resetForm();
              this.success = true;
              this.error = false;
              this.add_form_message = res.data.message;
              this.checkpoints.push(res.data.checkpoint);
            }else{
              this.success = false;
              this.error = true;
              this.add_form_message = res.data.error;

            }
          })
          .catch((e) => {
            alert(e);
          });
        }
    },
    created() {
        this.getCheckpoints();
    }
};
</script>

