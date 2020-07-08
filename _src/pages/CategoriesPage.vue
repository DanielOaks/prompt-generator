<template><div class="page">
  <h1>Categories Page</h1>

  <button class="button" v-on:click="moveToHomePage()">Go Home</button>

</div></template>

<script>
export default {
  name: 'CategoriesPage',
  methods: {
    show: function(e) {
      for (const p of document.getElementsByClassName('page')) {
        p.classList.add('todo');
      }
      const hp = this.$parent.$refs.homePage.$el;
      hp.classList.remove('todo');
      hp.classList.add('passed');

      this.$el.classList.remove('todo', 'passed');
    },
    moveToHomePage: function() {
      this.$parent.$refs.homePage.show();
    },
  },
}
</script>

<style lang="scss" scoped>
$gray: darkslategrey;
h1 {
  color: $gray;
  font-size: 1.5rem;
}
</style>