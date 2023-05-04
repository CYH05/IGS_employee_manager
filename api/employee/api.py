from rest_framework import viewsets
from .models import Employee
from.serializers import EmployeeSerialier
from rest_framework.response import Response

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerialier
    
    def create(self, request, *args, **kwargs) -> Response:
        serializer = self.serializer_class(request.data)        
        response = serializer.create(request.data)
        return Response(status=response['status'], data={"message": response["message"]})
    
    def partial_update(self, request, pk=None, *args, **kwargs) -> Response:
        serializer = self.serializer_class(request.data)        
        response = serializer.update(serializer, request.data, pk)
        return Response(status=response['status'], data={"message": response["message"]})