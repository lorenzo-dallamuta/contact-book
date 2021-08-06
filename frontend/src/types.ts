export type ContactInput = {
    firstName: string;
    lastName: string;
    department: string;
};

export type Contact = ContactInput & { phoneNumber: string };
