from .models import Tag, Profession
from rest_framework import serializers


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ProfessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profession
        fields = '__all__'