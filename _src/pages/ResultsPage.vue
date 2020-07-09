<template><div class="page">
  <h1>Results</h1>

  <button class="button" v-on:click="moveToCategoriesPage()">Go Back</button>

</div></template>

<script>
export default {
  name: 'CategoriesPage',
  methods: {
    show: function(e) {
      for (const p of document.getElementsByClassName('page')) {
        p.classList.remove('todo');
        p.classList.add('passed');
      }

      this.$el.classList.remove('todo', 'passed');
    },
    moveToCategoriesPage: function() {
      this.$parent.$refs.categoryPage.show();
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