import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    currentPage: 1,
    filename: '',
    imageUrl: "",
    result: [],
    searchResult: [],
    loading: false,
    waitState: "",
    errmsg: "",
    dogData: {
      ownerName: '',
      dogName: '',
      dogId: 0
    }
  },
  mutations: {
    SET_PAGE: (state, payload) => {
      console.log('Go to page', payload)
      state.currentPage = payload
    },
    SET_DOGDATA: (state, payload) => {
      state.dogData = payload
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
    SET_SEARCH_RESULT: (state, payload) => {
      state.searchResult = payload
    },
    START_LOADING: (state) => {
      state.loading = true
      state.waitState = 'wait'
    },
    STOP_LOADING: (state) => {
      state.loading = false
    },
    LOADING_SUCCESS: (state) => {
      state.waitState = 'success'
    },
    LOADING_FAIL: (state, payload) => {
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
    async search({
      commit
    }, text) {
      if (text === '') {
        commit('SET_SEARCH_RESULT', [])
        return
      }

      try {
        let result = await global.axios.get(
          `${process.env.VUE_APP_API_URL}/record/find/${text}`,
        );
        console.log(result);
        if ("error" in result.data) throw result.data.error
        commit('SET_SEARCH_RESULT', result.data)
      } catch (e) {
        commit('START_LOADING')
        commit('LOADING_FAIL', e)
      }
    }
  },
  getters: {
    getCurrentPage: state => state.currentPage,
    getFilename: state => state.filename,
    getResult: state => state.result,
    getSearchResult: state => state.searchResult,
    getImageUrl: state => state.imageUrl,
    getLoading: state => state.loading,
    getWaitState: state => state.waitState,
    getErrmsg: state => state.errmsg,
    getDogData: state => state.dogData
  }
})