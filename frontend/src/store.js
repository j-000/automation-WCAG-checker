import Vue from 'vue';
import Vuex from 'vuex';
import router from './router';

Vue.use(Vuex);
const store = new Vuex.Store({
    state:{
        token: null,
        loggedIn: false,
        auth_header: null
    },
    mutations:{
        login(state, token){
            state.token = token
            state.loggedIn = true
            state.auth_header = {'Authorization': `Bearer ${token}`}
        },
        logout(state){
            state.token = null
            state.loggedIn = false
            localStorage.removeItem('token');
            router.push('/')
        }
    },
    getters: {
        getstate(state){
            return state;
        }
    }
})

export default store;