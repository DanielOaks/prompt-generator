<template><div class="page">
  <h1>Categories Page</h1>

  <button class="button" v-on:click="moveToHomePage()">Go Home</button>

  <button class="button" v-on:click="moveToCategoryPage(id)" v-for="(info, id) in $root.setup.categories" v-bind:key="id">{{ info.name }}</button>

</div></template>

<script>
export default {
  name: 'CategoriesPage',
  methods: {
    show: function(e) {
      for (const p of document.getElementsByClassName('page')) {
        p.classList.remove('passed');
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
    moveToCategoryPage: function(id) {
      this.$root.$data.current_category = id;

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