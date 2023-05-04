from rest_framework import viewsets
from .models import Department
from.serializers import DepartmentSerializer
from rest_framework.response import Response

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    
    def create(self, request, *args, **kwargs) -> Response:
        serializer = self.serializer_class(request.data)        
        response = serializer.create(request.data)
        return Response(status=response['status'], data={"message": response["message"]})
    
    def partial_update(self, request, pk=None, *args, **kwargs )-> Response:
        serializer = self.serializer_class(request.data)        
        response = serializer.update(serializer, request.data, pk)
        return Response(status=response['status'], data={"message": response["message"]})