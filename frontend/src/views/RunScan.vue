<template>
  <div>
    <Scanner />
    <hr>
    <h2 class="text-left">Standard Checkpoints</h2>
    <p class="text-left">These checkpoints are included in all scans.</p>
    <div class="list-group">
      <div v-for="checkpoint in checkpoints" :key="checkpoint.id"  href="#" class="list-group-item text-left mb-2">
        <div class="">
          <h5 class="mb-1">{{ checkpoint.name }}</h5>
          <a href="#" target="_blank" class="font-italic">WCAG Source</a>
          <p class="mb-0"><strong>Benefits</strong> {{ checkpoint.benefits }} </p>
          <p class="mb-0"><strong>WCAG Levels</strong> {{ checkpoint.wcaglevels }}</p>
        </div>
      </div>
    </div>
    <hr>
    <h2 class="text-left">Custom Checkpoints</h2>
    <p class="text-left">With custom made checkpoints, you can ensure your pages meet your company's guidelines and standards.</p>
    <a v-if="!haspremium" href="#" class="btn btn-warning">Get Premium!</a>
  </div>
</template>

<script>
import Scanner from '../components/Scanner';
import { mapState } from 'vuex';
export default {
  name: 'RunScan',
  components: {
    Scanner
  },
  computed: mapState({
    haspremium: state => state.user.has_premium,
    checkpoints: state => state.standard_checkpoints
  }),
  created(){
    this.$store.dispatch('get_standard_checkpoints')
  }
}
</script>
