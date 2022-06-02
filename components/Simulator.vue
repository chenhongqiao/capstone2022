<template>
  <v-container>
    <v-row>
      <v-col>
        <v-sheet class="pa-4 rounded">
          <p class="text-h6">
            The single perspective
          </p>
          <v-card
            v-for="(source,index) in availableSources"
            :key="source.text"
            outlined
            class="mb-4"
            :color="source.selected?'primary':'inactive'"
            @click="toggleSource(index, 'available')"
          >
            <v-card-text>{{ source.text }}</v-card-text>
          </v-card>
          <p class="text-h6">
            Other perspectives
          </p>
          <v-card
            v-for="(source,index) in unavailableSources"
            :key="source.text"
            outlined
            class="mb-4"
            :color="source.selected?'primary':'inactive'"
            @click="toggleSource(index, 'unavailable')"
          >
            <v-card-text>{{ source.text }}</v-card-text>
          </v-card>
        </v-sheet>
      </v-col>
      <v-col>
        <v-sheet class="pa-4 rounded">
          <p class="text-h4 text-center">
            {{ character.name }}
          </p>
          <p>{{ character.description }}</p>
        </v-sheet>
        <v-sheet class="pa-4 rounded mt-4">
          <v-text-field v-model="question" label="Ask them a question" filled clearable />
          <div class="text-right">
            <v-btn color="primary" :disabled="!question||loading||!selectedSources.length" @click="getAnswers">
              Send <v-icon right dark>
                mdi-send
              </v-icon>
            </v-btn>
          </div>
        </v-sheet>
        <v-sheet class="pa-4 rounded mt-4">
          <p class="text-h6">
            {{ character.name }}'s response
          </p>
          <div v-if="loading" class="text-center">
            <v-progress-circular
              indeterminate
              color="primary"
            />
          </div>
          <div v-else>
            <v-card v-for="answer in answers" :key="answer" outlined class="mb-4">
              <v-card-text class="text-body-1">
                Some sources say the answer is "{{ answer }}"
              </v-card-text>
            </v-card>
          </div>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { defineComponent, computed, ref, ComputedRef, useContext, Ref } from '@nuxtjs/composition-api'
interface Scenario {
  available: string[]
  unavailable: string[]
  person: {
    name: string
    description: string
  }
}
interface Source {
  text: string
  selected: boolean
}
function useSources (scenario: Scenario) {
  const availableSources: Source[] = []
  const unavailableSources: Source[] = []
  if (scenario) {
    scenario.available.forEach((text) => {
      availableSources.push({ text, selected: false })
    })
    scenario.unavailable.forEach((text) => {
      unavailableSources.push({ text, selected: false })
    })
  }
  const selectedSources = computed(() => {
    return availableSources.filter(source => source.selected).concat(unavailableSources.filter(source => source.selected))
  })
  function toggleSource (index: number, type: string) {
    if (type === 'available') {
      availableSources[index].selected = !availableSources[index].selected
    } else if (type === 'unavailable') {
      unavailableSources[index].selected = !unavailableSources[index].selected
    }
  }
  return {
    availableSources: ref(availableSources),
    unavailableSources: ref(unavailableSources),
    selectedSources,
    toggleSource
  }
}
function useCharacters (scenario: Scenario) {
  const question = ref('')
  return {
    character: ref(scenario.person),
    question
  }
}
function useAnswers (sources: ComputedRef<Source[]>, question: Ref<string>) {
  const answers: string[] = []
  const loading = ref(false)
  const { $axios } = useContext()
  async function getAnswers () {
    loading.value = true
    const queue: Promise<string>[] = []
    sources.value.forEach((source) => {
      queue.push($axios.$post('https://machine-reading.harrychen.workers.dev/', {
        question: JSON.stringify(question.value),
        passage: source.text.toString()
      }))
    })
    answers.splice(0, answers.length)
    answers.push(...(await Promise.all(queue)))
    loading.value = false
  }
  return { getAnswers, answers: ref(answers), loading }
}
export default defineComponent({
  name: 'PersonSimulator',
  props: {
    scenario: {
      type: Object as () => Scenario,
      default: null
    }
  },

  setup ({ scenario }) {
    const sources = useSources(scenario)
    const character = useCharacters(scenario)
    const answers = useAnswers(sources.selectedSources, character.question)

    return {
      ...sources,
      ...answers,
      ...character
    }
  }
})

</script>
