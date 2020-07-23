<template><div class="page"><div>
  <h1>Prompts</h1>
  <h2 v-if="$root.setup.categories[$root.current_category]">{{$root.setup.categories[$root.current_category].name}}</h2>

  <div class="buttonList">
    <button class="button smol" v-on:click="moveToCategoriesPage()">Go Back</button>
    <button class="button smol" v-on:click="generateResults()">Regenerate</button>
  </div>

  <div v-for="(char, id) in $root.$data.charsToDisplay" v-bind:key="'c'+id">
    <h3 v-html="escapeHtml(char.name).replace('\n', '<br>')"></h3>
    <div class="descLine" v-if="char.description || char.img">
      <div class="img"><img v-if="char.img" :src="'/img/chars/' + char.img"/></div>
      <div class="desc"><p v-if="char.description" v-html="char.description"></p></div>
    </div>
  </div>

  <div v-for="(location, id) in $root.$data.locationsToDisplay" v-bind:key="'l'+id">
    <h3 v-html="escapeHtml(location.name).replace('\n', '<br>')"></h3>
    <div class="categoryName" v-if="location.categoryName" v-html="escapeHtml(location.categoryName).replace('\n', '<br>')"></div>
    <div class="descLine" v-if="location.description || location.img">
      <div class="img"><img v-if="location.img" :src="'/img/locations/' + location.img"/></div>
      <div class="desc"><p v-if="location.description" v-html="location.description"></p></div>
    </div>
  </div>

<div v-if="$root.setup.categories[$root.current_category]"><p class="footer" v-if="$root.setup.categories[$root.current_category].disclaimer" v-html="$root.setup.categories[$root.current_category].disclaimer"></p></div>

</div></div></template>

<script>
var uniqueLocations = 0;
var randomLocationsWeightUpperLimit = 0;
var locationList = [];

var uniqueChars = 0;
var randomCharWeightUpperLimit = 0;
var charList = [];

export default {
  name: 'ResultsPage',
  methods: {
    escapeHtml: function(html) {
      var text = document.createTextNode(html);
      var p = document.createElement('p');
      p.appendChild(text);
      return p.innerHTML;
    },
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
    parseRandomList: function(typeOfItem, paths, imagesRequired) {
      var uniqueItems = 0;
      var randomItemWeightUpperLimit = 0;
      var itemList = [];

      for (const path of paths) {
        if (!this.$jsonPointer.has(this.$parent.$data.data, '/' + path)) {
          continue;
        }

        const set = this.$jsonPointer.get(this.$parent.$data.data, '/' + path);
        if (set && set[typeOfItem]) {
          console.log('loading', typeOfItem, 'in set', set.name);

          const categoryName = set['displayed-name'];

          for (var item of set[typeOfItem]) {
            if (typeof item === 'string') {
              item = {
                name: item,
                weight: 1,
                description: '',
              };
            }

            if (imagesRequired && !item.img) {
              continue;
            }

            if (categoryName) {
              item['categoryName'] = categoryName;
            }

            itemList.push(item)
            uniqueItems += 1;
            randomItemWeightUpperLimit += item.weight || 1;
          }
        }
      }

      return {
        'uniqueItems': uniqueItems,
        'randomItemWeightUpperLimit': randomItemWeightUpperLimit,
        'itemList': itemList,
      }
    },
    generateCaches: function() {
      console.log('generating caches \o/');

      const cat = this.$parent.$data.current_category;
      if (!this.$parent.$data.setup.categories[cat]) {
        return
      }

      // locations
      var paths = this.$parent.$data.setup.categories[cat].locations;
      var imagesRequired = false;

      var info = this.parseRandomList('locations', paths, imagesRequired);
      uniqueLocations = info.uniqueItems
      randomLocationsWeightUpperLimit = info.randomItemWeightUpperLimit
      locationList = info.itemList

      console.log('generated locations:', uniqueLocations, randomLocationsWeightUpperLimit, locationList);

      // characters
      paths = this.$parent.$data.setup.categories[cat].characters;
      imagesRequired = this.$parent.$data.character_images_required;

      info = this.parseRandomList('characters', paths, imagesRequired);
      uniqueChars = info.uniqueItems
      randomCharWeightUpperLimit = info.randomItemWeightUpperLimit
      charList = info.itemList

      console.log('generated characters:', uniqueChars, randomCharWeightUpperLimit, charList);
    },
    generateResults: function() {
      // location
      this.$root.$data.locationsToDisplay = [];

      if (this.$root.$data.generate_location) {
        var weightToGo = Math.random() * randomLocationsWeightUpperLimit;
        for (const location of locationList) {
          if (weightToGo <= (location.weight || 1)) {
            this.$root.$data.locationsToDisplay.push(location);
            break;
          }

          weightToGo -= location.weight || 1;
        }
      }

      // characters
      this.$root.$data.charsToDisplay = [];

      const charsToGenerate = Math.min(uniqueChars, this.$root.$data.generate_characters);
      for (let i = 0; i < charsToGenerate; i++) {
        var regenerateChar = false;
        var weightToGo = Math.random() * randomCharWeightUpperLimit;
        for (const char of charList) {
          if (weightToGo <= (char.weight || 1)) {
            if (this.$root.$data.charsToDisplay.includes(char)) {
              regenerateChar = true;
              break;
            }

            this.$root.$data.charsToDisplay.push(char);
            break;
          }

          weightToGo -= char.weight || 1;
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
  line-height: 1.2;
}
.categoryName {
  color: #cad6e0;
  text-align: center;
  padding-top: .2em;
}
</style>