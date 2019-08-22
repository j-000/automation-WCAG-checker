<template>
    <div>
        <a href="#" @click="fetch">fetch</a>
        <p>{{ report }}</p>
    </div>
</template>

<script>
import axios from 'axios';
import url from '../main';
import store from '../store';

export default {
    name: 'ReportView',
    data(){
        return {
            report: '',
            url: url.url
        }
    },
    methods: {
        fetch(){
            const url = `${this.url}/api/v1/reports/${this.$route.params.reportid}`
            // eslint-disable-next-line
            console.log(store.getters.getstate.loggedId)
            axios.get(url, {
                headers: {'Authorization' : 'Bearer ' + store.getters.getstate.token}
            })
            .then(res=>{
                this.report = res.data
            })
            .catch(e=>{
                alert(e);
            })
        }
    },
    // created(){
    //     this.fetch();
    // }
}
</script>