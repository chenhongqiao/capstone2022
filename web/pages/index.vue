<template>
  <v-row justify="center" align="center">
    <v-col>
      <v-card class="logo d-flex justify-center">
        <v-img
          dark
          src="logo.png"
          max-height="350"
          max-width="350"
        />
      </v-card>
      <v-card>
        <v-container class="mx-4">
          <div class="my-4 text-h5 text-center text--primary">
            <div> <i>Bloody consequences do not make people give up misleading and hateful ideas</i> </div>
          </div>
          <v-divider />
          <div class="my-6">
            <p class="text-body-1 text--secondary">
              Throughout the history, misleading languages and hate speech have caused violent crimes, civil wars, and even genocide. However, some of these ideas still exist and thrive even in today's society. This project aims to show the danger of hateful ideas by demonstrating how people forget the damage these ideas have caused how they can continue to harm the society decades after causing bloody atrocities.
            </p>
            <p class="text-body-1 text--secondary">
              The project analyzes the role of misinformation and hate speech in Julius Caesar and the Holocaust. Empowered by machine learning and artificial intelligence, it also attempts to show the similarities in ideas and manupilation techniques between the Nazi regime and some politicians in modern United States.
            </p>
            <p class="text-body-1 text--secondary">
              This project is part of Northwood High School Humanities 9 Fall Capstone.
            </p>
          </div>
          <div class="my-6">
            <v-row>
              <v-col
                v-for="(item, i) in features"
                :key="i"
                cols="12"
                md="4"
              >
                <v-responsive max-width="300" class="mx-auto text-center">
                  <div class="mb-2">
                    <v-icon class="text-h1" color="grey">
                      {{ item.icon }}
                    </v-icon>
                  </div>
                  <div class="text-h6 mt-3">
                    {{ item.title }}
                  </div>
                  <div class="text-body-1 mt-2 text--secondary">
                    {{ item.description }}
                  </div>
                </v-responsive>
              </v-col>
            </v-row>
          </div>
        </v-container>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: 'IndexPage',
  data () {
    return {
      features: [{
        icon: 'mdi-home',
        title: 'Project Home',
        description: 'Basic information and the motivation of the project.'
      }, {
        icon: 'mdi-telescope',
        title: 'Explore with ML',
        description: 'Explore the connections between dangerous ideas in modern society and Nazi propaganda.'
      }, {
        icon: 'mdi-book-open',
        title: 'Humanities Inspiration',
        description: 'The History and English inspiration behind this project.'
      }]
    }
  }
}
</script>
