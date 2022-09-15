<template>
    <div class="lx">
      <h1>{{data.d1}}</h1>
      <h2>{{data.d2}}</h2>
    </div>
</template>
  
<script lang="ts" setup>
import { getCurrentInstance, reactive, toRefs } from 'vue';


      const { proxy } = getCurrentInstance() as any
      console.log(proxy.$loginingUser)
      const data = reactive({
          d1 : "记忆它过了很久：不是本人",
          d2 : proxy.$loginingUser,
      })

     
</script>

  <style>
  @media (min-width: 1024px) {
    .lx {
      min-height: 100vh;
      display: flex;
      align-items: center;
      left:0px;
      padding:100px;
      margin:0px;
    }
  }
  </style>
  
  
  