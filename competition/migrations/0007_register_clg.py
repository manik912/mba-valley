# Generated by Django 3.0.7 on 2020-09-22 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0006_submit'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='clg',
            field=models.CharField(default='your college', max_length=50),
        ),
    ]
