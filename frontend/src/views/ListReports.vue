<template>
  <div>
      <table class="table">
          <thead>
              <tr>
                  <th>id</th>
                  <th>link</th>
              </tr>
          </thead>
          <tbody>
              <a @click="g">clck</a>
          </tbody>
      </table>
  </div>
</template>

<script>
export default {
  name: 'ReportView',
  methods:{
    g(){
      this.$store.dispatch('getUserReports');
      // eslint-disable-next-line
      console.log(this.$store.state.user.reports);
    }
  }
}
</script>