import Vue from 'vue'
import Vuex from 'vuex'
import auth from './modules/auth.js'

Vue.use(Vuex)

export default new Vuex.Store({
  // vue에서 data
  state: {
  },
  // vue에서 methods
  mutations: {
  },
  // vue에서 methods들을 묶어놓음
  actions: {
  },
  modules: {
    auth,
  }
})