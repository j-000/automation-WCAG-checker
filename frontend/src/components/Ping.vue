<template>
    <div>
        <h1>Ping route component</h1>
        <p>{{ data }}</p>
    </div>
</template>


<script>
import axios from 'axios';

export default {
    data(){
        return {
            data: ''
        };
    },
    methods: {
        getData(){
            const BASE_URL = 'http://localhost:5000/api';
            const path =  `${BASE_URL}/ping`;
            axios.get(path)
            .then((res) => {
                this.data = res.data;
            })
            .catch((error) => {
                alert(error);
            });
        }
    },
    created() {
        this.getData();
    }
};
</script>

