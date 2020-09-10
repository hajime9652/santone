<template>
  <v-app id="rooms">
    <v-list subheader>
      <v-subheader>Recent rooms</v-subheader>

      <v-list-item v-for="item in items" :key="item.title" @click="join_room(item)">
        <v-list-item-avatar>
          <v-img :src="item.avatar"></v-img>
        </v-list-item-avatar>

        <v-list-item-content>
          <v-list-item-title v-text="item.title"></v-list-item-title>
        </v-list-item-content>

        <v-list-item-icon>
          <v-icon :color="item.active ? 'blue accent-4' : 'blue lighten-5'">mdi-domain</v-icon>
        </v-list-item-icon>
      </v-list-item>
    </v-list>

    <v-divider></v-divider>

    <v-list subheader>
      <v-subheader>Previous rooms</v-subheader>

      <v-list-item v-for="item in items2" :key="item.title" @click="join_room(item)">
        <v-list-item-avatar>
          <v-img :src="item.avatar"></v-img>
        </v-list-item-avatar>

        <v-list-item-content>
          <v-list-item-title v-text="item.title"></v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
    <v-list dense>
      <v-list-item link>
        <v-list-item-action>
          <v-icon>mdi-view-dashboard</v-icon>
        </v-list-item-action>
        <v-list-item-content>
          <v-list-item-title>Dashboard</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item link>
        <v-list-item-action>
          <v-icon>mdi-cog</v-icon>
        </v-list-item-action>
        <v-list-item-content>
          <v-list-item-title>Settings</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-app>
</template>

<script>
export default {
  name: "Rooms",
  data: () => ({
    items: [
      {
        active: true,
        title: "Office Green Tea",
        avatar: "../../assets/OGT.png",
        id: 1,
      },
      { active: true, title: "Google", avatar: "../../assets/G.png", id: 2 },
      { title: "Ax", avatar: "../../assets/Ax.png", id: 3 },
      { title: "波田野家", avatar: "../../assets/hatano.png", id: 4 },
    ],
    items2: [{ title: "Ernie", avatar: "../../assets/ernie.jpg", id: 5 }],
  }),
  methods: {
    join_room(item) {
      this.$emit("emitUp", { name: item.title, room_id: item.id });
    },
  },
};
</script>