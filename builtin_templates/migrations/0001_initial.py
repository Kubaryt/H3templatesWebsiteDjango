# Generated by Django 5.0.6 on 2024-05-31 16:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuiltInTemplate',
            fields=[
                ('template_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.template')),
            ],
            bases=('core.template',),
        ),
        migrations.CreateModel(
            name='BuiltInTemplateVersion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_recommended', models.BooleanField()),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builtin_templates.builtintemplate')),
            ],
        ),
        migrations.CreateModel(
            name='BuiltInTemplateRelease',
            fields=[
                ('templaterelease_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.templaterelease')),
                ('template_version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builtin_templates.builtintemplateversion')),
            ],
            bases=('core.templaterelease',),
        ),
    ]
