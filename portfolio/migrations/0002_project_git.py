# Generated by Django 4.0.3 on 2022-04-11 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='git',
            field=models.URLField(blank=True),
        ),
    ]
