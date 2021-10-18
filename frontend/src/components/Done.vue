<script src="../main.js"></script>
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
              <v-card-title>설문 완료</v-card-title>

              <v-card-text>
                <v-row>
                  <v-col justify="center" align="center">
                    <video ref="demo_video" @ended="onVideoEnded" :src="done_video" controls></video>
                  </v-col>

                </v-row>
              </v-card-text>

              <v-row>
                <v-col justify="center" align="right">
                  <v-btn @click="moveHome" class="my-4" depressed large>완료<div v-show="showPing" class="ping"></div></v-btn>
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
  name: "Done",
  data: () => ({
    showPing: false,
  }),
  computed: {
    done_video: function () {
      return this.$utils.getApiUrl() + '/attachments/done.mp4'
    }
  },
  mounted() {
    let self = this
    if(this.$cookies.get('user_id') == null) {
      this.$router.push('/')
    }

    setTimeout(function() {
      if(self.$refs.demo_video != null) {
        self.$refs.demo_video.play()
      }
    }, 3000)


  },
  methods: {
    moveHome: function() {
      this.$cookies.remove('user_id');
      this.$cookies.remove('name');
      window.location.reload()
    },
    onVideoEnded: function () {
      this.showPing = true
    }
  }
}
</script>

<style scoped>

</style>