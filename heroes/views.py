import timeit

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Hero
from .serializers import HeroReadOnlySerializer, HeroSerializer

# Create your views here.

@api_view(['GET', ])
def hero_detail_view(request, slug):
  try:
    hero = Hero.objects.get(alias=slug)
  except:
    return Response(status=status.HTTP_404_NOT_FOUND,)

  serialized_data = HeroSerializer(hero)
  return Response(serialized_data.data)

@api_view(['GET', ])
def heroes_view(request):
  heroes = Hero.objects.all()

  serialized_data = HeroSerializer(heroes, many = True)
  print(timeit.timeit(lambda: HeroSerializer(heroes, many = True), number=10000))

  print(timeit.timeit(lambda: HeroReadOnlySerializer(heroes, many = True), number=10000))
  # HeroReadOnlySerializer(heroes, many = True)

  return Response(serialized_data.data)

@api_view(['PUT', ])
def edit_hero(request, alias):
  try:
    hero_obj = Hero.objects.get(alias = alias)
  except:
    return Response(status=status.HTTP_404_NOT_FOUND)

  serializer_data = HeroSerializer(hero_obj, data=request.data)
  data = {}

  if serializer_data.is_valid():
    serializer_data.save()
    data['success'] = 'Update Successful'
    return Response(data = data)

  return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE', ])
def delete_hero(request, alias):
  try:
    hero_obj = Hero.objects.get(alias=alias)
  except:
    return Response(status=status.HTTP_404_NOT_FOUND)

  data = {}

  if hero_obj.delete():
    data['success'] = 'Delete Successful'
    return Response(data = data)
  else:
    data['failure'] = 'Delete Failed'

  return Response(data=data)

@api_view(['POST'])
def add_hero(request):
  serializer = HeroSerializer(data=request.data)

  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

