<template><div class="page">
  <h1>Category Page</h1>
  <h2>{{$root.current_category}}</h2>

  <button class="button" v-on:click="moveToCategoriesPage()">Go Back</button>
  <button class="button" v-on:click="moveToResultsPage()">Generate</button>

</div></template>

<script>
export default {
  name: 'CategoryPage',
  methods: {
    show: function(e) {
      for (const p of document.getElementsByClassName('page')) {
        p.classList.remove('passed');
        p.classList.add('todo');
      }
      const hp = this.$parent.$refs.homePage.$el;
      hp.classList.remove('todo');
      hp.classList.add('passed');
      const cp = this.$parent.$refs.categoriesPage.$el;
      cp.classList.remove('todo');
      cp.classList.add('passed');

      this.$el.classList.remove('todo', 'passed');
    },
    moveToCategoriesPage: function() {
      this.$parent.$refs.categoriesPage.show();
    },
    moveToResultsPage: function() {
      this.$parent.$refs.resultsPage.show();
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