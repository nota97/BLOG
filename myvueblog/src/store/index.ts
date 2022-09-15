import {createStore} from 'vuex'

export default createStore({
    state:{
        loginingToken : "",
        loginingUser : "",
    },
    getters:{},
    mutations:{
        setLoginMsg(state, data){
            state.loginingToken = data.token;
            state.loginingUser = data.user;
        },
    },
    actions:{},
    modules:{},
});