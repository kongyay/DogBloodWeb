<template lang="pug">
  v-container
    v-layout(row)
        v-flex(xs12 md6)
          | Param 1
        v-flex(xs12 md6)
          v-text-field(v-model="param1" required :rules="numberOnlyRules" label='Param 1')
    v-layout(row)
        v-flex(xs12 md6)
          | Param 2
        v-flex(xs12 md6)
          v-text-field(v-model="param2" required :rules="numberOnlyRules" label='Param 2')
    v-layout(row)
        v-flex(xs12 md6)
          | Distance
        v-flex(xs12 md6)
          v-text-field(v-model="distance" required :rules="numberOnlyRules" label='Distance')
    v-layout(row)
        v-flex(xs12 md6)
          | Min-Max Radius
        v-flex(xs12 md6)  
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
  props: { step: Number },
  data() {
    return {
      valid: true,
      param1: 20,
      param2: 20,
      distance: 15,
      radius: [10, 20],
      numberOnlyRules: [
        v => (!!v && /^[0-9]{0,10}$/.test(v)) || "กรุณากรอกเป็นตัวเลข"
      ]
    };
  },
  computed: {
    ...mapGetters(["getFilename", "getImageUrl", "getLoading", "getDogData"]),
    imageUrl: {
      get: function() {
        return this.getImageUrl;
      },
      set: function(newVal) {
        this.SET_IMAGE_URL(newVal);
      }
    }
  },
  methods: {
    ...mapMutations([
      "SET_PAGE",
      "SET_FILENAME",
      "SET_RESULT",
      "SET_IMAGE_URL",
      "START_LOADING",
      "STOP_LOADING",
      "LOADING_SUCCESS",
      "LOADING_FAIL"
    ]),
    async resize() {
      console.log("resized", this.radius);
      this.START_LOADING();
      let header = {
        "Content-type": "application/json"
      };
      let obj = {};
      obj.param1 = parseFloat(this.param1);
      obj.param2 = parseFloat(this.param2);
      obj.distance = parseFloat(this.distance);
      obj.minradius = parseFloat(this.radius[0]);
      obj.maxradius = parseFloat(this.radius[1]);
      obj.imageName = this.getFilename;
      console.log(obj);
      try {
        let result = await this.$axios.post(
          `${process.env.VUE_APP_API_URL}/dog/resize/${this.step}`,
          obj,
          header
        );
        console.log(result);
        if ("error" in result.data) throw result.data.error;
        this.imageUrl = result.data.image;
        this.LOADING_SUCCESS();
      } catch (e) {
        this.LOADING_FAIL(e);
      }
    },
    async confirm() {
      console.log("confirmed", this.radius);
      this.START_LOADING();
      let header = {
        "Content-type": "application/json"
      };
      let obj = { ...this.getDogData };
      obj.imageName = this.getFilename;
      console.log(obj);
      try {
        let result = await this.$axios.post(
          `${process.env.VUE_APP_API_URL}/dog/confirm/${this.step}`,
          obj,
          header
        );
        console.log(result);
        if ("error" in result.data) throw result.data.error;
        if (this.step == 1) {
          this.imageUrl = result.data.image;
        } else if (this.step == 2) {
          this.SET_RESULT(result.data);
        }

        this.LOADING_SUCCESS();
        this.SET_PAGE(this.step + 2);
      } catch (e) {
        this.LOADING_FAIL(e);
      }
    }
  },
  mounted() {
    if (this.step === 2) {
      this.param1 = 15;
      this.param2 = 15;
      this.distance = 55;
      this.minradius = 50;
      this.radius = [50, 67];
    }
  }
};
</script>
