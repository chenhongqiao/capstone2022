<template>
  <div>
    <v-container>
      <v-sheet class="pa-4 rounded">
        <v-row class="ma-1">
          <v-col class="text-body-1" cols="9">
            Welcome to an interactive simulation about the danger of a single perspective. You can select sources to digest, and then a simulated character powered by artificial intelligence will digest the pieces and answer questions. You can switch between premade scenarios or create your own custom scenario on the right.
          </v-col>
          <v-col>
            <v-select
              v-model="scenario"
              :items="scenarios"
              item-text="id"
              return-object
              prepend-icon="mdi-account-box"
              outlined
              dense
            />
          </v-col>
        </v-row>
      </v-sheet>
    </v-container>
    <v-container>
      <v-row>
        <v-col>
          <v-sheet class="pa-4 rounded">
            <div v-if="scenario.id!=='Custom'">
              <p class="text-h6">
                The single perspective
              </p>
              <v-card
                v-for="(source,index) in scenario.available"
                :key="index"
                outlined
                class="mb-4"
                :color="source.selected?'primary':'inactive'"
                @click="toggleSource(index, 'available')"
              >
                <v-card-text class="pb-1">
                  <p>{{ source.text }}</p>
                  <p v-if="source.cite" class="text--disabled">
                    Source: {{ source.cite }}
                  </p>
                </v-card-text>
              </v-card>
              <p class="text-h6">
                Other perspectives
              </p>
              <v-card
                v-for="(source,index) in scenario.unavailable"
                :key="index"
                outlined
                class="mb-4"
                :color="source.selected?'primary':'inactive'"
                @click="toggleSource(index, 'unavailable')"
              >
                <v-card-text class="pb-1">
                  <p>{{ source.text }}</p>
                  <p v-if="source.cite" class="text--disabled">
                    Source: {{ source.cite }}
                  </p>
                </v-card-text>
              </v-card>
            </div>
            <div v-else>
              <p class="text-h6">
                Their perspectives
              </p>
              <v-card
                v-for="(source,index) in scenario.available"
                :key="index"
                outlined
                class="mb-4"
              >
                <v-container>
                  <v-textarea v-model="source.text" outlined />
                  <v-row class="px-4">
                    <v-checkbox v-model="source.selected" label="Digest this source" class="mt-0 pt-1" />
                    <v-spacer />
                    <v-btn>
                      <v-icon dark @click="removeSource(index)">
                        mdi-delete
                      </v-icon>
                    </v-btn>
                  </v-row>
                </v-container>
              </v-card>
              <div class="text-right">
                <v-btn color="primary" @click="addSource">
                  Add<v-icon right dark>
                    mdi-plus
                  </v-icon>
                </v-btn>
              </div>
            </div>
          </v-sheet>
        </v-col>
        <v-col>
          <v-sheet v-if="scenario.person.name&&scenario.person.description" class="pa-4 rounded mb-4">
            <p class="text-h4 text-center">
              {{ scenario.person.name }}
            </p>
            <p class="text--secondary">
              {{ scenario.person.description }}
            </p>
          </v-sheet>
          <v-sheet class="pa-4 rounded mb-4">
            <v-text-field v-model="question" label="Ask them a question" outlined clearable />
            <div class="text-right">
              <v-btn color="primary" :disabled="!question||loading||!selectedSources.length" @click="getAnswers">
                Send <v-icon right dark>
                  mdi-send
                </v-icon>
              </v-btn>
            </div>
          </v-sheet>
          <v-sheet v-if="answers.length||loading" class="pa-4 rounded">
            <p class="text-h6">
              {{ scenario.person.name ? scenario.person.name+'\'s' : 'Their' }} response
            </p>
            <div v-if="loading" class="text-center">
              <v-progress-circular
                indeterminate
                color="primary"
              />
            </div>
            <div v-else>
              <v-card v-for="(answer,index) in answers" :key="index" outlined class="mb-4">
                <v-card-text class="text-body-1">
                  {{ prefix[index] }} "{{ answer }}"
                </v-card-text>
              </v-card>
            </div>
          </v-sheet>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script lang="ts">
import { defineComponent, computed, ref, ComputedRef, useContext, Ref, watch } from '@nuxtjs/composition-api'
interface Source {
  text: string
  selected: boolean
  cite?: string
  available: boolean
}
export interface Scenario {
  id: string
  available: Source[]
  unavailable: Source[]
  person: {
    name: string
    description: string
    cite?: string
  }
}
function useSources (scenario: Ref<Scenario>) {
  const selectedSources = computed(() => {
    return scenario.value.available.filter(source => source.selected).concat(scenario.value.unavailable.filter(source => source.selected))
  })
  function toggleSource (index: number, type: string) {
    if (type === 'available') {
      scenario.value.available[index].selected = !scenario.value.available[index].selected
    } else if (type === 'unavailable') {
      scenario.value.unavailable[index].selected = !scenario.value.unavailable[index].selected
    }
  }
  function addSource () {
    scenario.value.available.push({ text: '', selected: false, available: true })
  }
  function removeSource (index:number) {
    scenario.value.available.splice(index, 1)
  }
  return {
    selectedSources,
    toggleSource,
    addSource,
    removeSource
  }
}
function useCharacters (sources: Ref<Scenario>) {
  const question = ref('')
  watch(sources, () => {
    question.value = ''
  })
  return {
    question: ref(question)
  }
}
function useAnswers (scenario: Ref<Scenario>, sources: ComputedRef<Source[]>, question: Ref<string>) {
  const answers: Ref<string[]> = ref([])
  const prefix: Ref<string[]> = ref([])
  watch(scenario, () => {
    answers.value.splice(0, answers.value.length)
    prefix.value.splice(0, prefix.value.length)
  })
  const loading = ref(false)
  const { $axios } = useContext()
  async function getAnswers () {
    loading.value = true
    answers.value.splice(0, answers.value.length)
    prefix.value.splice(0, prefix.value.length)
    const queue: Promise<string>[] = []
    sources.value.forEach((source) => {
      queue.push($axios.$post('https://machine-reading.harrychen.workers.dev/', {
        question: JSON.stringify(question.value),
        passage: source.text.toString()
      }))
      if (source.available) {
        prefix.value.push('Some sources say the answer is')
      } else if (!source.available) {
        prefix.value.push('However, others say')
      }
    })
    answers.value.push(...(await Promise.all(queue)))
    loading.value = false
  }
  return { getAnswers, answers, loading, prefix }
}
export default defineComponent({
  name: 'ExplorePage',
  setup () {
    const scenarios: Ref<Scenario[]> = ref([{
      id: 'Peter Simon',
      available: [
        { text: 'Jews also owned substantial property (for example, more than half — about 60% — of Berlin belonged to the Jews, although they were only 3.8% of the population). That proves the extent to which Jewish parasites had exploited the German people.', selected: false, cite: 'Max Eichler, Du bist sofort im Bilde (Erfurt: J. G. Cramer’s Verlag, 1939) pp. 139-142.', available: true },
        { text: 'Of course the Jew is a human being too. None of us has ever doubted it. But a flea is also an animal. But not a very pleasant one. Since a flea is not a pleasant animal, we have no duty to protect and defend it, to take care of it so that it can bite and torment and torture us. Rather, we make it harmless.', selected: false, cite: 'Kurt Hilmar Eitzen, “Zehn Knüppel wider die Judenknechte,” Unser Wille und Weg (6) 1936, pp. 309-310.', available: true },
        { text: 'In the battle between the races, there is no truce. If you are determined finally to defend yourself, German people, then be pitiless!', selected: false, cite: 'Kurt Hilmar Eitzen, “Zehn Knüppel wider die Judenknechte,” Unser Wille und Weg (6) 1936, pp. 309-310.', available: true },
        { text: 'The Jew is the parasite of humanity. He can be a parasite for an individual person, a social parasite for whole peoples, and the world parasite of humanity.', selected: false, cite: 'G. G. Otto, Der Jude als Weltparasit (Munich: Eher Verlag, 1943).', available: true },
        { text: '[Jews are] a stable, inbred mixture of extreme races and racial rubbish.', selected: false, cite: 'G. G. Otto, Der Jude als Weltparasit (Munich: Eher Verlag, 1943).', available: true }],
      unavailable: [
        { text: '[A Jewish person] is a pianist who hoped to become a conductor and concert pianist. He started studying piano at the age of 10 and gave his first concert at the age of 14.', selected: false, cite: 'Bio of Otto-Karl Gruenbaum - Holocaust Encyclopedia', available: false },
        { text: '[A Jewish person] is the parent of two children.', selected: false, cite: 'Bio of Jeno Katz - Holocaust Encyclopedia', available: false },
        { text: 'Jewish teaching promotes love, humility, service, democracy, and many other values.', selected: false, cite: 'Attitudes, Beliefs and Values Shaping Jewish Practice - Reconstructing Judaism', available: false },
        { text: '[A Jewish person] is a worker in a textile factory.', selected: false, cite: 'Bio of Matvey Gredinger - Holocaust Encyclopedia', available: false }],
      person: {
        name: 'Peter Simon',
        description: 'Peter is a German citizen under the Nazi regime. He is a hard-working factory worker and does not face persecution from the government. Peter saved money to purchase a radio but only had access to Nazi-controlled media. He has a wife and two kids but does not have Jewish friends or relatives.'
      }
    }, {
      id: 'Custom',
      available: [],
      unavailable: [],
      person: {
        name: '',
        description: ''
      }
    }])
    const activeScenario = ref(scenarios.value[0])
    const sources = useSources(activeScenario)
    const character = useCharacters(activeScenario)
    const answers = useAnswers(activeScenario, sources.selectedSources, character.question)

    return {
      ...sources,
      ...answers,
      ...character,
      scenario: activeScenario,
      scenarios
    }
  }
})
</script>
