<template>
  <v-item-group multiple v-model="selected">
    <v-row>
      <v-col
        v-for="option in options"
        :key="option"
        md="3"
      >
          <v-item v-slot="{ active, toggle }">
            <v-row>
              <v-col>
                <v-card
                  :class="{'red-outline': active}"
                  :color="get_color(option)"
                  class="d-flex align-center default-outline"
                  @click="toggle"
                >
                  <span class="py-4 text-center mx-auto ">{{ option }}</span>
                </v-card>
              </v-col>
              <v-col cols="auto">
                <sign-video-tooltip :resourcePath="get_video(option)"></sign-video-tooltip>
              </v-col>
            </v-row>
          </v-item>
      </v-col>
    </v-row>
  </v-item-group>

</template>

<script>
import SignVideoTooltip from "@/components/SignVideoTooltip";

export default {
  name: "WordSelectForm",
  components: { SignVideoTooltip },
  props: ['answer_selection'],
  data () {
    return {
      selected: [],
    }
  },
  watch: {
    selected: function(oldVar, newVar) {
      let selected_text = []
      let self = this
      this.selected.forEach(function(i, e) {
        selected_text.push(self.options[i])
      })
      this.$emit('onAnswerChanged', selected_text)
    }
  },
  computed: {
    options: function() {
      let opts = []

      if(this.answer_selection == null) return []
      this.answer_selection.forEach(function(e) {
        opts.push(e.label)
      })
      return opts
    }
  },
  methods: {
    set_value: function(val) {
      if(val == null) return;

      let self = this
      let _selected = []

      val.forEach(function(e) {
        const idx = self.options.indexOf(e)
        if(idx != -1) {
          _selected.push(idx)
        }
      })

      this.selected = _selected
    },
    get_video: function(label) {
      let item = null
      this.answer_selection.forEach(function(e) {
        if(e.label == label) {
          item = e.sign_video
        }
      })
      return item
    },
    get_color: function(label) {
      let item = null
      this.answer_selection.forEach(function(e) {
        if(e.label == label) {
          item = e.color
        }
      })
      return item
    }
  }
}
</script>

<style scoped>
.default-outline {  border: 1px solid transparent !important; }
.red-outline { border: 1px solid #cd0000 !important; }
</style>