from .models import Department
from django.db.models import Q

def departmentNameValidator(data: dict) -> dict[str, any]:
    status= 200
    message = ""
    try:
        Department.objects.get(name=str.lower(data['name']))
        status = 400
        message = "This department name is already in use."            
    finally:
        return {"status": status, "message": message}
      
def departmentUpdateValidation(data: dict, id: int) -> dict[str, any]:
    status= 200
    message = ""
    try:
        Department.objects.get(~Q(id=id), name=data['name'])
        status = 400
        message = "This department name is already in use."  
    except Department.DoesNotExist:
        message = "Department updated."        
    return {"status": status, "message": message}