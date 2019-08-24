<template>
  <div>
    <Report :reportid="reportid" />      
  </div>
</template>

<script>
import Report from '../components/Report';

export default {
  name: 'ReportView',
  components: {
    Report
  },
  data(){
    return {
      reportid: ''
    }
  },
  methods: {
    fetchReportId(){
      this.reportid = this.$route.params.reportid;
    }
  },
  created(){
    this.fetchReportId()
  }
}
</script>