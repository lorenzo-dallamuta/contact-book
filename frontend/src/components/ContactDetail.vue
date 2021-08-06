<template>
    <div id="contact-detail">
        First name: {{ contact.firstName }}<br />
        Last name: {{ contact.lastName }}<br />
        Department: {{ contact.department }}<br />
        Phone: {{ contact.phoneNumber }}<br />
    </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from 'vue'
import { Contact } from '@/types'

export default defineComponent({
    name: 'ContactDetail',
    props: {
        contact: {
            type: Object as PropType<Contact>,
        },
    },
})
</script>

<style scoped>
#contact-detail {
    text-align: left;
}
</style>
