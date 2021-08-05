from rest_framework import viewsets
from .models import Department, Person
from .serializers import DepartmentSerializer, PersonSerializer
from .filters import DepartmentFilter, PersonFilter


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_class = DepartmentFilter


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_class = PersonFilter
