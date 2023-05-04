from django.db import models
from api.department.models import Department

class Employee(models.Model):
    name = models.CharField("Nome", max_length=30)
    email = models.EmailField("E-mail")
    department = models.ForeignKey(Department, related_name='department', on_delete=models.CASCADE)
    
    def __str__(self):
        return "{} | {}".format(self.name, self.department.name)
    
    def create(data: dict, department: Department)-> models.Model:
        employee = Employee(name=data['name'], email=data['email'], department=department)
        employee.save()
        return employee
    
    def update(self , data: dict, department: Department)-> models.Model:
        self.name = data['name'] if 'name' in data else self.name 
        self.email = data['email']if 'email' in data else self.email 
        self.department = department
        self.save()
        return self