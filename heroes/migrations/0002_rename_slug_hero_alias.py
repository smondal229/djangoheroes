# Generated by Django 3.2.5 on 2021-07-30 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hero',
            old_name='slug',
            new_name='alias',
        ),
    ]
