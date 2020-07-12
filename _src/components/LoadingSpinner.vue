<template><div class="whole-page-covering">
  <p>loading...</p>

</div></template>

<script>
export default {
  name: 'LoadingSpinner',
  methods: {
    hide: function(e) {
      this.$el.classList.add('hidden');
    },
  },
}
</script>

<style lang="scss" scoped>
.whole-page-covering {
  position: absolute;
  z-index: 99;
  left: 0;
  top: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(51,51,51,0.85);
  opacity: 1;
  color: #fff;
  transition: opacity 0.1s ease-in-out;
  display: flex;
  align-items: center;
  &.hidden {
    opacity: 0;
    pointer-events: none;
  }
  > p {
    margin: 0 auto;
  }
}
</style>