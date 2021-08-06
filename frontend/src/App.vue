<template>
    <div class="container">
        <ContactForm
            @nameChange="handleName($event)"
            @departmentChange="handleDepartment($event)"
        ></ContactForm>
        <ContactList id="contact-list" :contacts="[]"></ContactList>
    </div>
    {{ query }}
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import ContactForm from './components/ContactForm.vue'
import ContactList from './components/ContactList.vue'
import { ContactName } from './types'

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
            baseUrl: 'http://127.0.0.1:8000/api/people',
            query: '',
        }
    },
    computed: {
        url(): string {
            return this.baseUrl + this.query
        },
    },
    methods: {
        // handleName({firstName, lastName}: {firstName: string, lastName: string}) {
        handleName(newData: ContactName) {
            this.query = `?firstName=${newData.firstName}&lastName=${newData.lastName}`
        },
        handleDepartment(newVal: string) {
            this.query = `?department__name=${newVal}`
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
