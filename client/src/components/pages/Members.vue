<template>
  <v-container>
    <v-row justify="center">
      <div v-for="value in members" :key="value" rows="12" md="2">
        <v-tooltip right>
          <!-- <div :class="[value.color]" class="pa-6 text-center rounded-xl" v-text="`${value.name}`"></div> -->
          <template v-slot:activator="{ on, attrs }">
            <v-btn :color="value.color" dark fab v-bind="attrs" v-on="on">{{value.in}}</v-btn>
          </template>
          <span>{{value.name}}</span>
        </v-tooltip>
      </div>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "Members",
  props: {
    id: Number,
  },
  data() {
    return {
      room_id: this.id,
      members: [
        { name: "Hiroaki Kitagawa", in: "HK", color: "green" },
        { name: "Satoshi Hirai", in: "SH", color: "blue" },
        { name: "Katsuki Sasazawa", in: "KS", color: "grey darken-1" },
        { name: "波田野 創", in: "創", color: "green" },
      ],
    };
  },
  methods: {
    get_members() {
      this.room_id++;
    },
  },
};
</script>