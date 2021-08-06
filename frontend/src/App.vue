<template>
    <ContactForm></ContactForm>
    <ContactList :contacts="test"></ContactList>
</template>

<script lang="ts">
import { defineComponent } from "vue"
import ContactForm from "./components/ContactForm.vue"
import ContactList from "./components/ContactList.vue"

export default defineComponent({
  name: "App",
  components: {
    ContactForm,
    ContactList
  },
  // TODO: remove temporary data stub
  data() {
      return {
          test: [{
              firstName: "one",
              lastName: "two",
              phoneNumber: "three",
              department: "four",
          }, {
              firstName: "1",
              lastName: "2",
              phoneNumber: "3",
              department: "4",
          }]
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
