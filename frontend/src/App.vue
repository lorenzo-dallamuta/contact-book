<template>
    <div class="container">
        <ContactForm id="contact-form"></ContactForm>
        <ContactList id="contact-list" :contacts="test"></ContactList>
    </div>
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
  created() {
      document.title = "Contact Book"
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
    .container {
        padding: 1.5em 25% 0;
    }
    #contact-form {
        margin-bottom: 7em;
    }
    #contact-list {
        padding-left: 1.5em;
        font-size: 1.2em
    }

</style>
