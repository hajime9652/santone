import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css'
import VueSession from 'vue-session'

const opts = {}
Vue.use(Vuetify)
Vue.use(VueSession)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  vuetify: new Vuetify(opts),
  render: h => h(App)
}).$mount('#app')
