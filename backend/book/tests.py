import json
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Department, Person


class DepartmentTestCase(APITestCase):
    def setUp(self):
        Department.objects.create(name="Testing Department")
        self.len = Department.objects.count()

    def test_create(self):
        data = {"name": "Testing Department Create"}
        response = self.client.post("/api/department/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve(self):
        target = json.dumps([{"id": 1, "name": "Testing Department"}])
        response = self.client.get("/api/department?name=Testing%20Department")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(target, json.dumps(response.json()))

    def test_retrieve_partial(self):
        target = json.dumps([{"id": 1, "name": "Testing Department"}])
        response = self.client.get("/api/department?name__contains=Tes")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(target, json.dumps(response.json()))

    def test_list(self):
        data = {"name": "Testing Department List 1"}
        self.client.post("/api/department/", data)
        self.assertEqual(Department.objects.count(), self.len + 1)


class PeopleTestCase(APITestCase):

    def setUp(self):
        self.department = Department.objects.create(name="Testing Department")
        Person.objects.create(firstName="Django", lastName="Reinhardt",
                              phoneNumber="+1234567", department=self.department)
        self.len = Person.objects.count()
        self.target = json.dumps([{'id': 1, 'firstName': 'Django', 'lastName': 'Reinhardt',
                                 'phoneNumber': '+1234567', 'department': 'Testing Department'}])

    def test_create(self):
        data = {"firstName": "Louis", "lastName": "Armstrong",
                "phoneNumber": "+1357924", "department": "Testing Department"}
        response = self.client.post("/api/people/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_by_first_name(self):
        response = self.client.get("/api/people?firstName=Django")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(self.target, json.dumps(response.json()))

    def test_retrieve_by_last_name(self):
        response = self.client.get("/api/people?lastName=Reinhardt")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(self.target, json.dumps(response.json()))

    def test_retrieve_by_department(self):
        response = self.client.get(
            "/api/people?department_name=Testing%20Department")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(self.target, json.dumps(response.json()))

    def test_retrieve_by_first_name_partial(self):
        response = self.client.get("/api/people?firstName__contains=Dja")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(self.target, json.dumps(response.json()))

    def test_retrieve_by_last_name_partial(self):
        response = self.client.get("/api/people?lastName__contains=Rei")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(self.target, json.dumps(response.json()))

    def test_retrieve_by_department_partial(self):
        response = self.client.get(
            "/api/people?department_name__contains=Tes")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(self.target, json.dumps(response.json()))

    def test_list(self):
        data = {"firstName": "Louis", "lastName": "Armstrong",
                "phoneNumber": "+1357924", "department": "Testing Department"}
        self.client.post("/api/people/", data)
        self.assertEqual(Person.objects.count(), self.len + 1)
