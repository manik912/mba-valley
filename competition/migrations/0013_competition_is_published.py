# Generated by Django 3.0.7 on 2020-09-26 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0012_auto_20200925_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
