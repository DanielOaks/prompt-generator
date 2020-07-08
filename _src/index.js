import Vue from 'vue'
import HomePage from './pages/HomePage.vue'
import CategoriesPage from './pages/CategoriesPage.vue'

Vue.component('homePage', HomePage)
Vue.component('categoriesPage', CategoriesPage)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  mounted: function() {
    this.$refs.homePage.show();
  },
})