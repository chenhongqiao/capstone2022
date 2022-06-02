<template>
  <v-container>
    <v-row>
      <v-col>
        <v-sheet class="pa-4 rounded">
          <div class="d-flex justify-center">
            <v-img
              dark
              src="logo.png"
              height="400"
              max-width="400"
            />
          </div>
          <div class="my-4 text-h5 text-center text--primary">
            <div>Receiving information from only one perspective can lead to individuals dehumanizing other groups.</div>
          </div>
          <v-divider />
          <div class="my-6">
            <p class="text-body-1 text--secondary">
              One of the evolutionary advantages of humans is our ability to empathize with others around us, and this ability has been pulling human society together for thousands of years. When something bad happened to another human, we feel bad for them because it reminds us of our own experience. When something wrong is being done to another human, we feel like we need to do something because we don’t want the same to happen to us. However, it’s all based the similarities we recognize between us and other human beings, and Chimamanda Adichie warns that one thing can threaten that.
            </p>
            <blockquote class="blockquote">
              <p>
                The consequence of the single story is this: It robs people of dignity. It makes our recognition of our equal humanity difficult. It emphasizes how we are different rather than how we are similar.
              </p>
              <p class="text-right mr-8 pr-8">
                Chimamanda Adichie
              </p>
            </blockquote>
            <p class="text-body-1 text--secondary">
              When we emphasize the differences instead of similarities between us and others, we gradually lose the ability to compassion for them. Eventually, they seem too different to us that we no longer recognize their human dignity and rights but instead view them as animals or objects. When we have multiple perspectives, we see their human traits and similarities. When we have only one perspective, we go deep into how they are different, give them tags of prejudice, and eventually view them as lesser a human.
            </p>
            <p class="text-body-1 text--secondary">
              One of the extreme but typical examples of a single perspective leading to dehumanization is the Holocaust. Please navigate to the Explore page to see how the Nazi party’s single perspective can led to German citizens dehumanizing Jewish people.
            </p>
          </div>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { defineComponent } from '@nuxtjs/composition-api'
export default defineComponent({
  name: 'HomePage'
})
</script>
