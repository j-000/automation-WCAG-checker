<template>
    <div>
        <p>{{ report }}</p>
    </div>
</template>

<script>
import axios from 'axios';
import * as g from '../../vue.config';

export default {
    name: 'ReportView',
    data(){
        return {
            report: ''
        }
    },
    methods: {
        fetch(){
            const url = `${g.api_url}/api/v1/reports/${this.$route.params.reportid}`
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