<template><div class="page"><div>
  <h1>Prompts</h1>

  <button class="button" v-on:click="moveToCategoryPage(id)" v-for="(info, id) in $root.setup.categories" v-bind:key="id">{{ info.name }}</button>

</div></div></template>

<script>
export default {
  name: 'CategoriesPage',
  methods: {
    show: function(e) {
      for (const p of document.getElementsByClassName('page')) {
        p.classList.add('todo');
        p.classList.remove('passed');
      }
      this.$el.classList.remove('todo', 'passed');
    },
    moveToCategoryPage: function(id) {
      this.$root.$data.current_category = id;

      this.$parent.$refs.categoryPage.show();
    },
  },
}
</script>

<style lang="scss" scoped>
h1 {
  color: #fff;
  font-size: 2.5rem;
  text-align: center;
  padding: 0 0 .5em;
}
</style>