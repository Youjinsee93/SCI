import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import './assets/animation.css'

import VueRouter from 'vue-router'

import TypeOneProblem from "@/components/TypeOneProblem";
import Home from "@/components/Home";
import Register from "./components/Register";
import Introduction from "./components/Introduction";
import Demostration from "./components/Demonstration";
import Done from "./components/Done";

Vue.use(VueRouter)

Vue.config.productionTip = false

window.axios = require('axios');

import VueCookies from "vue-cookies";
Vue.use(VueCookies);

const router = new VueRouter({
    routes: [
        {path: '/', component: Introduction},
        {path: '/intro', component: Introduction},
        {path: '/register', component: Register},
        {path: '/demo', component: Demostration},
        {path: '/home', component: Home},
        {path: '/done', component: Done},
        {path: '/:uid/type1', component: TypeOneProblem},
        {path: '/:uid/type1/:problem_num', component: TypeOneProblem},
    ]
});

import {utils} from './utils.js'

Vue.prototype.$utils = utils

import VTooltip from 'v-tooltip'
Vue.use(VTooltip)
Vue.directive('tooltip', VTooltip.VTooltip)
Vue.directive('close-popover', VTooltip.VClosePopover)
Vue.component('v-popover', VTooltip.VPopover)

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')



