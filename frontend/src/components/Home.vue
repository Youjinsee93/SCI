<template>
  <v-container>

   <v-layout>
      <v-flex>

        <v-row justify="center">
          <v-col md="8" class="py-15">

            <v-card class="text-center pa-5">
              <v-row class="py-5">
                <v-col>
                  <v-row>
                    <v-col>
                      <span>전체 진행률</span>
                    </v-col>
                    <v-col>
                      {{ solved_problems_1.length }} / {{ available_problems_1.length }} ({{ parseInt(solved_problems_1.length / available_problems_1.length * 100) }}%)
                    </v-col>
                  </v-row>
                </v-col>
              </v-row>

              <v-row>
                <v-col
                 v-for="(zip, index) in zipped_problems"
                      :key="'z'+index"
                      cols="4"
                      md="3"
                >
                    <v-card
                      class="d-flex align-center default-outline py-4 category-box"
                      style="cursor:pointer;"
                      :class="{'highlight': (index == 0 && solved_problems_1.length == 0 && category_selected_idx == null),
                                'selected': (category_selected_idx == index),
                                'solved': (getSolvedCount(zip.problem) == zip.problem.length)}"
                      @click="category_selected_idx = index"
                    >
                      <span class="text-center mx-auto ">
                        <span>{{ zip.category }}</span>
                        <span style="font-size:0.8em;"><br>( {{ getSolvedCount(zip.problem) }} / {{zip.problem.length }})</span>

                      </span>

                    </v-card>
                </v-col>
              </v-row>


              <div  v-show="category_selected_idx != null">
                <v-divider class="my-5"></v-divider>
                <v-row>
                  <v-col
                        v-for="(problem, index) in display_problems"
                        :key="'p'+index"
                        cols="4"
                        md="3"
                      >

                    <v-col>

                      <v-card
                        class="d-flex align-center default-outline py-2 problem-box"
                        style="cursor:pointer;"
                        :class="{'solved': solved_problems_1.includes(problem), 'highlight': (index == 0 && solved_problems_1.length == 0)}"
                        @click="moveToTypeOneProblem(problem)"
                      >
                        <span class="text-center mx-auto ">{{ problem }}번
                          <span style="font-size:0.8em;" v-if="solved_problems_1.includes(problem)"><br>(완료)</span>
                          <span style="font-size:0.8em;" v-else><br>(미완료)</span>
                        </span>

                      </v-card>

                    </v-col>

                  </v-col>

                </v-row>
              </div>
            </v-card>


            <v-card class="text-center pa-5 mt-5" v-show="solved_problems_1.length == available_problems_1.length">
              <v-row class="py-1">
                <v-col>
                  <v-btn
                    depressed
                    color="primary"
                    @click="$router.push('/done')"
                  ><div v-show="true" class="ping"></div>
                    설문을 완료하였다면 클릭해주세요
                  </v-btn>
                </v-col>
              </v-row>
            </v-card>

          </v-col>
        </v-row>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  name: "Home",
  data () {
    return {
      available_problems_1: [],
      solved_problems_1: [],
      genre_list: [],

      category_selected_idx: null
    }
  },
  computed: {
    zipped_problems: function() {
      let output = []
      let previousGenre = null
      let self = this

      this.available_problems_1.forEach(function(e) {
        let genre = self.genre_list[e]

        if(genre != previousGenre) {
          output.push({category: genre, problem: []})
        }

        output[output.length - 1].problem.push(e)

        previousGenre = genre
      })

      return output
    },
    display_problems: function() {
      if(this.category_selected_idx == null) return []

      return this.zipped_problems[this.category_selected_idx].problem
    },

  },

  mounted() {
    if(this.$cookies.get('user_id') != null) {
      // Already Login
    } else {
      this.$router.push('/')
    }


     axios.get(this.$utils.getApiUrl() + '/type1/problems', {
            params: {
              user_id: this.$cookies.get('user_id')
            }
          }).then((res) => {
           this.available_problems_1 = res.data.available
           this.solved_problems_1 = res.data.solved
           this.genre_list = res.data.genre

         })
  },
  methods: {
    moveToTypeOneProblem: function (num) {
      this.$router.push('/' + this.$cookies.get('user_id') + '/type1/' + num)
    },
    getSolvedCount: function(problems) {
      if(this.solved_problems_1.length == 0) {
        return 0
      }

      let cnt = 0
      let self = this
      problems.forEach(function(e) {
        if(self.solved_problems_1.includes(e)) {
          cnt += 1
        }
      })
      return cnt
    }
  }

}
</script>

<style scoped>
.category-box { background-color: #b5efe6; border: 2px solid transparent; }
.category-box.selected { border:2px solid #ff3e3e; }
.category-box.solved { background-color: lightgray; opacity:0.5; }
.category-box.highlight {
    background: rgb(211, 211, 211);
    animation: load 1.0s cubic-bezier(0.25, 0.25, 0.75, 0.75) infinite;
}

.problem-box { background-color: #eaefb5; }
.problem-box.solved { background-color: lightgray; opacity:0.5; }
.problem-box.highlight {
    background: rgb(211, 211, 211);
    animation: load 1.0s cubic-bezier(0.25, 0.25, 0.75, 0.75) infinite;
}

@keyframes load {
    0% {
        background: rgb(211, 211, 211);
    }
    50% {
        background: rgb(255, 117, 117);
    }
    100% {
        background: rgb(211, 211, 211);
    }
}
</style>