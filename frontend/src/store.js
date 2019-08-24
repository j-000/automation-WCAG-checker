import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);
const store = new Vuex.Store({
  state:{
    token: null,
    loggedIn: false,
    user: {},
    alert: false
  },
  mutations:{
    LOGIN(state){
      state.token = localStorage.getItem('token')
      state.user = JSON.parse(localStorage.getItem('user'))
      state.loggedIn = true
    },
    LOGOUT(state){
      state.token = null
      state.loggedIn = false
      localStorage.clear();
    },
    UPDATE_ALERT(state, newalert){
      state.alert = newalert
    },
    UPDATE_TOTAL_REPORTS(state, newcount){
      state.user.totalreports = newcount
    }
  },
  actions:{
    doLogin({commit}){
      commit('LOGIN')
    },
    doLogout({commit}){
      commit('LOGOUT')
    },
    alertUser({commit}, newalert){
      commit('UPDATE_ALERT', newalert)
      setTimeout(function(){
        commit('UPDATE_ALERT', false)
      }, 1500)
    }
  },
  getters: {
    getstate(state){
      return state;
    }
  }
})

export default store;