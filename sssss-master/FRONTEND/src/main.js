import Vue from 'vue'
import App from './App.vue'
import './plugins/element.js'
import router from './router/index.js';
import store from './store/index.js';
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import VueSession from 'vue-session'

import '@mdi/font/css/materialdesignicons.css' 

Vue.use(Vuetify)
Vue.use(VueSession)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  beforeCreate() {
    this.$store.dispatch("getTokenInLocalStorage")
  },
  vuetify: new Vuetify(),
  render: h => h(App),
  data: {
  }
}).$mount('#app')

export default new Vuetify({
  icons: {
    iconsfont: 'mdi' || 'mdiSvg' || 'md' || 'fa' || 'fa4'
  }
})