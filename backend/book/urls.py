from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, PersonViewSet

router = DefaultRouter()
router.register(r'department', DepartmentViewSet, basename='department')
router.register(r'person', PersonViewSet, basename='person')

urlpatterns = (
    path('api/', include(router.urls)),
)