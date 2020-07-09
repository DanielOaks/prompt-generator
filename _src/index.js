import Vue from 'vue'
import HomePage from './pages/HomePage.vue'
import CategoriesPage from './pages/CategoriesPage.vue'
import CategoryPage from './pages/CategoryPage.vue'
import ResultsPage from './pages/ResultsPage.vue'

Vue.component('homePage', HomePage)
Vue.component('categoriesPage', CategoriesPage)
Vue.component('categoryPage', CategoryPage)
Vue.component('resultsPage', ResultsPage)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  mounted: function() {
    this.$refs.homePage.show();
  },
})