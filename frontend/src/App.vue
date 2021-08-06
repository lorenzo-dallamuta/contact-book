<template>
    <div class="container">
        <ContactForm
            @nameChange="handleName($event)"
            @departmentChange="handleDepartment($event)"
        ></ContactForm>
        <ContactList id="contact-list" :contacts="contacts"></ContactList>
    </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from 'vue'
import ContactForm from './components/ContactForm.vue'
import ContactList from './components/ContactList.vue'
import { ContactName, Contact } from './types'

export default defineComponent({
    name: 'App',
    components: {
        ContactForm,
        ContactList,
    },
    created() {
        document.title = 'Contact Book'
    },
    data() {
        return {
            query: '',
            contacts: {
                type: Array as PropType<Array<Contact>>,
            },
        }
    },
    computed: {
        url(): string {
            return 'http://127.0.0.1:8000/api/people' + this.query
        },
    },
    methods: {
        handleName(newData: ContactName) {
            this.query = `?firstName__contains=${newData.firstName}&lastName__contains=${newData.lastName}`
        },
        handleDepartment(newVal: string) {
            this.query = `?department__name__contains=${newVal}`
        },
    },
    watch: {
        url(newUrl) {
            fetch(newUrl)
                .then((response) => response.json())
                .then((data) => (this.contacts = data))
                .catch((error) => console.log(error))
        },
    },
})
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
    font-size: 1.2em;
}
</style>
