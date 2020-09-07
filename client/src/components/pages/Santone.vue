<template>
  <div>
    Santone
  </div>
</template>

<script>
import router from "../../router";
export default {
  name: "Santone",
  mounted() {
    this.checkLoggedIn();
  },
  methods: {
    checkLoggedIn() {
      this.$session.start();
      if (!this.session.has("token")) {
        router.push("/auth");
    }
    }
  }
};
</script>

