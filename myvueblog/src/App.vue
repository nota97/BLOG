<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import { onMounted, ref } from 'vue'
import store from './store';
const activeIndex = ref('1')
const activeIndex2 = ref('1')
const handleSelect = (key: string, keyPath: string[]) => {
  console.log(key, keyPath);
  console.log(store.state.loginingUser)
}
const setemtpyuser = ()=>{
    let emptyuser = {
    user: "",
    token: "",
    date: null,}
    localStorage.setItem("LoginingUser",JSON.stringify(emptyuser))
}
let lname = ""
let lu :any  =  localStorage.getItem("LoginingUser")  
lu = JSON.parse(lu)
console.log(lu)
if (lu.user != ""){
  if (Date.now() - lu.date > 43200000){
    setemtpyuser();
  }else{
    lname = lu.user
  }
}

console.log(lname)
const onSubmit = () => {
  localStorage.setItem("loginingUser", "")
  localStorage.setItem("loginToken", "")
  setemtpyuser();
  window.location.href = '/'
}
</script>

<template>
  <header>
    <div>
      <el-menu router :default-active="activeIndex2" class="el-menu-demo" mode="horizontal" background-color="#545c64"
        text-color="#fff" active-text-color="#ffd04b" @select="handleSelect">
        <el-menu-item index="1" route="/">GALI Center</el-menu-item>
        <el-sub-menu index="2" v-show="lname">
          <template #title >Blogspace</template>
          <el-menu-item index="2-1" route="/bloglist">blog list</el-menu-item>
          <el-menu-item index="2-2" route="/blogadd">add blog</el-menu-item>
          <el-menu-item index="2-3" disabled>item three</el-menu-item>
          <el-sub-menu index="2-4">
            <template #title>item four</template>
            <el-menu-item index="2-4-1">item one</el-menu-item>
            <el-menu-item index="2-4-2">item two</el-menu-item>
            <el-menu-item index="2-4-3">item three</el-menu-item>
          </el-sub-menu>
        </el-sub-menu>
        <el-menu-item index="3" route="/about">about</el-menu-item>
        <el-menu-item index="4" route="/lx">Orders</el-menu-item>
        <div v-if="lname" style="right: 1%; position: absolute; width: 200px; height: 59px;">
          <el-avatar style="right: 40%;top: 20%; position: absolute;" src="https://avatars.githubusercontent.com/u/57176280?s=400&u=e8e4df48c4593bd6fc77a8f49f2dde786d736a80&v=4"  />
          <el-dropdown  style="left: 90%; top: 40%; position: absolute;" >

            <el-link :underline="false" type="primary">{{lname}}</el-link>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item>PersonCenter</el-dropdown-item>
                <el-dropdown-item @click="onSubmit">LoginOut</el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </div>

        <!-- <el-link :underline="false" type="primary" v-if="lname" @click="onSubmit">{{lname}}</el-link> -->
        <el-link :underline="false" type="primary" href="/login" v-else>Login</el-link>
      </el-menu>
    </div>

    <RouterView />
  </header>
</template>


<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
  padding: 0px;
  margin: 0px;
  position: absolute;
  top: 0px;
  left: 0px;
  width: 200%;
  height: 100%;
  border: hidden;
}

.el-link {
  margin-right: 8px;
  position: absolute;
  right: 1%;
  top: 30%;
}

.el-link .el-icon--right.el-icon {
  vertical-align: text-bottom;
}
</style>
