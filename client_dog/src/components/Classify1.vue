<template lang="pug">
  v-container
    v-layout(column align-space-around justify-center fill-height)
      v-form(ref="form")
        v-container
          v-layout(row)
            v-flex(xs12 md1)
              | Owner Name
            v-flex(xs12 md11)
              v-text-field(v-model="ownerName" required :rules="ownerNameRules" label='Owner')
          v-layout(row)
            v-flex(xs12 md1)
              | Dog Name
            v-flex(xs12 md11)
              v-text-field(v-model="dogName" required :rules="dogNameRules" label='Dog')
          v-layout(row)
            v-flex(xs12 md1)
              | Dog ID
            v-flex(xs12 md11)
              v-text-field(v-model="dogId" required :rules="dogIdRules" label='ID')
          v-layout(row)
            v-flex(xs12 md1)
              | Image
            v-flex(xs12 md11)
              v-img.preview.elevation-3(:src='imageUrl' @click='pickFile')
              v-text-field(label='Select Image', @click='pickFile', v-model='imageName', prepend-icon='attach_file' required :rules='imageRules')
              input(type='file', style='display: none', ref='image', accept='image/*', @change='onFilePicked')
          v-layout(row)
            v-btn(@click='validate' color='success' round block :disabled="!valid||getLoading" :loading="getLoading") Upload

    
  
</template>

<script>
import { mapMutations, mapGetters } from "vuex";
export default {
  data() {
    return {
      valid: true,
      ownerName: "",
      dogName: "",
      dogId: "",
      imageName: "",
      imageFile: "",
      ownerNameRules: [v => !!v || "กรุณากรอก"],
      dogNameRules: [v => !!v || "กรุณากรอก"],
      dogIdRules: [
        v => (!!v && /^[0-9]{0,10}$/.test(v)) || "กรุณากรอกเป็นตัวเลข"
      ],
      imageRules: [
        v => (!!v && !!this.imageUrl && !!this.imageFile) || "กรุณาเลือกรูปภาพ"
      ]
    };
  },
  computed: {
    ...mapGetters(["getImageUrl", "getLoading"]),
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
      "SET_IMAGE_URL",
      "SET_DOGDATA",
      "START_LOADING",
      "STOP_LOADING",
      "LOADING_SUCCESS",
      "LOADING_FAIL"
    ]),
    async validate() {
      if (this.$refs.form.validate()) {
        console.log("submitted");
        this.START_LOADING();
        let header = {
          "Content-type": "application/json"
        };
        let obj = {};
        obj.ownerName = this.ownerName;
        obj.dogName = this.dogName;
        obj.dogId = this.dogId;
        this.SET_DOGDATA(obj);
        obj.image = this.imageUrl;
        obj.imageName = this.imageName;
        console.log(obj);
        try {
          let result = await this.$axios.post(
            `${process.env.VUE_APP_API_URL}/dog/add`,
            obj,
            header
          );
          console.log(result);
          if ("error" in result.data) throw result.data.error;
          if ("filename" in result.data)
            this.SET_FILENAME(result.data.filename);
          this.LOADING_SUCCESS();
          this.SET_PAGE(2);
        } catch (e) {
          this.LOADING_FAIL(e);
        }
      }
    },
    pickFile() {
      this.$refs.image.click();
    },

    onFilePicked(e) {
      const files = e.target.files;
      if (files[0] !== undefined) {
        this.imageName = files[0].name;
        if (this.imageName.lastIndexOf(".") <= 0) {
          return;
        }
        const fr = new FileReader();
        fr.readAsDataURL(files[0]);
        fr.addEventListener("load", () => {
          this.imageUrl = fr.result;
          this.imageFile = files[0]; // this is an image file that can be sent to server...
        });
      } else {
        this.imageName = "";
        this.imageFile = "";
        this.imageUrl = "";
      }
    }
  }
};
</script>

<style scoped>
.preview {
  width: 100%;
}
</style>
