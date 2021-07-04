from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Pet
from .serializers import PetSerializer


class PetList(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)
