from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify


# Create your models here.
class Hero(models.Model):
  name = models.CharField(null= False, blank=False, max_length=60)
  alias = models.SlugField(null= False, blank=False, unique=True)
  gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), default='M')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

  class Meta:
    indexes = [
      models.Index(fields=['alias'])
    ]

@receiver(pre_save, sender=Hero)
def save_hero(sender, instance, **kwargs):
  instance.alias = slugify(instance.name)
