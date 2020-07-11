<template><div class="page"><div>
  <h1>Prompts</h1>
  <h2 v-if="$root.setup.categories[$root.current_category]">{{$root.setup.categories[$root.current_category].name}}</h2>

  <button class="button smol" v-on:click="moveToCategoriesPage()">Go Back</button>

  <label for="characters"><h3>Characters</h3></label>
  <div class="number-display-line">
  <button class="button" v-on:click="adjustchars(-1)">-</button>
  <span class="number-display" id="characters">{{$root.generate_characters}}</span>
  <button class="button" v-on:click="adjustchars(+1)">+</button>
  </div>

  <div class="checkbox-line">
  <input id="locations" v-model="$root.generate_location" type="checkbox">
  <label for="locations">Generate Location</label>
  </div>

  <button class="button" v-on:click="moveToResultsPage()">Generate</button>

</div></div></template>

<script>
export default {
  name: 'CategoryPage',
  methods: {
    show: function(e) {
      for (const p of document.getElementsByClassName('page')) {
        p.classList.add('todo');
        p.classList.remove('passed');
      }
      const cp = this.$parent.$refs.categoriesPage.$el;
      cp.classList.remove('todo');
      cp.classList.add('passed');

      this.$el.classList.remove('todo', 'passed');
    },
    adjustchars: function(num) {
      this.$root.$data.generate_characters = Math.max(0, this.$root.$data.generate_characters + num);
    },
    moveToCategoriesPage: function() {
      this.$parent.$refs.categoriesPage.show();
    },
    moveToResultsPage: function() {
      //this.$parent.$refs.resultsPage.generate();
      this.$parent.$refs.resultsPage.show();
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
h3 {
  color: #fff;
  font-size: 1.5rem;
  text-align: center;
  padding: 1em 0 .5em;
}
.number-display-line {
  text-align: center;
  margin-bottom: 1em;
  .button {
    display: inline-block;
  }
  span {
    font-size: 2em;
    padding: 0 .6em;
    color: #fff;
  }
}
.checkbox-line {
  text-align: center;
  color: #fff;
  margin-bottom: 1em;
}

</style>