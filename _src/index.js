import Vue from 'vue'
import LoadingSpinner from './components/LoadingSpinner.vue'
import CategoriesPage from './pages/CategoriesPage.vue'
import CategoryPage from './pages/CategoryPage.vue'
import ResultsPage from './pages/ResultsPage.vue'

import jsonPointer from 'json-pointer'

Vue.component('loadingSpinner', LoadingSpinner)

Vue.component('categoriesPage', CategoriesPage)
Vue.component('categoryPage', CategoryPage)
Vue.component('resultsPage', ResultsPage)

Vue.prototype.$jsonPointer = jsonPointer;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  data: {
    setup: {
      'categories': {},
    },
    generate_characters: 1,
    generate_location: false,
    generate_scenes: 0,
    current_category: '',
    characterCache: {},
    locationCache: {},
    charsToDisplay: [],
    character_images_required: false,
  },
  mounted: function() {
    this.$refs.categoriesPage.show();

    fetch('/data.json')
      .then(r => r.json())
      .then(json => {
        this.$data.setup = json.setup;
        this.$data.data = json.data_files;

        this.$refs.loadingSpinner.hide();
      });
  },
})