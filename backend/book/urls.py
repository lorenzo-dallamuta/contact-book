from django.urls import include, path
from .views import DepartmentViewSet, PersonViewSet
from .routers import CustomDefaultRouter

router = CustomDefaultRouter()
router.register(r'department', DepartmentViewSet, basename='department')
router.register(r'person', PersonViewSet, basename='person')

urlpatterns = (
    path('api/', include(router.urls)),
)
