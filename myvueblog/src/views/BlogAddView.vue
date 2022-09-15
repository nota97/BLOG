<template>
    <div class="con">
        <div class="form">
            <h1> ADD A BLOG</h1>
            <span>I sit at my window this morning where the world like a passer-by stops
            for a moment, nods to me and goes.</span>
            <el-divider />
            <el-form :model="form" label-width="120px">
                <el-form-item label="blog title">
                    <el-input v-model="form.title" />
                </el-form-item>
                <!-- <el-form-item label="Activity zone">
        <el-select v-model="form.region" placeholder="please select your zone">
          <el-option label="Zone one" value="shanghai" />
          <el-option label="Zone two" value="beijing" />
        </el-select>
      </el-form-item>
      <el-form-item label="Activity time">
        <el-col :span="11">
          <el-date-picker
            v-model="form.date1"
            type="date"
            placeholder="Pick a date"
            style="width: 100%"
          />
        </el-col>
        <el-col :span="2" class="text-center">
          <span class="text-gray-500">-</span>
        </el-col>
        <el-col :span="11">
          <el-time-picker
            v-model="form.date2"
            placeholder="Pick a time"
            style="width: 100%"
          />
        </el-col>
      </el-form-item>
      <el-form-item label="Instant delivery">
        <el-switch v-model="form.delivery" />
      </el-form-item>
      <el-form-item label="Activity type">
        <el-checkbox-group v-model="form.type">
          <el-checkbox label="Online activities" name="type" />
          <el-checkbox label="Promotion activities" name="type" />
          <el-checkbox label="Offline activities" name="type" />
          <el-checkbox label="Simple brand exposure" name="type" />
        </el-checkbox-group>
      </el-form-item>
      <el-form-item label="Resources">
        <el-radio-group v-model="form.resource">
          <el-radio label="Sponsor" />
          <el-radio label="Venue" />
        </el-radio-group>
      </el-form-item> -->
                <el-form-item label="blog content">
                    <el-input v-model="form.content" type="textarea" rows="10" />
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="onSubmit">Submit</el-button>
                    <el-button>Cancel</el-button>
                </el-form-item>
            </el-form>
        </div>
    </div>
</template>
  
  <style>
  .con {
      position: relative;
      height: 80%;
      width: 100%;
  }
  
  .form {
      padding: 20px;
      width: 30%;
      left: 30%;
      top: 10%;
      position: absolute;
  }

  </style>
  
  <script lang="ts" setup>
import axios from 'axios'
import { reactive } from 'vue'

// do not use same name with ref
const form = reactive({
    title: '',
    content: '',
})
let base_url = "http://127.0.0.1:8000/api/blogs/";
let ltoken = localStorage.getItem("loginToken")
let n_url = base_url +"?token=" +ltoken
console.log(n_url)
const addblogs = () => {
    // const router = useRouter()
    let add_data = JSON.stringify(form)
    axios.post(n_url, add_data, { headers: { "content-type": "application/json" } }).then(() => {
        // router.push('home')
        window.location.href = '/bloglist';
    }).catch(err => {
        console.log(err)
        console.log(typeof (add_data))
        console.log(add_data)
    })
}
const onSubmit = () => {
    console.log(form)
    addblogs()
}
</script>