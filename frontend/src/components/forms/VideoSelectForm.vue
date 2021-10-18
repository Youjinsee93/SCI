<template>
  <v-item-group multiple v-model="selected">
    <v-row>
      <v-col
        v-for="option in options"
        :key="option"
        md="4"
      >

          <v-item v-slot="{ active, toggle }">


            <v-card
                v-if="!option.endsWith('.mp4')"
                :class="{'red-outline': active}"
                class="d-flex align-center"
                height="150"
                @click="toggle"
                style="background-size:contain;background-color:#f6f6f6;background-position:center;"
                :style="{backgroundImage: 'url(' + get_public_attachment_url(option) + ')'}"
            >

            </v-card>

            <v-card
                :class="{'red-outline': active}"
                class="d-flex align-center overflow-hidden"
                height="150"
                @click="toggle"
                v-else>
              <video width="100%" controls preload :src="get_public_attachment_url(option)"></video>
            </v-card>


          </v-item>

      </v-col>
    </v-row>
  </v-item-group>
</template>

<script>
export default {
  name: "VideoSelectForm",
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
      return this.answer_selection.split(';')
    }
  },
  methods: {
    get_public_attachment_url: function (file_name) {
      return this.$utils.getApiUrl() + '/attachments/' + file_name
    },
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
    }
  }

}
</script>

<style scoped>
.red-outline { border: 3px solid #cd0000; }
</style>