import { shallowMount } from '@vue/test-utils'
import ContactDetail from '@/components/ContactDetail.vue'

describe('ContactDetail', () => {
    test('it renders props to template', () => {
        const firstName = 'Django'
        const lastName = 'Reinhardt'
        const phoneNumber = '+1234567'
        const department = 'Music Development'

        const target = `First name: ${firstName} Last name: ${lastName} Department: ${department} Phone: ${phoneNumber}`

        const wrapper = shallowMount(ContactDetail, {
            props: {
                contact: {
                    firstName,
                    lastName,
                    phoneNumber,
                    department,
                },
            },
        })
        expect(wrapper.find('div#contact-detail').text()).toContain(target)
    })
})
