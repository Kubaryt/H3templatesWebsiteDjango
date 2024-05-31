from django.contrib import admin

from .models import OriginalTemplate, OriginalTemplateRelease

admin.site.register(OriginalTemplate)
admin.site.register(OriginalTemplateRelease)
