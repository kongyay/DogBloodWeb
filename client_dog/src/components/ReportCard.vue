<template lang="pug">
  div
    v-layout(row)
      v-flex(xs3)
        v-img.preview.elevation-3.ma-2(:src='record.image || "https://meredith.nhcrafts.org/wp-content/uploads/dog-placeholder.jpg"')
      v-flex(xs9)
        v-chip(color='primary' dark)
          h2 Record {{index+1}} ({{record.timestamp}})
        v-data-table.elevation-1(:headers='headers', :items='record.classify_data' hide-actions flat)
          template(v-slot:items="props")
            tr
              td
                v-checkbox(:input-value='props.item.verify',@change='switchVerify(index,props.index)', primary, hide-details)
              td {{ props.item.class }}
              td.text-xs-right {{ props.item.value }}
    v-layout(row)
      v-flex(xs3 offset-xs9)
        v-btn(color='info', @click='print()' block outline round) 
          v-icon.px-2 print
          | Print
</template>


<script>
import { mapMutations } from "vuex";
export default {
  props: {
    record: Object,
    index: Number
  },
  data() {
    return {
      headers: [
        {
          text: "Verify",
          value: "verify",
          align: 'left',
          sortable: false,
        },
        {
          text: "Class",
          value: "class"
        },
        {
          text: "Percent (%)",
          align: "right",
          value: "value"
        }
      ]
    };
  },
  methods: {
    ...mapMutations(["SWITCH_VERIFY_RESULT"]),
    switchVerify(index,classi) {
      this.SWITCH_VERIFY_RESULT({index,classi})
    },
    print() {
      let printWindow = window.open(
        this.$router.resolve(
          {
            name: "print", 
            query: {record: JSON.stringify(this.record), index:this.index}
          }).href,
          "Print Report",
          "width=595,height=842"); 
      printWindow.print()
    }
  }
}
</script>
