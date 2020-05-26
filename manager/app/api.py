from app.models import App
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import AppSerializer
from .movie_engine import engine

class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AppSerializer 

class MovieViewSet(viewsets.ModelViewSet):
    def list(self, request, *args, **kwargs):
        data = engine.get_random_movie()
        return Response(data)
