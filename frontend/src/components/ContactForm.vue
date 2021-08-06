<template>
    <form id="contact-form">
        <label for="first-name">First name</label>
        <input id="first-name" v-model="firstName">
        <label for="last-name">Last name</label>
        <input id="last-name" v-model="lastName">
        <label for="department">Department</label>
        <input id="department" v-model="department">
    </form>
    <p>
        first: {{ firstName }}
        last: {{ lastName }}
        dpt: {{ department }}
    </p>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
    name: "ContactForm",
    data() {
        return {
            firstName: "",
            lastName: "",
            department: ""
        }
    }
})
</script>

<style scoped>
    label {
        display: block;
        padding: 1.2em 0.4em 0px;
        text-align: left;
        color: #696969
    }
    input {
        width: 100%;
        padding: 0.5em 0.2em 0em;
        display: inline-block;
        border: 1px solid #696969;
        border-radius: 5px;
        font-size: 1.0em;
        font-weight: bold;
    }
    input:focus {
        outline: none
    }
</style>