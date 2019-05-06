<template lang="pug">
  v-app
    v-toolbar(app='')
      v-toolbar-title.headline.text-uppercase
        span DOGBLOOD
        span.font-weight-light CLASSIFICATION
      v-spacer
      v-layout(row, style='max-width: 250px')
        v-text-field(v-if='$route.path!=="/print"' v-model='searchTxt' @keyup.enter="goSearch" @click:append='goSearch', placeholder='Search...', single-line, append-icon='search', hide-details)
    v-content
      router-view
    v-dialog(v-model='loading', :persistent="getWaitState=='wait'", width='300')
      v-card(:color="getWaitState=='success' && 'light-green' || getWaitState=='fail' && 'amber' || 'primary' " , dark)
        v-card-text
            span(v-if="getWaitState=='wait'") กรุณารอสักครู่..
            span(v-if="getWaitState=='success'") สำเร็จ !
            span(v-if="getWaitState=='fail'") ไม่สำเร็จ :( {{getErrmsg}}
            v-progress-linear.mb-0(:indeterminate="getWaitState=='wait'", color='white')
</template>

<script>
import { mapGetters, mapMutations, mapActions } from "vuex";
export default {
  name: "App",
  components: {},
  data() {
    return {
      searchTxt: ""
    };
  },
  computed: {
    ...mapGetters(["getLoading", "getWaitState", "getErrmsg"]),
    loading: {
      get: function() {
        return this.getLoading;
      },
      // eslint-disable-next-line
      set: function(newVal) {
        this.STOP_LOADING();
      }
    }
  },
  methods: {
    ...mapMutations(["STOP_LOADING"]),
    ...mapActions(["search"]),
    goSearch() {
      console.log("search", this.searchTxt);
      this.search(this.searchTxt);
    }
  }
};
</script>
