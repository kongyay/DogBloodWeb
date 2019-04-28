<template lang="pug">
  v-container
    v-layout(row)
      v-img.preview.elevation-3(:src='getImageUrl')
    v-layout(column align-space-around justify-center fill-height)
      v-flex()
        v-data-table.elevation-1(:headers='headers', :items='getResult')
          template(v-slot:items="props")
            td {{ props.item.class }}
            td.text-xs-right {{ props.item.value }}
            
</template>

<script>
import { mapGetters, mapMutations } from "vuex";
export default {
  data() {
    return {
      headers: [
        {
          text: "Class",
          value: "class"
        },
        {
          text: "Percent (%)",
          align: "right",
          value: "value"
        }
      ],
      valid: true,
      waitState: "",
      errmsg: "",
      radius: [1, 100]
    };
  },
  computed: {
    ...mapGetters(["getResult", "getImageUrl"])
  },
  methods: {
    ...mapMutations(["SET_VERIFY_RESULT"])
  }
};
</script>