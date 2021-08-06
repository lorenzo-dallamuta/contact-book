<template>
    <div id="contact-list">
        <ContactDetail class="contact-detail" v-for="(contact, index) in contacts" :contact="contact" :key="index"></ContactDetail>
    </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from 'vue'
import { Contact } from '@/types'
import ContactDetail from './ContactDetail.vue'

export default defineComponent({
    name: "ContactList",
    components: {
        ContactDetail
    },
    props: {
        contacts: {
            type: Array as PropType<Array<Contact>>
        }
    }
})
</script>

<style scoped>
    .contact-detail {
        margin-bottom: 2.5rem;
    }
</style>