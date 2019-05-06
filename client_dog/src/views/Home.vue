<template lang='pug'>
  v-container
    //Search
    search-result
    
    // Main
    
    v-stepper(v-model='currentPage' vertical)
      v-stepper-step(step='1', :complete='currentPage>1') Enter Information and Image
      v-stepper-content(step='1')
        Classify1()
        v-btn(v-if='getFilename.length>0' color='primary', @click='SET_PAGE(2)' outline) Continue

      v-stepper-step(step='2', :complete='currentPage>2') Detection 1
      v-stepper-content(step='2')
        Classify2(:step='1')
        v-btn(color='primary', @click='SET_PAGE(1)' outline) Back

      v-stepper-step(step='3', :complete='currentPage>2') Detection 2
      v-stepper-content(step='3')
        Classify2(:step='2')
        v-btn(color='primary', @click='SET_PAGE(2)' outline) Back

      v-stepper-step(step='4', :complete='currentPage>3') View the classified data
      v-stepper-content(step='4')
        Classify3()
        v-btn(color='primary', @click='SET_PAGE(3)' outline) Back
      v-btn(color='error', @click='SET_PAGE(1)' flat) Restart
</template>

<script>
import { mapGetters, mapMutations } from "vuex";
import Classify1 from "../components/Classify1";
import Classify2 from "../components/Classify2";
import Classify3 from "../components/Classify3";
import SearchResult from "../components/SearchResult";

export default {
  data() {
    return {
      page: 1
    };
  },
  computed: {
    ...mapGetters(["getCurrentPage", "getFilename"]),
    currentPage: {
      get: function() {
        return this.getCurrentPage;
      },
      set: function(newVal) {
        this.SET_PAGE(newVal);
      }
    }
  },
  methods: {
    ...mapMutations(["SET_PAGE"])
  },
  components: {
    Classify1,
    Classify2,
    Classify3,
    SearchResult
  }
};
</script>
