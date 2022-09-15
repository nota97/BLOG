<template>
  <el-table :data="blogs_list" stripe style="width: 100%">
    <el-table-column prop="title" label="title" width="180" />
    <el-table-column prop="content" label="content" />
    <!-- <el-table-column prop="url" label="url" /> -->
    <el-table-column prop="post_time" label="date" width="220" />
    <el-table-column fixed="right" label="Operations" width="120">
      <template #default="scope">
        <el-button link type="primary" size="small" @click="editblog(scope.$index, scope.row)">Edit</el-button>
        <el-button link type="primary" size="small" @click="deleteblog(scope.$index, scope.row['url'])">Delete</el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<script lang="ts">
  import axios from 'axios'
  import { reactive, onMounted, toRefs } from 'vue'
  import { useRouter } from 'vue-router'
  
  export default {
    name: 'blogs',
    setup() {
      const router = useRouter();
      let base_url = "http://127.0.0.1:8000/api/blogs";
      const state = reactive({
        blogs_list: [],
      })
      const getblogs = () => {
        axios.get(base_url, { params : { token : localStorage.getItem("loginToken")}}).then(res => {
          state.blogs_list = res.data;
          console.log(state.blogs_list)
        }).catch(err => {
          console.log(err)
        })
      }
      const editblog = (index: number, row:any) =>{
        console.log(index,row)
        router.push({ path: '/blogedit', query: row})
        // window.location.href = '/blogedit/'
      }
      const deleteblog = (index: number, row: string) => {
        let d_url = row
        console.log(index, d_url)
        axios.delete(d_url, { params : { token : localStorage.getItem("loginToken")}}).then(()=>{
          getblogs();
        }).catch(err => {
          console.log(err)
        })
      }
      onMounted(() => {
        getblogs();
      })
      return {
        ...toRefs(state),
        deleteblog,
        editblog,
      }
    }
  }
  
  </script>
  