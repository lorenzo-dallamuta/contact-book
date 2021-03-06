import rest_framework_filters as filters
from .models import Department, Person


class DepartmentFilter(filters.FilterSet):
    class Meta:
        model = Department
        fields = {
            'name': ['exact', 'iexact', 'contains']
        }


class PersonFilter(filters.FilterSet):
    department = filters.RelatedFilter(
        'DepartmentFilter', queryset=Department.objects.all())

    class Meta:
        model = Person
        fields = {
            'firstName': ['exact', 'iexact', 'contains'],
            'lastName': ['exact', 'iexact', 'contains']
        }
