<template><div class="page"><div>
  <h1>Prompts</h1>
  <h2 v-if="$root.setup.categories[$root.current_category]">{{$root.setup.categories[$root.current_category].name}}</h2>

  <button class="button smol" v-on:click="moveToCategoriesPage()">Go Back</button>

  <h3 v-for="(char, id) in $root.$data.charsToDisplay" v-bind:key="id">{{ char.name }}</h3>

  <button class="button regen" v-on:click="generateResults()">Regenerate</button>

</div></div></template>

<script>
var uniqueChars = 0;
var randomCharWeightUpperLimit = 0;
var charList = [];

export default {
  name: 'ResultsPage',
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
    generateCaches: function() {
      console.log('generating caches \o/');

      const cat = this.$parent.$data.current_category;
      if (!this.$parent.$data.setup.categories[cat]) {
        return
      }

      // characters first
      var paths = this.$parent.$data.setup.categories[cat].characters;

      uniqueChars = 0;
      randomCharWeightUpperLimit = 0;
      charList = [];

      for (const path of paths) {
        if (!this.$jsonPointer.has(this.$parent.$data.data, '/' + path)) {
          continue;
        }

        const set = this.$jsonPointer.get(this.$parent.$data.data, '/' + path);
        if (set && set.characters) {
          console.log('loading characters in set', set.name);

          for (var character of set.characters) {
            if (typeof character === 'string') {
              character = {
                name: character,
                weight: 1,
                description: '',
              };
            }

            charList.push(character)
            uniqueChars += 1;
            randomCharWeightUpperLimit += character.weight;
          }
        }
      }

      console.log('generated characters:', uniqueChars, randomCharWeightUpperLimit, charList);
      

      console.log(this.$parent.$data.setup.categories[cat].locations);

      console.log('building happens here!');
    },
    generateResults: function() {
      this.$root.$data.charsToDisplay = [];

      const charsToGenerate = Math.min(uniqueChars, this.$root.$data.generate_characters);
      for (let i = 0; i < charsToGenerate; i++) {
        var regenerateChar = false;
        var weightToGo = Math.random() * randomCharWeightUpperLimit;
        for (const char of charList) {
          if (weightToGo <= char.weight) {
            if (this.$root.$data.charsToDisplay.includes(char)) {
              regenerateChar = true;
              break;
            }

            this.$root.$data.charsToDisplay.push(char);
            break;
          }

          weightToGo -= char.weight;
        }
        if (regenerateChar) {
          i -= 1;
        }
      }
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
  color: rgb(221, 230, 243);
  font-size: 2.25rem;
  text-align: center;
  padding: 1em 0 0;
}
.regen {
  margin-top: 2.5em;
}
</style>