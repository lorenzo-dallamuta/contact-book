export type ContactFilter = {
    firstName: string
    lastName: string
    department: string
}

export type Contact = ContactFilter & {
    phoneNumber: string
}
