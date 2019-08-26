<template>
  <div class="text-left">
    <h1>Results for {{ report.alias ? report.alias : `Report # ${report.id}`}}</h1>
    <p><a :href="report.url" target="_blank" title="Opens a new window">Link</a></p>
    <p>
      <span class="badge badge-success m-1">{{ report.seo }} SEO</span>
      <span class="badge badge-warning m-1">{{ report.accessibility }} Accessability</span>
      <span class="badge badge-danger m-1">{{ report.usability }} Usability</span>
    </p>
    <small>Reported on {{ report.timestamp }}</small>
    <hr>
    <h2>Issue</h2>
    <h3>SEO</h3>

    <h3>Usability</h3>
    <h3>Accessability</h3>
  </div>
</template>

<script>
export default {
  name: 'ReportView',
  computed: {
    report(){
      return this.$store.state.reports.filter(report => report.hashid == this.$route.params.hashid)[0]
    }
  }
}
</script>