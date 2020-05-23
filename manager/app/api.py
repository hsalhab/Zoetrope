from app.models import App
from rest_framework import viewsets, permissions
from .serializers import AppSerializer

class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AppSerializer 