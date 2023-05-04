from random import random, randint
from ..department.models import Department
from ..employee.models import Employee

employees = [
  {"name":"João Victor", "email": "joaovictor@email.com"},
  {"name":"Carlos Ramos", "email": "carlosramos@email.com"},
  {"name":"Eduardo Silva", "email": "eduardosilva@email.com"},
  {"name":"Letícia Alves", "email": "leticiaalves@email.com"},
  {"name":"Mariana Brando", "email": "marianabrando@email.com"},
  {"name":"Lucas Carvalho", "email": "lucascarvalho@email.com"},
  {"name":"Victor Santos", "email": "victorsantos@email.com"},
  {"name":"Juliana Moraes", "email": "julianamoraes@email.com"},
  {"name":"Beatriz Lima", "email": "beatrizlima@email.com"},
  {"name":"Vitoria Lemos", "email": "vitorialemos@email.com"},
]


departments = [
  "human resources",
  "financial",
  "legal",
  "warehouse",
  "technology",
]

def populate():
    __createDepartment()
    __createEmployee()
    
    
def __createDepartment():
    for department in departments:
        d = Department.objects.create(name=department)
        d.save()

def __createEmployee():
    choices = []
    dpts = Department.objects.all()
    for dpt in dpts:
        choices.append(dpt)
    for employee in employees:
      
      e = Employee.objects.create(name=employee['name'], email=employee['email'], department=choices[randint(0, 4)])
      e.save()