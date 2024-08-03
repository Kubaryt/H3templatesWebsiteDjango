# Generated by Django 5.0.6 on 2024-06-17 21:09

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
                ('templatebase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.templatebase')),
            ],
            bases=('core.templatebase',),
        ),
        migrations.CreateModel(
            name='BuiltInTemplateVersion',
            fields=[
                ('templatebase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.templatebase')),
                ('is_recommended', models.BooleanField()),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builtin_templates.builtintemplate')),
            ],
            bases=('core.templatebase',),
        ),
        migrations.CreateModel(
            name='BuiltInTemplateRelease',
            fields=[
                ('templatereleasebase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.templatereleasebase')),
                ('template_version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builtin_templates.builtintemplateversion')),
            ],
            bases=('core.templatereleasebase',),
        ),
    ]
