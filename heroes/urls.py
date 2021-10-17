from django.urls import path

from .views import (add_hero, delete_hero, edit_hero, hero_detail_view,
                    heroes_view)

app_name = 'Heroes'

urlpatterns = [
  path('', heroes_view, name='heroes'),
  path('create/', add_hero, name='add_hero'),
  path('<alias>/update/', edit_hero, name='update_hero'),
  path('<alias>/delete/', delete_hero, name='delete_hero'),
  path('<slug>/', hero_detail_view, name='hero_detail'),
]
