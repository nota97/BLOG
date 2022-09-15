<template>
    <div class="form">
        <el-form :model="form" label-width="120px">
            <el-form-item label="blog title">
                <el-input v-model="form.title" />
            </el-form-item>
            <el-form-item label="blog content">
                <el-input v-model="form.content" type="textarea" autosize />
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="onSubmit">Submit</el-button>
                <el-button>Cancel</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>
  
  <style>
  .form {
      padding: 20px;
      width: 30%;
      position: relative;
  }
  </style>
<script lang="ts" setup>
import axios from 'axios'
import { reactive } from 'vue'
import router from '@/router'
import { useRoute } from 'vue-router'

// do not use same name with ref
const route = useRoute()
let editdata = route.query
const form = reactive({
    title: editdata['title'],
    content: editdata['content'],
})

const putblogs = () => {
    let edit_url : any = editdata['url']
    let add_data = JSON.stringify(form)
    let ltoken = localStorage.getItem("loginToken")
    let n_url = edit_url +"?token=" +ltoken
    axios.put(n_url, add_data, { headers: { "content-type": "application/json" } }).then(() => {
        window.location.href = '/bloglist';
    }).catch(err => {
        console.log(err)
    })
}
const onSubmit = () => {
    console.log(form)
    console.log(editdata)
    putblogs()
}
</script>