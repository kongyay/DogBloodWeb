import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    currentPage: 1,
    filename: '',
    imageUrl: "",
    result: [],
    loading: false,
    waitState: "",
    errmsg: "",
  },
  mutations: {
    SET_PAGE: (state, payload) => {
      console.log('Go to page', payload)
      state.currentPage = payload
    },
    SET_FILENAME: (state, payload) => {
      console.log('Current file name', payload)
      state.filename = payload
    },
    SET_IMAGE_URL: (state, payload) => {
      state.imageUrl = payload
    },
    SET_RESULT: (state, payload) => {
      state.result = payload
    },
    START_LOADING: (state) => {
      state.loading = true
      state.waitState = 'wait'
    },
    STOP_LOADING_SUCCESS: (state) => {
      state.loading = false
      state.waitState = 'success'
    },
    STOP_LOADING_FAIL: (state, payload) => {
      state.loading = false
      state.waitState = 'fail'
      state.errmsg = payload
    },
    RESTART: (state, payload) => {
      state.currentPage = 1
      state.filename = ''
      state.imageUrl = ''
      state.result = []
    },
  },
  actions: {

  },
  getters: {
    getCurrentPage: state => state.currentPage,
    getFilename: state => state.filename,
    getResult: state => state.result,
    getImageUrl: state => state.imageUrl,
    getLoading: state => state.loading,
    getWaitState: state => state.waitState,
    getErrmsg: state => state.errmsg
  }
})