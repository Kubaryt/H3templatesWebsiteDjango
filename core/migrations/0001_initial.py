# Generated by Django 5.0.6 on 2024-05-31 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TemplateRelease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('short_description', models.TextField()),
                ('description', models.TextField()),
                ('graph', models.ImageField(upload_to='')),
                ('release_date', models.DateField()),
                ('is_recommend', models.BooleanField()),
            ],
        ),
    ]
