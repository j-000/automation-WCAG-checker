<template>
  <div class="card-columns">
    <ReportCard v-for="report in reports" :key="report.id" :report="report"/>
  </div>
</template>

<script>
import ReportCard from '../components/ReportCard'
import { mapState } from 'vuex';
export default {
  name: 'ReportView',
  components:{
    ReportCard
  },
  computed: mapState({
    reports: ({reports}) => reports
  }),
  created(){
    this.$store.dispatch('get_user_reports')
  }
}
</script>