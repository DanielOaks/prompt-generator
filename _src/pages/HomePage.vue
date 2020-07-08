<template><div class="page">
  <h1>Home Page</h1>

  <button class="button" v-on:click="moveToCategoriesPage()">Goto Categories</button>
  
</div></template>

<script>
export default {
  name: 'HomePage',
  methods: {
    show: function(e) {
      for (const p of document.getElementsByClassName('page')) {
        p.classList.add('todo');
      }
      this.$el.classList.remove('todo', 'passed');
    },
    moveToCategoriesPage: function() {
      this.$parent.$refs.categoriesPage.show();
    },
  },
}
</script>

<style lang="scss" scoped>
$gray: darkslategrey;
h1 {
  color: $gray;
  font-size: 2rem;
}
</style>