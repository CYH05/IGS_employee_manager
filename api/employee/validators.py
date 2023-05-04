from .models import Employee
from api.department.models import Department

def emailValidation(data: dict) -> dict[str,any]:
    status= 201
    message = "Email valid."
    try:
        Employee.objects.get(email=data['email'])
        status = 400
        message = "The e-mail '{}' is already in use.".format(data['email'])
    finally:
        return {"status": status, "message": message}
      

def departmentValidation(data: dict) -> dict[str,any]:
    status= 201
    message = "Department valid."
    try:
        Department.objects.get(name = str.lower(data['department']['name']))
    except Department.DoesNotExist:
        status = 400
        message = "There isn't a department with name: {}".format(data['department']['name'])   
    finally:
        return {"status": status, "message": message}