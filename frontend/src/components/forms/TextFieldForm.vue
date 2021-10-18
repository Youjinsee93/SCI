<template>
    <v-row>
      <v-col>
        <v-textarea solo v-model="text"></v-textarea>
      </v-col>
    </v-row>

</template>

<script>
export default {
  name: "TextFieldForm",
  data () {
    return {
      text: '',
    }
  },
  watch: {
    text: function(oldVar, newVar) {
      this.$emit('onAnswerChanged', this.text)
    },
  },
  methods: {
    set_value: function(val) {
      this.text = val
    }
  }

}
</script>

<style scoped>

</style>