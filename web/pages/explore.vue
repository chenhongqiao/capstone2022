<template>
  <v-row justify="center" align="center">
    <v-col>
      <v-card>
        <v-container>
          <v-text-field
            v-model="query"
            filled
            dense
            dark
            clearable
          />
          <v-container>
            <v-row>
              <div class="text-body-1 text--secondary pt-1">
                Enter a statement or belief to check if similar ideas were used by Nazi Anti-Semitic Propaganda
              </div>
              <v-spacer />
              <v-btn color="primary" :disabled="!query" @click="executeQuery">
                Search
              </v-btn>
            </v-row>
          </v-container>
        </v-container>
      </v-card>
      <v-card v-if="data.length" class="mt-4">
        <v-container>
          <v-card v-for="item in data" :key="item.sentence" outlined class="mb-4">
            <v-container>
              <p>
                <v-chip small>
                  {{ item.similarities.toFixed(4) }}
                </v-chip>
              </p>
              <p class="text-h6 text--primary">
                {{ item.sentence }}
              </p>
              <p>{{ item.title }}</p>
              <p class="text-body-1 text--secondary">
                {{ item.background }}
              </p>
              <p class="text-body-2 text--disabled">
                Source: {{ item.source }}
              </p>
            </v-container>
          </v-card>
        </v-container>
      </v-card>
      <v-card v-else class="mt-4">
        <v-card-text class="text-center">
          Quotes from a subset of a <a href="https://research.calvin.edu/german-propaganda-archive/" target="_blank">collection</a> of Nazi regime's Anti-Semitic Propaganda will be shown here. The number at the top indicates the similarity determined by the algorithm. Collection is maintained by Professor Emeritus Randall Bytwerk from Calvin University.
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: 'ExplorePage',
  data () {
    return {
      query: '',
      data: []
    }
  },
  methods: {
    async executeQuery () {
      this.data = await this.$axios.$post('/query', { query: this.query })
    }
  }
}
</script>
