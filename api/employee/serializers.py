from rest_framework import serializers
from .models import Employee
from api.department.serializers import DepartmentSerializer
from api.department.models import Department
from .validators import departmentValidation, emailValidation


class EmployeeSerialier(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    department = DepartmentSerializer(required=True)
    
    class Meta:
        model = Employee
        fields = '__all__'
        
    def create(self, validated_data) -> dict[str,any]:
        validation = self.createValidation(validated_data)
        if validation['status']==201:
            department = Department.objects.get(name = str.lower(validated_data['department']['name']))
            Employee.create(validated_data, department)
            validation['message'] = "Employee added."
        return validation
    
    def createValidation(self, data: dict) -> dict[str,any]:
        emailStatus = emailValidation(data)
        departmentStatus = departmentValidation(data)
        if departmentStatus == 201 and emailStatus['status'] == 201:
            return {"status": 201, "message": "All fields valid"}
        else:
            if departmentStatus['status'] != 201:
                return departmentStatus
            else:
                return emailStatus
        
    def update(self, instance, validated_data, pk) -> dict[str,any]:
        validation = self.UpdateValidation(validated_data)
        if validation['status']==200:
            department = Department.objects.get(name = str.lower(validated_data['department']['name']))
            employee = Employee.objects.get(id = pk)
            employee.update(validated_data, department)
            validation['message'] = "Employee updated."
        return validation
    
    def UpdateValidation(self, data: dict) -> dict[str,any]:
        if 'department' in data:
            departmentStatus = departmentValidation(data)
        if 'email' in data:
            emailStatus = emailValidation(data)
        
        if departmentStatus['status'] == 201 and emailStatus['status'] == 201:
            return {"status": 200, "message": "All fields valid"}
        else:
            if departmentStatus['status'] != 201:
                return departmentStatus
            else:
                return emailStatus