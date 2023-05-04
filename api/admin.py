from django.contrib import admin

from api.employee.models import Employee
from api.department.models import Department

admin.site.register(Employee)
admin.site.register(Department)