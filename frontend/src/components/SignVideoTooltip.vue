<template>
  <div class="icon" v-tooltip="{
      content: isMouseHovered ? tooltipContent : '',
      show: showTooltip,
      offset: 10,
      placement: 'auto',
      autoHide: false,
    }"
       @mouseover="onMouseIn"
       @mouseout="onMouseOut"
  >
  </div>
</template>

<script>
export default {
  name: "SignVideoTooltip",
  props: ['resourcePath'],
  data() {
    return {
      showTooltip: true,
      isMouseHovered: false
    }
  },
  computed: {
    videoUrl: function () {
      if (this.resourcePath) {
        return this.get_public_attachment_url(this.resourcePath)
      } else {
        return null
      }
    },
    tooltipContent: function() {
      return '<video src="' + this.videoUrl  +'" width="300px" autoplay loop>'
    }
  },
  methods: {
    get_public_attachment_url: function (file_name) {
      return this.$utils.getApiUrl() + '/attachments/' + file_name
    },
    onMouseIn: function() {
      this.isMouseHovered = true
    },
    onMouseOut: function() {
      this.isMouseHovered = false
    }
  }

}

</script>

<style scoped>
.icon {
  width: 30px;
  height: 30px;
  background-repeat: no-repeat;
  background-position: right;
  background-size: contain;
  background-image: url('./assets/sign-icon.png');
  cursor: pointer
}
.icon:hover {
  opacity: 0.9;
}

</style>