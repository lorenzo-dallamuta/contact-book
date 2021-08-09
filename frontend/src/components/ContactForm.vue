<template>
    <form id="contact-form">
        <label for="first-name">First name</label>
        <input id="first-name" v-model="contactFilter.firstName" />
        <label for="last-name">Last name</label>
        <input id="last-name" v-model="contactFilter.lastName" />
        <label for="department">Department</label>
        <input id="department" v-model="contactFilter.department" />
    </form>
</template>

<script lang="ts">
import { defineComponent, ref, watch } from 'vue'
import { cloneDeep } from 'lodash'

export default defineComponent({
    name: 'ContactForm',
    emits: ['filterChange'],
    setup(props, { emit }) {
        const contactFilter = ref({
            firstName: '',
            lastName: '',
            department: '',
        })

        watch(
            () => cloneDeep(contactFilter),
            (newData) => {
                console.log(newData.value)
                emit('filterChange', newData.value)
            }
        )

        return {
            contactFilter,
        }
    },
})
</script>

<style scoped>
label {
    display: block;
    padding: 1.2em 0.4em 0px;
    text-align: left;
    color: #696969;
}
input {
    width: 100%;
    padding: 0.5em 0.2em 0em;
    display: inline-block;
    border: 1px solid #696969;
    border-radius: 5px;
    font-size: 1em;
    font-weight: bold;
}
input:focus {
    outline: none;
}
</style>
