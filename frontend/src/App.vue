<template>
    <div class="container">
        <ContactForm @contactInput="handleInput($event)"></ContactForm>
        <ContactList id="contact-list" :contacts="[]"></ContactList>
    </div>
    {{ contactInfo }}
</template>

<script lang="ts">
import { defineComponent } from "vue"
import ContactForm from "./components/ContactForm.vue"
import ContactList from "./components/ContactList.vue"
import { ContactInput } from "./types";

export default defineComponent({
  name: "App",
  components: {
    ContactForm,
    ContactList
  },
  created() {
      document.title = "Contact Book"
  },
  data() {
      return {
          contactInfo: {
              firstName: "",
              lastName: "",
              department: "",
          }
      }
  },
  methods: {
      handleInput(newVal:ContactInput) {
          this.contactInfo = newVal
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
