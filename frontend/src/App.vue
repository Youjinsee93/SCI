<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <span @click="$router.push('/')" style="cursor:pointer">Emotion Survey</span>
      </div>

      <v-spacer></v-spacer>

      <div v-show="name != null">
        <span class="mx-3">{{ name }}</span>
        <v-btn color="error" @click="logout">설문종료</v-btn>
      </div>
    </v-app-bar>

    <v-main>
      <router-view></router-view>


    </v-main>


  </v-app>
</template>

<script>

export default {
  name: 'App',
  data: () => ({
    user_id: null,
    name: null,
  }),
  mounted() {
    this.user_id = this.$cookies.get('user_id')
    this.name = this.$cookies.get('name');
  },
  methods: {
    logout: function() {
      this.$cookies.remove('user_id');
      this.$cookies.remove('name');
      window.location.reload()
    }
  }

};
</script>
