<template>
 <v-container>

   <v-layout>
      <v-flex>

        <v-row justify="center">
          <v-col md="15" class="py-15">
            <v-row>
              <v-col cols="12" lg="5">
                <v-card class="text-center my-5" style="min-height: 500px;">
                  <v-progress-linear
                    v-model="solved_percent"
                    color="pink"
                  ></v-progress-linear>
                  <v-row class="pa-5">
                    <v-col>
                      <v-select dense autowidth return-object select csingle-line lass="pa-0 ma-0" :items="problem_items" v-model="problem_num" style="width: 100px;text-align: center" class="float-right"></v-select>
                    </v-col>

                    <v-col class="text-left">/ {{ available_problems.length }}</v-col>
                  </v-row>

                  <v-card-text>
                    <v-expand-transition>
                      <v-row justify="center" align="center">

                        <v-col md="2" sm="1" xs="1" class="px-3 py-15">
                           <v-btn text class="px-3 py-15" :disabled="!can_go_previous" @click="goPrev"><v-icon x-large>mdi-chevron-left</v-icon></v-btn>
                        </v-col>

                        <v-col v-if="!(problem.question_resource != null && (problem.question_resource.endsWith('.gif') || problem.question_resource.endsWith('.jpg')))">
                          <video width="100%" controls preload :src="get_public_attachment_url(problem.question_resource)"></video>
                        </v-col>
                        <v-col v-else>
                          <img width="100%" :src="get_public_attachment_url(problem.question_resource)">
                        </v-col>
                        <v-col v-else>
                          <v-progress-circular
                            indeterminate
                            color="black"
                          ></v-progress-circular>
                        </v-col>
                        <v-col md="2" sm="1" xs="1">
                           <v-btn text class="px-3 py-15" :disabled="!can_go_next" @click="goNext"><v-icon x-large>mdi-chevron-right</v-icon></v-btn>
                        </v-col>
                      </v-row>
                    </v-expand-transition>
                  </v-card-text>

                  <v-row justify="center" align="center">

                    <v-col class="px-10">
                      <v-btn class="my-3" block @click="$router.push('/home')">
                        문제선택 화면
                      </v-btn>
                    </v-col>
                  </v-row>

                </v-card>
              </v-col>
              <v-col cols="12" lg="7">
                <v-card class="my-5">
                  <v-row class="pa-5">
                    <v-col cols="auto">
                      <sign-video-tooltip :resourcePath="problem.question_sign"></sign-video-tooltip>
                    </v-col>
                    <v-col class="px-3">{{ problem.num }}. {{ problem ? '(' + problem.genre + ') ' + problem.question_text : '' }}</v-col>
                  </v-row>

                  <v-divider></v-divider>


                  <v-row class="py-5 px-10" justify="center" align="center">

                    <v-col cols="12" lg="12">
                      <word-select-form ref="word_select_form" v-if="problem.question_type == 'word-select'" :answer_selection.sync="problem.answer_selection" @onAnswerChanged="onAnswerChanged"></word-select-form>
                      <word-evaluation-form ref="word_evaluation_form" v-else-if="problem.question_type == 'word-evaluation'" @onAnswerChanged="onAnswerChanged"></word-evaluation-form>
                      <div v-else>잘못된 문제형식</div>
                    </v-col>

                  </v-row>
                  <v-row v-show="problem.user_input" class="pt-5 px-10" justify="center" align="center">
                    <v-col>
                      <v-text-field label="기타 (자유롭게 적어주세요)" v-model="answer_input"></v-text-field>
                    </v-col>
                  </v-row>
                  <v-divider class="my-10"></v-divider>
                  <v-row class="py-15 px-10" justify="center" align="center" v-show="problem.num == null">
                    <v-col class="text-center">
                      <v-progress-circular
                          indeterminate
                          color="black"
                      ></v-progress-circular>
                    </v-col>
                  </v-row>
                  <v-row class="py-5 text-center" justify="center" align="center" >
                    <v-col md="5">
                      <v-btn
                        block
                        elevation="2"
                        large
                        color="primary"
                        @click="submit"
                        :disabled="problem.num == null"
                      >{{ is_first_submit ? '제출' : '다시 제출' }}</v-btn>
                    </v-col>
                    <v-col md="5" v-show="!is_first_submit">
                      <v-btn
                        block
                        elevation="2"
                        large
                        v-if="can_go_next"
                        @click="goNext"
                        :disabled="problem.num == null"
                      >다음 문제로 <v-icon>chevron-right</v-icon></v-btn>
                      <v-btn
                        block
                        elevation="2"
                        large
                        v-else="can_go_next"
                        @click="$router.push('/home')"
                        :disabled="problem.num == null"
                      >홈으로</v-btn>
                    </v-col>
                  </v-row>
                </v-card>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>

import SignVideoTooltip from "@/components/SignVideoTooltip";
import WordSelectForm from "@/components/forms/WordSelectForm";
import WordEvaluationForm from "@/components/forms/WordEvaluationForm";

export default {
  name: "TypeOneProblem",
  components: { SignVideoTooltip, WordSelectForm, WordEvaluationForm },
  data () {
    return {
      problem_num: null,
      problem: {},
      available_problems: [],
      solved_problems: [],
      genre_list: {},

      start_time: null,
      is_first_submit: null,

      answer: null,
      answer_input: null,
    }
  },

  mounted() {
    if(this.$cookies.get('user_id') == null) {
      this.$router.push('/home')
    }

    this.get_problems()
  },
  watch: {
    problem_num: function(oldVar, newVar) {
      this.get_problems()
      this.get_problem()
      this.answer = null
      this.get_answer()

    },
    problem: function(oldVar, newVar) {
      // Time checking
      this.start_time = new Date()
    }
  },
  computed: {
    problem_index: function () {
      if(this.problem_num == null) return null
      return this.available_problems.indexOf(this.problem_num.value)
    },
    can_go_previous: function() {
      return this.problem_index > 0
    },
    can_go_next: function() {
      if(this.problem_index >= this.available_problems.length - 1) return false

      if(this.genre_list[this.problem_items[this.problem_index].value] != this.genre_list[this.problem_items[this.problem_index + 1].value]) {
          return false
        } else {
          return true
      }
    },
    solved_percent: function() {
      return this.solved_problems.length / this.available_problems.length * 100
    },
    problem_items: function() {
      let items = []
      let self = this
      this.available_problems.forEach(function(e) {
        let display = e
        if(self.solved_problems.includes(e)) {
          display += ' (제출됨)'
        }
        items.push({text: display, value: e})
      })

      return items
    }

  },
  methods: {
    get_problems: function() {
      axios.get(this.$utils.getApiUrl() + '/type1/problems', {
            params: {
              user_id: this.$cookies.get('user_id')
            }
      })
      .then((res) => {
        this.available_problems = res.data.available
        this.solved_problems = res.data.solved
        this.genre_list = res.data.genre

        let self = this

        try {
          if(this.problem_num == null) {
            if(this.$route.params.problem_num != null) {

              let l_problem = null
              this.problem_items.forEach(function(e) {
                if(e.value != self.$route.params.problem_num) {
                  return
                }
                l_problem = e
              })

              if(l_problem != null) {
                this.problem_num = l_problem
              } else {
                this.problem_num = this.problem_items[0]
              }

            } else {
              this.problem_num = this.problem_items[0]
            }
          }
        } catch (e) {
          console.log(e)
        }
        this.get_problem()
      })
      .catch((ex) => { console.log(ex); })

    },
    get_problem: function() {
      if(this.problem_num == null) return;

      this.answer_input = null
      this.problem = {}
      axios.get(this.$utils.getApiUrl() + '/type1/problems/' + this.problem_num.value)
      .then((res) => { this.problem = res.data; this.get_answer() })
      .catch((ex) => { console.log(ex); })

    },
     get_answer: function() {
       if (this.problem_num == null) return;

       this.is_first_submit = true

       axios.get(this.$utils.getApiUrl() + '/type1/problems/' + this.problem_num.value + '/answers', {
            params: {
              user_id: this.$cookies.get('user_id')
            }
          })
           .then((res) => {
              if(res.data == 'NA') return;

              if(this.problem.question_type == 'word-select') {
                this.$refs.word_select_form.set_value(res.data.answer)
              } else if(this.problem.question_type == 'word-evaluation') {
                this.$refs.word_evaluation_form.set_value(res.data.answer)
              }
              this.answer_input = res.data.answer_input
              this.is_first_submit = false

           })
           .catch((ex) => {
           })

     },
    get_public_attachment_url: function(file_name) {
      return this.$utils.getApiUrl() + '/attachments/' + file_name
    },
    onAnswerChanged: function(answer) {
      this.answer = answer
    },
    submit: function () {
        axios.post(this.$utils.getApiUrl() + '/type1/problems/' + this.problem_num.value + '/answers', {
            user_id: this.$cookies.get('user_id'),
            answer: this.answer,
            answer_input: this.answer_input,
            elapse_time: (new Date()).getTime() - this.start_time.getTime()
          })
          .then((res) => {
            this.get_problems()
          })
          .catch((ex) => { alert('에러발생!\n' + ex); })

    },

    goPrev: function() {
      this.problem_num = this.problem_items[this.problem_index - 1]
    },
    goNext: function() {
      this.problem_num = this.problem_items[this.problem_index + 1]
    }
  }
}
</script>

<style scoped>

</style>