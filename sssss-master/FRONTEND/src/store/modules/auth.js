import jwtDecode from 'jwt-decode'

const state = {
  token: null,
}

const mutations = { 
  // 로그인 상태 정보를 저장한다.
  setToken(state, token){
    state.token = token
  },
}

const actions = { 
  // 로그인 작업 실행
  login(options, token){
    options.commit('setToken', token)
    localStorage.setItem("access_token", token)
  },
  logout(options){
    options.commit('setToken', null)
    localStorage.removeItem("access_token")
  },
  getTokenInLocalStorage(options) {
    let token = localStorage.getItem("access_token")
    if(token != null) {
      options.commit('setToken', token)
    }
  },
}

const getters = { // 저장소 상태 정보를 계싼하여 조회할 필요가 있을때 사용한다.
  isAuthenticated: function(state){
    return state.token ? true : false
  },
  requestHeader(state){
    return {
      headers: {
        Authorization: `JWT ${state.token}`
      }
    }
  },
  userId: function(state){
    return state.token ? jwtDecode(state.token).user_id : null
  },
  loggedInUser(state) {
		return state.token ? jwtDecode(state.token) : null;
	},
}

export default {
    state, 
    mutations, 
    actions,
    getters,
}
