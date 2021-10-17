from rest_framework import serializers

from .models import Hero


class HeroSerializer(serializers.ModelSerializer):
  class Meta:
    model = Hero
    fields = ('name', 'alias', 'gender', 'created_at')
    read_only_fields = ['alias']

class HeroReadOnlySerializer(serializers.Serializer):
  name = serializers.CharField()
  alias = serializers.SlugField()
  gender = serializers.CharField()
  created_at = serializers.DateTimeField()
