<template>
  <v-container>
    <v-layout>
      <v-flex>
        <v-row justify="center">
          <v-col md="8">
            <v-card
              elevation="1"
              class="pa-3 my-5"
            >
              <v-card-title>실험 안내</v-card-title>

              <v-card-text>
                <v-row>
                  <v-col justify="center" align="center">
                    <video ref="intro_video" @ended="onVideoEnded" :src="introduction_video" controls></video>
                  </v-col>

                </v-row>
              </v-card-text>

              <v-card-text v-html="exp_description" class="py-7"></v-card-text>

                <v-row>
                  <v-col justify="center" align="right">
                    <v-btn @click="moveRegister" class="my-4" depressed large>다음 단계로<div v-show="showPing" class="ping"></div></v-btn>
                  </v-col>
                </v-row>
            </v-card>

          </v-col>
        </v-row>
        <v-row>
          <v-col>

          </v-col>
        </v-row>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  name: "Introduction",
  data: () => ({
    exp_description: '불러오는 중...',
    showPing: false,
  }),
  computed: {
    introduction_video: function () {
      return this.$utils.getApiUrl() + '/attachments/introduction.mp4'
    }
  },
  mounted() {
    let self = this
    if(this.$cookies.get('user_id') != null) {
      this.$router.push('/home')
    }

    axios.get(this.$utils.getApiUrl() + '/experiment-desc')
      .then((res) => { this.exp_description = res.data })
      .catch((ex) => { console.log('Connection error', ex); })


    setTimeout(function() {
      self.$refs.intro_video.play()
    }, 3000)


  },
  methods: {
    moveRegister: function() {
      this.$router.push('/register')
    },
    onVideoEnded: function () {
      this.showPing = true
    }
  }
}
</script>

<style scoped>

</style>