<template>
  <div :class="alertobject.success ? 'alert alert-success' : 'alert alert-danger'">
    {{ alertobject.message }}
  </div>
</template>

<script>
export default {
  name: 'Alerts',
  props: {
    alertobject: Object
  }
}
</script>

<style>

</style>