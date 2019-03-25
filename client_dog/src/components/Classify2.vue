<template lang="pug">
  v-container
    v-layout(align-space-around justify-center fill-height)
      v-flex(shrink style='width: 50px')
          v-text-field.mt-0(v-model='radius[0]' hide-details single-line type='number')
      v-flex.mx-2()
          v-range-slider(v-model='radius' :max='100' :min='1' :step='1')
      v-flex(shrink style='width: 50px')
          v-text-field.mt-0(v-model='radius[1]' hide-details single-line type='number')
    v-layout(row)
      v-btn(@click='resize' color='primary' round block :disabled="!valid||getLoading" :loading="getLoading") Resize
    v-layout(row)
      v-img.preview.elevation-3(:src='getImageUrl')
    v-layout(row)
        v-btn(@click='confirm' color='success' round block :disabled="!valid||getLoading" :loading="getLoading") Confirm
</template>

<script>
import { mapGetters, mapMutations } from "vuex";
export default {
  data() {
    return {
      valid: true,
      loading: false,
      waitState: "",
      errmsg: "",
      imageUrl: "",
      radius: [1, 100]
    };
  },
  computed: {
    ...mapGetters(["getFilename", "getImageUrl", "getLoading"])
  },
  methods: {
    ...mapMutations([
      "SET_PAGE",
      "SET_FILENAME",
      "SET_RESULT",
      "START_LOADING",
      "STOP_LOADING_SUCCESS",
      "STOP_LOADING_FAIL"
    ]),
    async resize() {
      console.log("resized", this.radius);
      this.START_LOADING();
      let header = {
        "Content-type": "application/json"
      };
      let obj = {};
      obj.minradius = this.radius[0];
      obj.maxradius = this.radius[1];
      obj.dogId = this.dogId;
      obj.imageName = this.getFilename;
      console.log(obj);
      try {
        let result = await this.$axios.post(
          `${process.env.VUE_APP_API_URL}/dog/resize`,
          obj,
          header
        );
        console.log(result);
        if ("error" in result.data) throw result.data.error;
        this.STOP_LOADING_SUCCESS();
      } catch (e) {
        this.STOP_LOADING_FAIL(e);
      }
    },
    async confirm() {
      console.log("confirmed", this.radius);
      this.START_LOADING();
      let header = {
        "Content-type": "application/json"
      };
      let obj = {};
      obj.imageName = this.getFilename;
      console.log(obj);
      try {
        let result = await this.$axios.post(
          `${process.env.VUE_APP_API_URL}/dog/confirm`,
          obj,
          header
        );
        console.log(result);
        if ("error" in result.data) throw result.data.error;
        this.SET_RESULT(result.data);
        this.STOP_LOADING_SUCCESS();
        this.SET_PAGE(3);
      } catch (e) {
        this.STOP_LOADING_FAIL(e);
      }
    }
  }
};
</script>
