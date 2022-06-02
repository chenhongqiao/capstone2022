<template>
  <div>
    <Simulator :scenario="scenario" />
  </div>
</template>

<script>
export default {
  name: 'ExplorePage',
  data () {
    return {
      scenario: {
        available: ['Jews also owned substantial property (for example, more than half — about 60% — of Berlin belonged to the Jews, although they were only 3.8% of the population). That proves the extent to which Jewish parasites had exploited the German people.', 'Of course the Jew is a human being too. None of us has ever doubted it. But a flea is also an animal. But not a very pleasant one. Since a flea is not a pleasant animal, we have no duty to protect and defend it, to take care of it so that it can bite and torment and torture us. Rather, we make it harmless.', 'In the battle between the races, there is no truce. If you are determined finally to defend yourself, German people, then be pitiless!'],
        unavailable: ['Jews are someone\'s parents, sons, daughters, or siblings.', 'Jewish teaching emphasizes compassion.', 'Jews are your neighbors and friends.'],
        person: {
          name: 'Peter Simon',
          description: 'Peter is a German citizen under the Nazi regime. He is a hard-working factory worker and does not face persecution from the government. He has a wife and 2 kids. He saved money to purchase a radio but only has access to Nazi-owned medias. He does not have Jewish friends or relatives.'
        }
      }
    }
  }
}
</script>
