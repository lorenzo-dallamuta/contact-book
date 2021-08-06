<template>
  <ContactDetail :contact="test" ></ContactDetail>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import ContactDetail from "./components/ContactDetail.vue";

export default defineComponent({
  name: "App",
  components: {
    ContactDetail
  },
  // TODO: remove temporary data stub
  data() {
      return {
          test: {
              firstName: "one",
              lastName: "two",
              phoneNumber: "three",
              department: "four",
          }
      }
  }
});
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
</style>
