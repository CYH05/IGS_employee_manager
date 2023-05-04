from django.db import models

class Department(models.Model):
    name = models.CharField('Nome departamento', max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    
    def create(data: dict) -> models.Model:
        department = Department(name=str.lower(data['name']))
        department.save()
        return department
    
    def update(self , data: dict)-> models.Model:
        self.name = str.lower(data['name']) if 'name' in data else self.name 
        self.save()
        return self