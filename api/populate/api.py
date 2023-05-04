from rest_framework import viewsets
from rest_framework.response import Response
from .serializer import PopulateSerializer
from .utils import populate


class PopulateViewSet(viewsets.ViewSet):
    serializer_class = PopulateSerializer
    

    @staticmethod
    def create(request):
        populate()

        return Response()