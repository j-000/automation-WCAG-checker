<template>
    <div>
        <p>{{ report }}</p>
    </div>
</template>

<script>
import axios from 'axios';
import url from '../main';

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
            axios.get(url)
            .then(res=>{
                this.report = res.data
            })
            .catch(e=>{
                alert(e);
            })
        }
    },
    created(){
        this.fetch();
    }
}
</script>