<template>
<p>
  {{ reportid }}
</p>
</template>

<script>
export default {
  name: 'Report',
  props: ['reportid'],
  data(){
    return{

    }
  },
  methods:{

  },
  created(){
    //  call api service with reportid
  }
}
</script>

<style>

</style>