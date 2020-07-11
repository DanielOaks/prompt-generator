<template><div class="page"><div>
  <h1>Prompts</h1>
  <h2 v-if="$root.setup.categories[$root.current_category]">{{$root.setup.categories[$root.current_category].name}}</h2>

  <button class="button" v-on:click="moveToCategoriesPage()">Go Back</button>

</div></div></template>

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
    generateResults: function() {

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
h2 {
  color: #eef8ff;
  font-size: 1rem;
  text-align: center;
  padding: 0 0 0.8em;
  margin-top: -.8em;
}
</style>