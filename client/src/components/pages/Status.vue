<template>
  <v-app id="status">
    <v-item-group mandatory>
      <v-container>
        <v-row>
          <v-col cols="12" md="4">
            <v-item v-slot:default="{ active, toggle }">
              <v-card
                :color="active ? 'blue' : 'grey lighten-5'"
                class="d-flex align-center"
                dark
                height="100"
                @click="toggle"
              >
                <v-scroll-y-transition>
                  <div v-if="active" class="display-3 flex-grow-1 text-center">Focus</div>
                </v-scroll-y-transition>
              </v-card>
            </v-item>
          </v-col>
          <v-col cols="12" md="4">
            <v-item v-slot:default="{ active, toggle }">
              <v-card
                :color="active ? 'grey darken-1' : 'grey lighten-5'"
                class="d-flex align-center"
                dark
                height="100"
                @click="toggle"
              >
                <v-scroll-y-transition>
                  <div v-if="active" class="display-3 flex-grow-1 text-center">Idle</div>
                </v-scroll-y-transition>
              </v-card>
            </v-item>
          </v-col>
          <v-col cols="12" md="4">
            <v-item v-slot:default="{ active, toggle }">
              <v-card
                :color="active ? 'green' : 'grey lighten-5'"
                class="d-flex align-center"
                dark
                height="100"
                @click="toggle"
              >
                <v-scroll-y-transition>
                  <div v-if="active" class="display-3 flex-grow-1 text-center">Relax</div>
                </v-scroll-y-transition>
              </v-card>
            </v-item>
          </v-col>
        </v-row>
      </v-container>
    </v-item-group>
  </v-app>
</template>

<script>
export default {
  name: "Status",
  methods: {
    chengeStatus(color) {
      this.$emit("emitUp", { name: "波田野 創", in: "創", color: color });
    },
  },
};
</script>