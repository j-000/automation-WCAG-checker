<template>
  <router-link :to="{ name: 'report-details', params: {hashid: report.hashid } }">
    <div id="report-card">
      <div class="card text-left">
        <div class="card-header">Report # {{ report.id }}</div>
        <div class="card-body">
          <h5 class="card-title">Page alias: {{ report.alias }} </h5>
          <p class="card-text mb-0">URL: {{ report.url }}</p>
          <div class="row mt-3 mb-3">
            <div class="col">
              <span class="badge badge-success m-1">{{ report.seo }} SEO</span>
              <span class="badge badge-warning m-1">{{ report.accessibility }} Accessability</span>
              <span class="badge badge-danger m-1">{{ report.usability }} Usability</span>
            </div>
          </div>
          <small class="text-muted">Last checked on {{ report.timestamp }}</small>
        </div>
      </div>
    </div>
  </router-link>
</template>

<script>
export default {
  name: 'ReportCard',
  props: {
    report: {
      type: Object,
      required: true
    }
  }
}
</script>

<style scoped>
  a{
    text-decoration: none!important;
    color: black!important;  
  }
  #report-card:hover{
    box-shadow: 8px 8px 22px -10px rgba(0,0,0,0.75)!important;
  }
</style>>

