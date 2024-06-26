from django.db import models

from core.models import Template, TemplateRelease


class BuiltInTemplate(Template):
    def number_of_versions(self):
        return BuiltInTemplateVersion.objects.filter(template=self).count()


class BuiltInTemplateVersion(models.Model):
    name = models.CharField(max_length=255)
    is_recommended = models.BooleanField()
    template = models.ForeignKey(BuiltInTemplate, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + self.template.name

    def number_of_releases(self):
        return BuiltInTemplateRelease.objects.filter(template_version=self).count()


class BuiltInTemplateRelease(TemplateRelease):
    template_version = models.ForeignKey(
        BuiltInTemplateVersion, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name + self.template_version.name
