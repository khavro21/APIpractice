from rest_framework import serializers
from .models import Pet


class PetSerializer(serializers.ModelSerializer):
    poster_id = serializers.ReadOnlyField(source='poster.id')
    poster = serializers.ReadOnlyField(source='poster.username')

    class Meta:
        model = Pet
        fields = ['id', 'category', 'name', 'tags', 'status', 'poster_id', 'photoUrls', 'poster', 'created']
