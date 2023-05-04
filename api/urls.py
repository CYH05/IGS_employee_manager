from django.urls import include, path
from rest_framework import routers
from .employee.api import EmployeeViewSet
from .department.api import DepartmentViewSet
from .populate.api import PopulateViewSet

router = routers.DefaultRouter()
router.register(r'employee', EmployeeViewSet)
router.register(r'department', DepartmentViewSet)
router.register(r'populate', PopulateViewSet, basename='populate')

urlpatterns = [
    path('', include(router.urls))
]