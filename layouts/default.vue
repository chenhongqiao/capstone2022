<template>
  <v-app dark>
    <v-navigation-drawer
      v-model="drawer"
      clipped
      fixed
      app
    >
      <v-list>
        <v-list-item
          v-for="(route, index) in routes"
          :key="index"
          :to="route.to"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ route.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>{{ route.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar
      clipped-left
      fixed
      app
    >
      <v-app-bar-nav-icon class="d-lg-none" @click="drawer = !drawer" />
      <v-toolbar-title>
        The Danger of a Single Perspective
      </v-toolbar-title>
    </v-app-bar>
    <v-main>
      <v-container>
        <Nuxt />
      </v-container>
    </v-main>
    <v-footer dark app>
      <div>
        Harry Chen - Humanities 9 Spring Capstone
      </div>
    </v-footer>
  </v-app>
</template>

<script lang="ts">
import { defineComponent, ref } from '@nuxtjs/composition-api'
export default defineComponent({
  name: 'DefaultLayout',
  setup () {
    const routes = [
      {
        icon: 'mdi-home',
        title: 'Home',
        to: '/'
      },
      {
        icon: 'mdi-chart-bubble',
        title: 'Explore',
        to: '/explore'
      }
    ]

    return {
      routes: ref(routes),
      drawer: ref(true)
    }
  }
})
</script>
