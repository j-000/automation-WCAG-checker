<template>
    <div>
        <p>{{ report }}</p>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'ReportView',
    data(){
        return {
            report: ''
        }
    },
    methods: {
        fetch(){
            const url = `http://3.9.176.237/api/v1/reports/${this.$route.params.reportid}`
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