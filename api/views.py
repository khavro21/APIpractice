from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Pet
from .serializers import PetSerializer
from django.core.exceptions import ValidationError


class PetList(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)


class GetOnePet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # In order to delete an object, we need to make sure that the user is the same who created it. The same for put
    def delete(self, request, *args, **kwargs):
        pet = Pet.objects.filter(pk=kwargs['pk'], poster=self.request.user)
        if pet.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError('This pet was not created by you!')

    def put(self, request, *args, **kwargs):
        pet = Pet.objects.filter(pk=kwargs['pk'], poster=self.request.user)
        if pet.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError('This pet was not created by you!')
