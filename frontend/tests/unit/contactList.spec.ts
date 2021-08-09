import { shallowMount } from '@vue/test-utils'
import ContactList from '@/components/ContactList.vue'

describe('ContactList', () => {
    test('it renders props and children to template', () => {
        const firstName = 'Django'
        const lastName = 'Reinhardt'
        const phoneNumber = '+1234567'
        const department = 'Music Development'

        const contact = {
            firstName,
            lastName,
            phoneNumber,
            department,
        }

        const wrapper = shallowMount(ContactList, {
            props: {
                contacts: [contact, contact],
            },
        })
        expect(wrapper.find('div#contact-list').exists()).toBe(true)
        expect(
            wrapper.findAll('contact-detail-stub.contact-detail').length
        ).toBe(2)
    })
})
