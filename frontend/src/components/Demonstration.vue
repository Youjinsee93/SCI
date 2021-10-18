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
                    <video ref="demo_video" @ended="onVideoEnded" :src="introduction_video" controls></video>
                  </v-col>

                </v-row>
              </v-card-text>

              <v-row>
                <v-col justify="center" align="right">
                  <v-btn @click="moveHome" class="my-4" depressed large>설문 시작하기<div v-show="showPing" class="ping"></div></v-btn>
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
  name: "Demonstration",
  data: () => ({
    showPing: false,
  }),
  computed: {
    introduction_video: function () {
      return this.$utils.getApiUrl() + '/attachments/demonstration.mp4'
    }
  },
  mounted() {
    let self = this
    if(this.$cookies.get('user_id') == null) {
      this.$router.push('/register')
    }

    setTimeout(function() {
      if(self.$refs.demo_video != null) {
        self.$refs.demo_video.play()
      }
    }, 3000)


  },
  methods: {
    moveHome: function() {
      this.$router.push('/home')
    },
    onVideoEnded: function () {
      this.showPing = true
    }
  }
}
</script>

<style scoped>

</style>