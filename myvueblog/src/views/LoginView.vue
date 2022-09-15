<template>
    <div class="con_login">
        <div class="form_login">
            <h1> 登录</h1>
            <span>请输入你的账号密码</span>
            <el-divider />
            <el-form :model="form" label-width="100px">
                <el-form-item label="账号">
                    <el-input v-model="form.user" />
                </el-form-item>
                <el-form-item label="密码" prop="pass">
                    <el-input v-model="form.password" type="password" autocomplete="off" />
                </el-form-item>
                <el-form-item>
                    <el-link :underline="false">没有账号请点击注册</el-link>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="onSubmit">Login</el-button>
                    <el-button @click="onCancel">Cancel</el-button>
                </el-form-item>
            </el-form>
        </div>

    </div>
</template>
  
<style>
.con_login {
    position: relative;
    height: 100%;
    width: 100%;
    background-image: url(https://fuss10.elemecdn.com/a/3f/3302e58f9a181d2509f3dc0fa68b0jpeg.jpeg);
}

.form_login {
    padding: 30px;
    width: 20%;
    left: 50%;
    top: 40%;
    transform: translate(-50%, -50%);
    position: absolute;
    border: 1px solid var(--el-border-color);
    border-radius: 10px;
    background-color: white;
}

.el-link {
    margin-right: 8px;
}

.el-link .el-icon--right.el-icon {
    vertical-align: text-bottom;
}
</style>

<script lang="ts" setup>
import axios from 'axios'
import { getCurrentInstance, reactive } from 'vue'
import { useRouter } from 'vue-router'

// do not use same name with ref
const router = useRouter();
const form = reactive({
    user: '',
    password: '',
})
let LoginingUser = {
    user: "",
    token: "",
    date: null,
}
console.log("LoginingUser:"+LoginingUser)
let loginToken = "";
let loginingUser = "";
let login_url = "http://127.0.0.1:8000/api/login/";
// const { proxy } = getCurrentInstance() as any
// console.log(proxy.$loginingUser)
const logincheck = () => {
    let loginData = JSON.stringify(form)
    console.log(loginData)
    axios.post(login_url, loginData, { headers: { "content-type": "application/json" } }).then(res => {
        loginToken = res.data.data['token']
        loginingUser = res.data.data['nickname']

        if (res.data['code'] == 200) {
            console.log("登录成功")
            console.log(loginToken, loginingUser)
            // proxy.$loginingUser = loginingUser
            // console.log(proxy.$loginingUser)
            let LoginingUser = {
                user: loginingUser,
                token: loginToken,
                date: Date.now()
            }
            localStorage.setItem("loginingUser", loginingUser);
            localStorage.setItem("loginToken", loginToken);
            localStorage.setItem("LoginingUser", JSON.stringify(LoginingUser))
            // router.push({ path: '/' })
            window.location.href = '/'
        }
        else {
            console.log(res.data)
            alert(res.data['data'])
        }
    }).catch(err => {
        console.log(err.data)
        alert(err.data)
    })
}

const onSubmit = () => {
    logincheck();
}
const onCancel = () => {
    form.user = "";
    form.password = "";
}
</script>