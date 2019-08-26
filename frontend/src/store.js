import Vue from 'vue'
import Vuex from 'vuex'
import ApiService from './services/ApiService'
import router from './router'

Vue.use(Vuex);
const store = new Vuex.Store({
  state:{
    token: null,
    loggedIn: false,
    user: {},
    alerts: [],
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
      state.reports = []
    },
    UPDATE_ALERT(state, newalertobject){
      state.alerts.push(newalertobject)
    },
    REMOVE_ALERT(state, alerttoremove){
      var i = state.alerts.indexOf(alerttoremove)
      state.alerts.splice(i, 1)
    },
    UPDATE_REPORTS(state, newreports){
      state.reports = newreports
    },
    UPDATE_USER(state, newuserobj){
      state.user = newuserobj
    },
    DECREASE_SCAN_QUOTA(state){
      state.user.scan_quota -= 1
    }
  },
  actions:{
    // call mutations, do async stuff, axios calls, etc.

    register_user({dispatch}, payload){
      return ApiService.register_user({name:payload.name, email:payload.email, password:payload.password})
      .then(({data})=>{
        if(data.success){
          dispatch('authenticate', {email:payload.email, password:payload.password})
          router.push('/')
        }else{
          dispatch('alertUser', {message:data.message, success:data.success})
        }
      })
      .catch(e=>{
        dispatch('alertUser', {message:e, success:false})
      })
    },
    doLogout({commit, dispatch, state}){
      ApiService.logout(state.token).then( ({data}) =>{
        commit('LOGOUT')
        localStorage.clear()
        dispatch('alertUser', data)
        router.push('/')
      }).catch(e=>{
        alert(e);
      })
    },
    alertUser({commit}, newalertobject){
      commit('UPDATE_ALERT', newalertobject)
      setTimeout(function(){
        commit('REMOVE_ALERT', newalertobject)
      }, 2500)
    },
    authenticate({commit, dispatch}, payload){
      return ApiService.authenticate(payload.email, payload.password)
      .then(res =>{
        if(res.data.success){
          localStorage.setItem('token', res.data.user.token);
          commit('LOGIN', {token:res.data.user.token, user:res.data.user})
        }
        dispatch('alertUser', res.data)
      })
      .catch(e=>{
        dispatch('alertUser', {message:e, success:false})
      })
    },
    get_user_reports({state, commit, dispatch}){
      return ApiService.get_user_reports(state.user.id, state.token)
      .then(({data})=> {
        if(data.success){
          commit('UPDATE_REPORTS', data.reports)
        }else{
          dispatch('alertUser', data)
        }
      })
      .catch(e=>{
        dispatch('alertUser', {message:e, success:false})
      })
    },
    start_scan({state, commit, dispatch}, payload){
      if(state.user.scan_quota > 0){
        return ApiService.start_scan(state.token, payload)
        .then(({data}) => {
          if(data.success){
            commit('DECREASE_SCAN_QUOTA')
          }
          dispatch('alertUser', data)
          return data
        })
        .catch(e=>{
          dispatch('alertUser', {message:e, success:false})
        })
      }else{
        dispatch('alertUser', {message: 'You have no more scans to use.', success:false})
      }
    },
    update_user({state, commit}){
      return ApiService.update_user(state.token).then(({data})=>{
        commit('UPDATE_USER', data.user)
      })
    }
  },
  getters: {
    getalerts({alerts}){return alerts},
    get_scan_quota(context){return context.user.scan_quota}
  }
})

export default store;