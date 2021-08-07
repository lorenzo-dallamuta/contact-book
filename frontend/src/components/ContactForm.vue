<template>
    <form id="contact-form">
        <label for="first-name">First name</label>
        <input id="first-name" v-model="contactName.firstName" />
        <label for="last-name">Last name</label>
        <input id="last-name" v-model="contactName.lastName" />
        <label for="department">Department</label>
        <input id="department" v-model="department" />
    </form>
</template>

<script lang="ts">
import { defineComponent, ref, watch } from 'vue'
import { cloneDeep, debounce } from 'lodash'
import useDebouncesRef from '@/composables/useDebouncedRef'

export default defineComponent({
    name: 'ContactForm',
    emits: ['nameChange', 'departmentChange'],
    setup(props, { emit }) {
        const contactName = ref({
            firstName: '',
            lastName: '',
        })
        const department = useDebouncesRef('', 400)

        watch(
            () => cloneDeep(contactName),
            (newData) => {
                console.log('got in')
                debounce(() => {
                    emit('nameChange', newData.value)
                }, 400)()
            }
        )

        watch(department, (newData) => {
            emit('departmentChange', newData)
        })

        return {
            contactName,
            department,
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
