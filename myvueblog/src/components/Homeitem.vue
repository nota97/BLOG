<script setup lang="ts">
import { ref } from 'vue';

let settitle = ref("WELCOME")
let posttime = ref(new Date)
let setcontent = ref("THIS IS GALI CENTER")
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