<script setup lang="ts">
import axios from 'axios';
import { onMounted, reactive, ref, watch } from 'vue';
import { onBeforeRouteUpdate, useRoute } from 'vue-router';

const route = useRoute()
let index = Number(route.params.index)
let settitle = ref()
let posttime = ref()
let setcontent = ref()
let base_url = "http://127.0.0.1:8000/api/blogs";
const state = reactive({
    blogs_list: [],
})
const getblogs = () => {
    axios.get(base_url).then(res => {
        state.blogs_list = res.data;
        setcontent.value = state.blogs_list[index]['content']
        settitle.value = state.blogs_list[index]['title']
        posttime.value = state.blogs_list[index]['post_time']
        console.log(state.blogs_list)
    }).catch(err => {
        console.log(err)
    })
}
onBeforeRouteUpdate((to:any)=>{
  index = Number(to.params.index)
  setcontent.value = state.blogs_list[index]['content']
        settitle.value = state.blogs_list[index]['title']
        posttime.value = state.blogs_list[index]['post_time']
})
onMounted(() => {
    getblogs();
})
</script>
    
<template>
    <el-container>
        <el-header>
            <div style="position:absolute; top: 50%;">
                <h1>{{settitle}}</h1>
            </div>
        </el-header>
        <el-divider />
        <el-main>
            <pre>{{setcontent}}</pre>
        </el-main>
        <el-divider />
        <el-footer>{{'DATE: '+posttime}}</el-footer>
    </el-container>
</template>