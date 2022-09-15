import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import './assets/main.css'
import store from './store'

const app = createApp(App)

app.use(router)
app.use(ElementPlus)
app.mount('#app')

//注册全局变量
app.config.globalProperties.$loginingUser = ''
app.config.globalProperties.$loginingToken = ""