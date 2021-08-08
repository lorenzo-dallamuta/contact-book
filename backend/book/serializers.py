from rest_framework import serializers
from .models import Department, Person


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name',)


class PersonSerializer(serializers.ModelSerializer):
    department = serializers.SlugRelatedField(
        queryset=Department.objects.all(), slug_field="name")

    class Meta:
        model = Person
        fields = ('id', 'firstName', 'lastName', 'phoneNumber', 'department',)
