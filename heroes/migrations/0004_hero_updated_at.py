# Generated by Django 3.2.5 on 2021-07-31 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0003_hero_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
