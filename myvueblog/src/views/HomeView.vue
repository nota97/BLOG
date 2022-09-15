<script setup lang="ts">
import { onBeforeRouteUpdate, RouterLink, RouterView, useRoute, useRouter } from 'vue-router'
import {
  Document,
  Menu as IconMenu,
  Location,
  Setting,
  Histogram,
} from '@element-plus/icons-vue'
import { onMounted, reactive, ref, toRefs, watch } from 'vue';
import axios from 'axios';
const handleOpen = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
const handleClose = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
const urls = [
  'https://fuss10.elemecdn.com/a/3f/3302e58f9a181d2509f3dc0fa68b0jpeg.jpeg',
  'https://fuss10.elemecdn.com/1/34/19aa98b1fcb2781c4fba33d850549jpeg.jpeg',
  'https://fuss10.elemecdn.com/0/6f/e35ff375812e6b0020b6b4e8f9583jpeg.jpeg',
  'https://fuss10.elemecdn.com/9/bb/e27858e973f5d7d3904835f46abbdjpeg.jpeg',
  'https://fuss10.elemecdn.com/d/e6/c4d93a3805b3ce3f323f7974e6f78jpeg.jpeg',
  'https://fuss10.elemecdn.com/3/28/bbf893f792f03a54408b3b7a7ebf0jpeg.jpeg',
]

let base_url = "http://127.0.0.1:8000/api/blogs";
const state = reactive({
  blogs_list: [],
})
const getblogs = () => {
  axios.get(base_url).then(res => {
    state.blogs_list = res.data;
    console.log(state.blogs_list)
  }).catch(err => {
    console.log(err)
  })
}
// let settitle = ref("WELCOME")
// let posttime = ref(new Date)
// let setcontent = ref("THIS IS GALI CENTER")
let lname = "GALI"
const userimage = reactive({
  circleUrl:
  "https://avatars.githubusercontent.com/u/57176280?s=400&u=e8e4df48c4593bd6fc77a8f49f2dde786d736a80&v=4",
})
const { circleUrl } = toRefs(userimage)

const router = useRouter()
const route = useRoute()
const activeIndex = ref(route.path)
const itemclick = (index: any) => {
  // let text: string = state.blogs_list[index]['content']
  // // text = text.replace('\n',' ')
  // setcontent.value = text
  // settitle.value = state.blogs_list[index]['title']
  // posttime.value = state.blogs_list[index]['post_time']
  router.push({ name: 'knowitem', params:{index:index}})
  activeIndex.value = route.path
  console.log(activeIndex.value)
}
watch(
  ()=> route.path,
  (newValue,oldValue)=>{
    activeIndex.value = newValue
  },
  {immediate:true}
)
onMounted(() => {
  getblogs();
})

</script>

<template>
  <el-scrollbar height="100%">

    <div class="common-layout">
      <el-container>
        <el-aside width="20%">
          <el-col :span="12">
            <div style="position:relative; text-align: center;">
              <el-avatar :size="100" :src="circleUrl" />
              <h1 class="mb-2">{{lname}}</h1>
            </div>

            <el-menu router :default-active="activeIndex" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose" >
              <el-sub-menu index="1">
                <template #title>
                  <el-icon>
                    <document />
                  </el-icon>
                  <span>KNOWLEDGE</span>
                </template>

                <el-menu-item v-for="item,index in state.blogs_list" :key="index" :index="'/home/knowitem/'+index+''"
                  @click="itemclick(index)" >{{item['title']}}</el-menu-item>

              </el-sub-menu>
              <el-menu-item index="/home/helloworld" route="/home/helloworld">
                <el-icon>
                  <Histogram />
                </el-icon>
                <span >HISTOGRAM</span>
              </el-menu-item>
              <el-menu-item index="3" disabled>
                <el-icon>
                  <location />
                </el-icon>
                <span>LOCATION</span>
              </el-menu-item>
              <el-menu-item index="/home/setting" router="/home/setting">
                <el-icon>
                  <setting />
                </el-icon>
                <span>SETTING</span>
              </el-menu-item>
            </el-menu>
          </el-col>
        </el-aside>
        <RouterView />
        <!-- <el-container>
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
        </el-container> -->
      </el-container>
    </div>
    <div class="demo-image__lazy">
      <el-image v-for="url in urls" :key="url" :src="url" lazy />
    </div>
    
  </el-scrollbar>

</template>

<style>
.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.box-card {
  width: 480px;
}

.demo-image__lazy {
  height: 70%;
  overflow-y: auto;
}

.demo-image__lazy .el-image {
  display: block;
  min-height: 200px;
  margin-bottom: 10px;
}

.demo-image__lazy .el-image:last-child {
  margin-bottom: 0;
}

.common-layout {
  padding: 20px;
}
</style>
