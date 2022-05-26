<template>
  <v-app dark>
    <v-app-bar
      dark
      app
    >
      <v-tabs centered>
        <v-tab v-for="item in items" :key="item.to" :to="item.to">
          {{ item.title }}
        </v-tab>
      </v-tabs>
    </v-app-bar>
    <v-main>
      <v-container>
        <Nuxt />
      </v-container>
    </v-main>
    <v-footer
      app
    >
      <span>&copy; {{ new Date().getFullYear() }} Harry Chen</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: 'DefaultLayout',
  data () {
    return {
      items: [
        {
          title: 'Home',
          to: '/'
        },
        {
          title: 'Explore',
          to: '/explore'
        },
        {
          title: 'Inspire',
          to: '/inspire'
        }
      ]
    }
  }
}
</script>
