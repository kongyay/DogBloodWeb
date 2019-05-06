<template lang='pug'>
  v-layout(row wrap)
    // Search
    v-flex(xs12 v-if='getSearchResult.length>0')
      v-alert(:value='true', color='primary', icon='info', outline)
        div.headline Dog: {{getSearchResult[0].dog_data.dog_name}}
        div.title
          code (id: {{getSearchResult[0].dog_data.dog_id}})
        div.subheading Owner: {{getSearchResult[0].dog_data.owner_name}}

          
      
    v-divider.pa-2(v-if='getSearchResult.length>0')
    v-flex(xs12 v-for='(record,i) in getSearchResult' :key='i')
      report-card(:record='record',:index='i')
    v-divider.pa-3(v-if='getSearchResult.length>0')
</template>

<script>
import { mapGetters } from "vuex";
import ReportCard from './ReportCard.vue'
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
    
  },
  components: {
    ReportCard
  }
};
</script>