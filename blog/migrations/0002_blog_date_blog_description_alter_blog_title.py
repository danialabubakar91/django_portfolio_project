# Generated by Django 4.0.3 on 2022-03-25 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
