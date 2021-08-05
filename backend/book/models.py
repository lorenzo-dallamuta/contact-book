from string import Template
from django.db import models
from django.core.validators import RegexValidator


class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Person(models.Model):
    """
    the model representing contacts in the book, for consistency reasons
    they are referred to as person/people instead of contact/contacts
    """
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{7,15}$")
    phoneNumber = models.CharField(
        validators=[phoneNumberRegex], max_length=16, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'people'

    def __str__(self):
        return Template('$first $last').substitute(first=self.firstName, last=self.lastName)
