from rest_framework import serializers
from .models import Department, Person


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('name',)


class PersonSerializer(serializers.ModelSerializer):
    department = serializers.StringRelatedField()

    class Meta:
        model = Person
        fields = ('firstName', 'lastName', 'phoneNumber', 'department',)
