from rest_framework import serializers
from .models import Department, Person


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ('url', 'name',)


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('url', 'firstname', 'lastname', 'phoneNumber', 'department')
