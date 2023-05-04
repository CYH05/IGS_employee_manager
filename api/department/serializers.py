from rest_framework import serializers
from .models import Department

from .validators import departmentNameValidator, departmentUpdateValidation

class DepartmentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    
    class Meta:
        model = Department
        fields = '__all__'
        
    def create(self, validated_data: dict) -> dict[str, any]:
        validation = self.createValidation(validated_data)
        if validation['status']==200:
            Department.create(validated_data)
            validation['status'] = 201
            validation['message'] = "Department added."
        return validation
    
    def update(self, instance, validated_data: dict, pk: int) -> dict[str, any]:
        validation = self.UpdateValidation(validated_data, pk)
        if validation['status']==200:
            department = Department.objects.get(id=pk)
            department.update(validated_data)
            validation['message'] = "Department updated."
        return validation
    
    
    # If any of these actions need more validators the functions will be called and treated here.
    def createValidation(self, data: dict) -> dict[str, any]:
        return departmentNameValidator(data)
    
    def UpdateValidation(self, data: dict, id: int) -> dict[str, any]:
        return departmentUpdateValidation(data, id)