<template lang="pug">
  v-app
    v-toolbar(app='')
      v-toolbar-title.headline.text-uppercase
        span DOGBLOOD
        span.font-weight-light CLASSIFICATION
      v-spacer
      v-btn(flat='', href='https://github.com/vuetifyjs/vuetify/releases/latest', target='_blank')
        span.mr-2 v1.0
    v-content
      router-view
    v-dialog(v-model='getLoading', :persistent="getWaitState=='wait'", width='300')
      v-card(:color="getWaitState=='success' && 'light-green' || getWaitState=='fail' && 'amber' || 'primary' " , dark)
        v-card-text
            span(v-if="getWaitState=='wait'") รอแป๊บนึง..
            span(v-if="getWaitState=='success'") สำเร็จ !
            span(v-if="getWaitState=='fail'") ไม่สำเร็จ :( {{getErrmsg}}
            v-progress-linear.mb-0(:indeterminate="getWaitState=='wait'", color='white')
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "App",
  components: {},
  data() {
    return {
      //
    };
  },
  computed: {
    ...mapGetters(["getLoading", "getWaitState", "getErrmsg"])
  },
  methods: {}
};
</script>
