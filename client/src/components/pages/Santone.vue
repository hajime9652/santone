<template>
  <div id="app">
    <v-app id="inspire">
      <v-app id="inspire">
        <v-navigation-drawer v-model="drawer" app clipped>
          <Rooms @emitUp="getRoom" />
        </v-navigation-drawer>

        <v-app-bar app clipped-left>
          <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
          <v-toolbar-title>Room:{{stack.room.name}}</v-toolbar-title>
        </v-app-bar>

        <v-main>
          <Members room="stack.room" />
          <Status />
        </v-main>

        <v-footer app>
          <span>&copy;New title {{ new Date().getFullYear() }}</span>
        </v-footer>
      </v-app>
    </v-app>
  </div>
</template>

<script>
import router from "../../router";
import Rooms from "./Rooms.vue";
import Members from "./Members.vue";
import Status from "./Status.vue";
export default {
  name: "Santone",
  components: {
    Rooms,
    Members,
    Status,
  },
  data() {
    return {
      stack: { room: "", on_desk: "", status: "" },
      drawer: null,
    };
  },
  mounted() {
    this.checkLoggedIn();
  },
  methods: {
    checkLoggedIn() {
      this.$session.start();
      if (!this.session.has("token")) {
        router.push("/auth");
      }
    },
    getRoom(payload) {
      this.stack.room = payload;
    },
  },
};
</script>

