# Generated by Django 4.0.4 on 2022-04-22 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sobrevivente',
            name='qant_denuncias',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
