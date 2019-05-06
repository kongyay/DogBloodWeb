<template lang="pug">
  v-container
    v-layout(row)
      v-flex(xs12 )
        v-alert(:value='true', color='black', icon='info', outline)
          div.headline Dog: {{record.dog_data.dog_name}}
          div.title
            code.black--text (id: {{record.dog_data.dog_id}})
          div.subheading Owner: {{record.dog_data.owner_name}}
    v-divider(pa-2)
    v-layout(row)
      v-flex(xs12)
        v-chip.black--text(outline)
          h2 Record {{index+1}} ({{record.timestamp}})
        v-data-table.elevation-1(:headers='headers', :items='record.classify_data' hide-actions)
          template(v-slot:items="props")
            tr(@click='SWITCH_VERIFY_RESULT(i)')
              td
                v-checkbox(:input-value='props.item.verify', primary, hide-details)
              td {{ props.item.class }}
              td.text-xs-right {{ props.item.value }}
</template>


<script>
export default {
  data() {
    return {
      record: {},
      index: 0,
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
  mounted() {
    this.record = JSON.parse(this.$route.query.record)
    this.index = parseInt(this.$route.query.index)
    setTimeout(() => window.print(),2000) 
  }
}
</script>
