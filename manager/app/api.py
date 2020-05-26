from app.models import App
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import AppSerializer

class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AppSerializer 

class MovieViewSet(viewsets.ModelViewSet):
    def list(self, request, *args, **kwargs):
        data = {
            'message': 'hi how are ya'
        }
        return Response(data)
