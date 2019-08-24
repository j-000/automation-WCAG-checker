<template>
    <div>
        <table class="table">
            <thead>
                <tr>
                    <th>id</th>
                    <th>link</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="report in reports" v-bind:key="report.id">
                    <td>{{ report.id }}</td>
                    <td><router-link to="/reports/report.id">link</router-link></td>
                </tr>
            </tbody>
        </table>
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
            url: url.url,
            reports: []
        }
    },
    methods: {
        fetch(){
            const url = `${this.url}/api/v1/users/${store.getters.getstate.userid}/reports`
            axios.get(url, {
                headers: {'Authorization':`Bearer ${store.getters.getstate.token}`}
            })
            .then(res=>{
                this.report = res.data.reports
            })
            .catch(e=>{
                alert(e);
            })
        }
    }
}
</script>