from rest_framework import serializers
from .models import *
from django_countries.serializers import CountryFieldMixin


class SubjectSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class IdTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdType
        fields = '__all__'
