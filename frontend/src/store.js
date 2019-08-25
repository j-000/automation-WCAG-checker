import Vue from 'vue';
import Vuex from 'vuex';
import router from './router';
import ApiService from './services/ApiService';

Vue.use(Vuex);
const store = new Vuex.Store({
  state:{
    token: null,
    loggedIn: false,
    user: {},
    alert: [],
    reports: []
  },
  mutations:{
    // should only change state. Nothing else.
    LOGIN(state, payload){
      state.token = payload.token
      state.user = payload.user
      state.loggedIn = true
    },
    LOGOUT(state){
      state.token = null
      state.loggedIn = false
      state.user = {}
    },
    UPDATE_ALERT(state, newalertobject){
      state.alert.push(newalertobject)
    },
    REMOVE_ALERT(state, alerttoremove){
      var i = state.alert.indexOf(alerttoremove)
      state.alert.splice(i, 1)
    },
    UPDATE_REPORTS(state, newreports){
      state.user.reports = newreports
    }
  },
  actions:{
    // call mutations, do async stuff, axios calls, etc.
    register_user({dispatch}, payload){
      return ApiService.register_user({name:payload.name, email:payload.email, password:payload.password})
      .then(({data})=>{
        if(data.success){
          dispatch('authenticate', payload)
        }
        dispatch('alertUser', data)
      }).catch(e=>{
        alert(e);
      })
    },
    doLogout({commit, dispatch, state}){
      ApiService.logout(state.token).then( ({data}) =>{
        commit('LOGOUT')
        localStorage.clear()
        dispatch('alertUser', data)
      }).catch(e=>{
        alert(e);
      })
    },
    alertUser({commit}, newalertobject){
      commit('UPDATE_ALERT', newalertobject)
      setTimeout(function(){
        commit('REMOVE_ALERT', newalertobject)
      }, 1500)
    },
    authenticate(context, payload){
      return ApiService.authenticate(payload.email, payload.password)
      .then(res =>{
        if(res.data.success){
          localStorage.setItem('token', res.data.token);
          context.commit('LOGIN', {token:res.data.token, user:res.data.user})
        }
        context.dispatch('alertUser', res.data)
      })
      .catch(e=>{
        alert(e);
      })
    },
    getUserReports(context){
      return ApiService.getUserReports(context.state.user, context.state.token)
      .then(res => {
        context.commit('UPDATE_REPORTS', res.data.reports)
      })
      .catch(e=>{
        alert(e);
      })
    }
  },
  getters: {
    getstate(state){
      return state;
    },
    getuserreports(state){
      return state.user.reports
    }
  }
})

export default store;