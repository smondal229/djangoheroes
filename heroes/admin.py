from django.contrib import admin

from .models import Hero


# Register your models here.
class HeroAdmin(admin.ModelAdmin):
  list_display = ('name', 'alias', 'gender')
  search_fields=('name', )
  prepopulated_fields = {"alias": ("name",)}

admin.site.register(Hero, HeroAdmin)
