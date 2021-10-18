<template>
  <div>
    <v-row>
      <v-col class="">1. 선택한 감정에 대한 강도를 선택해주세요.</v-col>
    </v-row>

    <v-slider
        class="my-10"
        v-model="l_answer.strength"
        :max="10"
        step="1"
        thumb-label="always"
        :tick-labels="strengthLabel"
    ></v-slider>

    <v-row>
      <v-col class="">2. 선택한 감정이 부정적인지, 긍정적인지에 대하여 선택해주세요.</v-col>
    </v-row>

    <v-row>
    <v-slider
        class="my-10"
        v-model="l_answer.positive"
        :max="10"
        step="1"
        thumb-label="always"
        :tick-labels="positionLabel"
    ></v-slider>
    </v-row>


    <v-row>
      <v-col class="">3. 선택한 감정이 차분한 느낌인지, 활발한 느낌인지에 대하여 선택해주세요</v-col>
    </v-row>

    <v-row>
    <v-slider
        class="my-10"
        v-model="l_answer.activity"
        :max="10"
        step="1"
        thumb-label="always"
        :tick-labels="activityLabel"
    ></v-slider>
    </v-row>
  </div>
</template>

<script>
import SignVideoTooltip from "@/components/SignVideoTooltip";

export default {
  name: "WordEvaluationForm",
  components: { SignVideoTooltip },
  data () {
    return {
      strengthLabel: ['약함', '1', '2', '3️', '4️', '5', '6', '7', '8', '9', '강함'],
      positionLabel: ['부정적', '😢', '☹️', '☹️', '🙁', '😐', '🙂', '😊', '😁', '😄', '긍정적'],
      activityLabel: ['차분함', '1', '2', '3️', '4️', '5', '6', '7', '8', '9', '활발함'],

      l_answer: {
        strength: 5,
        positive: 5,
        activity: 5,
      },
    }
  },
  watch: {
    'l_answer': {
        handler: function (val, oldVal) {
          this.$emit('onAnswerChanged', val)
        },
        deep: true
    }
  },
  computed: {
  },
  methods: {
    set_value: function(val) {
      if(val == null) return;
      this.l_answer = val

    },
  }
}
</script>

<style scoped>
.default-outline {  border: 3px solid transparent !important; }
.red-outline { border: 3px solid #cd0000 !important; }
</style>