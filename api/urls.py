from django.urls import include, path
from rest_framework import routers
from .employee.api import EmployeeViewSet
from .department.api import DepartmentViewSet

router = routers.DefaultRouter()
router.register(r'employee', EmployeeViewSet)
router.register(r'department', DepartmentViewSet)

urlpatterns = [
    path('', include(router.urls))
]