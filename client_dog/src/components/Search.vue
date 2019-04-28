<template lang='pug'>
  v-layout(row wrap)
    // Search
    v-flex(xs12 v-if='getSearchResult.length>0')
      h2 Dog: {{getSearchResult[0].dog_data.dog_name}} 
      | (id: {{getSearchResult[0].dog_data.dog_id}})
      h3 Owner: {{getSearchResult[0].dog_data.owner_name}}
      v-btn(color='primary', @click='print()' block outline) Print
    v-divider.pa-1(v-if='getSearchResult.length>0')
    v-flex(xs12 v-for='(record,i) in getSearchResult' :key='i')
      v-layout(row)
        v-flex(xs3)
          v-img.preview.elevation-3.ma-2(:src='record.image || "https://meredith.nhcrafts.org/wp-content/uploads/dog-placeholder.jpg"')
        v-flex(xs9)
          h2 Record {{i+1}}
          v-data-table.elevation-1(:headers='headers', :items='record.classify_data' hide-actions)
            template(v-slot:items="props")
              tr(@click='SWITCH_VERIFY_RESULT(i)')
                td
                  v-checkbox(:input-value='props.item.verify', primary, hide-details)
                td {{ props.item.class }}
                td.text-xs-right {{ props.item.value }}

    v-divider.pa-1(v-if='getSearchResult.length>0')
</template>

<script>
import { mapGetters, mapMutations } from "vuex";

export default {
  data() {
    return {
      page: 1,
      headers: [
        {
          text: "Verify",
          value: "verify"
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
  computed: {
    ...mapGetters(["getSearchResult"])
  },
  methods: {
    ...mapMutations(["SWITCH_VERIFY_RESULT"]),
    print() {
      window.print();
    }
  },
  components: {}
};
</script>