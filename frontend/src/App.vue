<template>
  <div id="app">
    <NavBar />
    <div class="m-5">
      <Alerts v-for="alert in getalerts" :key="alert.message"  :alertobject="alert"/>
      <router-view/>
    </div>
  </div>
</template>

<script>

import NavBar from './components/NavBar';
import Alerts from './components/Alerts';
import { mapGetters } from 'vuex';

export default {
  name: 'app',
  components: {
    NavBar,
    Alerts
  },
  computed:mapGetters(['getalerts'])
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
