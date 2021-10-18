<script src="../main.js"></script>
<template>
  <v-container>
   <v-layout>
      <v-flex>

        <v-row justify="center">
          <v-col md="8" class="py-15">

            <v-card class="text-center my-5">
              <v-progress-linear
                v-model="solved_percent"
                color="pink"
              ></v-progress-linear>
              <v-row class="mt-2">
                <v-col>
                  <v-select dense autowidth return-object select csingle-line :items="problem_items" v-model="problem_num" style="width: 100px;text-align: center" class="float-right"></v-select>
                </v-col>

                <v-col class="text-left">/ {{ available_problems.length }}</v-col>
              </v-row>
            </v-card>

            <v-stepper v-model="e1">
              <v-stepper-header>
                <v-stepper-step
                  :complete="e1 > 1"
                  step="1"
                >
                  감정 선택
                </v-stepper-step>

                <v-divider></v-divider>

                <v-stepper-step
                  :complete="e1 > 2"
                  step="2"
                >
                  감정 설문
                </v-stepper-step>

                <v-divider></v-divider>

                <v-stepper-step step="3">
                  설문 완료
                </v-stepper-step>
              </v-stepper-header>
              <v-stepper-items>
                <v-stepper-content step="1">

                  <v-item-group class="my-10" v-model="emotion">
                    <v-container>
                      <v-row>
                        <v-col
                          v-for="e in emotion_option"
                          :key="e"
                          md="3"
                        >
                          <v-item v-slot="{ active, toggle }">
                            <v-card
                              :color="active ? '#FFF2CC' : '#FFF2CC'"
                              :class="{'red-outline': emotion == e}"
                              class="d-flex align-center"

                              height="100"
                              @click="e1 = 2;emotion=e"

                            >
                              <div class="flex-grow-1 text-center">
                                  {{ e }}
                              </div>

                            </v-card>
                          </v-item>
                        </v-col>
                      </v-row>
                    </v-container>
                  </v-item-group>

                </v-stepper-content>

                <v-stepper-content step="2">
                  <v-container class="my-10">
                    <v-row>
                      <v-col class="display-1">{{ emotion }}에 대한 설문</v-col>
                    </v-row>

                    <v-row>
                      <v-col class="">1. '{{ emotion }}'에 대해 얼마나 이해하고 있나요?</v-col>
                    </v-row>
                    <v-slider
                        class="my-10"
                        v-model="slider"
                        :max="10"
                        step="1"
                        thumb-label="always"
                        :tick-labels="satisfactionEmojis"
                    ></v-slider>

                    <v-row>
                      <v-col class="">2. '{{ emotion }}'에 대한 개인적인 의견 또는 생각나는 에피소드를 자유롭게 써주세요</v-col>
                    </v-row>
                    <v-textarea class="my-3" solo v-model="episode_text">
                    </v-textarea>

                    <v-row>
                      <v-col class="">3. '{{ emotion }}'과 관련된 그림을 선택해주세요.</v-col>
                    </v-row>


                    <v-item-group class="" v-model="image_selected">
                      <v-container>
                        <v-row>
                          <v-col
                            v-for="io in image_option"
                            :key="io"
                            md="4"
                          >
                            <v-item v-slot="{ active, toggle }">

                              <v-card
                                  v-if="io.endsWith('.gif') || io.endsWith('.jpg')"
                                  :class="{'red-outline': active}"
                                  class="d-flex align-center overflow-hidden"
                                  height="150"
                                  @click="toggle"
                                  style="background-size:contain;background-position:center;"
                                  :style="{backgroundImage: 'url(' + get_public_attachment_url(io) + ')'}">

                              </v-card>
                              <v-card
                                v-else
                                :class="{'red-outline': active}"
                                class="d-flex align-center overflow-hidden"

                                height="150"
                                @click="toggle">
                                <video width="100%" controls preload :src="get_public_attachment_url(io)"></video>
                              </v-card>
                            </v-item>
                          </v-col>
                        </v-row>
                      </v-container>
                    </v-item-group>


                  </v-container>

                  <v-btn
                    color="primary"
                    class="float-right"
                    @click="submit"
                  >
                    {{ is_first_submit ? '제출' : '다시 제출' }}
                  </v-btn>

                  <v-btn @click="e1 = 1;emotion=null" text>
                    다시 선택하기
                  </v-btn>
                </v-stepper-content>

                <v-stepper-content step="3">

                  <v-container class="text-center my-15">
                    <v-row>
                      <v-col>
                        설문에 응답해주셔서 감사합니다.
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col>
                        <v-btn class="px-3" v-if="can_go_next" @click="goNext" color="primary">다음 문제로</v-btn>
                        <v-btn class="px-3" v-else @click="$router.push('/home')" color="primary">홈으로</v-btn>
                      </v-col>
                    </v-row>
                  </v-container>
                </v-stepper-content>
              </v-stepper-items>
            </v-stepper>
        </v-col>
      </v-row>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  name: "Proto1",
  computed: {
    problem_index: function () {
      if(this.problem_num == null) return null
      return this.available_problems.indexOf(this.problem_num.value)
    },
    can_go_next: function() {
      return this.problem_index < this.available_problems.length - 1
    },
    solved_percent: function() {
      return this.solved_problems.length / this.available_problems.length * 100
    },
    emotion_option: function() {

      if(this.problem != null) {
        try {
          return this.problem.emotion_select.split(';')
        } catch(e) {
          return []
        }
      } else {
        return []
      }
    },
    image_option: function() {
      if(this.problem != null) {
        try {
          return this.problem.image_select.split(';')
        } catch(e) {

        }
      } else {
        return []
      }
    },
    image_selected_text: function() {
      return this.image_option[this.image_selected]
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
  mounted() {
    if(this.$cookies.get('user_id') != null) {
      // Already Login
      this.$router.push('/' + this.$cookies.get('user_id') + '/proto1')
    } else {
      this.$router.push('/')
    }


    this.get_problems()
  },
  watch: {
    problem_num: function(oldVar, newVar) {
      this.get_problems()
      this.get_problem()
      this.get_answer()

      this.e1 = 1

    },
    problem: function(oldVar, newVar) {
      // Time checking
      this.start_time = new Date()
    }
  },
  data () {
      return {
        problem_num: null,
        problem: {},
        available_problems: [],
        solved_problems: [],

        start_time: null,
        is_first_submit: false,
        e1: 1,
        emotion: null,
        episode_text: null,
        image_selected:null,
        satisfactionEmojis: ['😭', '😢', '☹️', '☹️', '🙁', '😐', '🙂', '😊', '😁', '😄', '😍'],
        slider: 50,
    }
  },
   methods: {
     get_problems: function () {
       axios.get(this.$utils.getApiUrl() + '/proto1/problems', {
            params: {
              user_id: this.$cookies.get('user_id')
            }
          }).then((res) => {
             this.available_problems = res.data.available
             this.solved_problems = res.data.solved

             try {
               if (this.problem_num == null) {
                 this.problem_num = this.problem_items[0]
               }
             } catch (e) {
               console.log(e)
             }
           })
           .catch((ex) => {
             console.log(ex);
           })

     },
     get_problem: function () {
       if (this.problem_num == null) return;

       this.problem = {}
       axios.get(this.$utils.getApiUrl() + '/proto1/problems/' + this.problem_num.value)
           .then((res) => {
             this.problem = res.data.problem
           })
           .catch((ex) => {
           })

     },
     get_answer: function() {
       if (this.problem_num == null) return;

        this.emotion = null
        this.episode_text = null
        this.image_selected = null
        this.slider = 5

        this.is_first_submit = true

       axios.get(this.$utils.getApiUrl() + '/proto1/problems/' + this.problem_num.value + '/answers', {
            params: {
              user_id: this.$cookies.get('user_id')
            }
          })
           .then((res) => {

              this.emotion = res.data.emotion
              this.episode_text = res.data.episode_text

              if(res.data.image_selected != null) {
                const idx = this.image_option.indexOf(res.data.image_selected)
                if(idx != -1) {
                  this.image_selected = idx
                }
              }
              this.slider = res.data.slider

              this.is_first_submit = false
           })
           .catch((ex) => {
             console.log(ex)
           })

     },
     get_public_attachment_url: function (file_name) {
       return this.$utils.getApiUrl() + '/attachments/' + file_name
     },
     submit: function () {
        axios.post(this.$utils.getApiUrl() + '/proto1/problems/' + this.problem_num.value + '/answers', {
            user_id: this.$cookies.get('user_id'),
            answer: {
              emotion: this.emotion,
              episode_text: this.episode_text,
              image_selected: this.image_selected_text,
              slider: this.slider,
            },
            elapse_time: (new Date()).getTime() - this.start_time.getTime()
          })
          .then((res) => {
            this.e1 = 3
            this.get_problems()
          })
          .catch((ex) => { alert('에러발생!\n' + ex); })
     },
     goNext: function() {
      this.problem_num = this.problem_items[this.problem_index + 1]
    }
   }
}
</script>

<style scoped>
.red-outline { border: 3px solid #cd0000 !important; }
</style>