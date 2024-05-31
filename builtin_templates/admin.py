from django.contrib import admin

from .models import BuiltInTemplate, BuiltInTemplateVersion, BuiltInTemplateRelease

admin.site.register(BuiltInTemplate)
admin.site.register(BuiltInTemplateVersion)
admin.site.register(BuiltInTemplateRelease)
