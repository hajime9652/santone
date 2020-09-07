import Vue from 'vue'
import Router from 'vue-router'

import Auth from '@/components/pages/Auth'
import Santone from '@/components/pages/Santone'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Santone',
      component: Santone
    },
    {
      path: '/auth',
      name: 'Auth',
      component: Auth
    }
  ]
})
