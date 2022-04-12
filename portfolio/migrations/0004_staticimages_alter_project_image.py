# Generated by Django 4.0.3 on 2022-04-12 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_project_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaticImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=250)),
                ('image', models.ImageField(upload_to='portfolio/static')),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='portfolio/project'),
        ),
    ]
