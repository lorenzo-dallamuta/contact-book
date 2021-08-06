export type ContactName = {
    firstName: string;
    lastName: string;
};

export type Contact = ContactName & {
    phoneNumber: string;
    department: string;
};
