from django.db import models

from core.models import Template, TemplateRelease


class BuiltInTemplate(Template):
    number_of_version = models.IntegerField()


class BuiltInTemplateVersion(models.Model):
    name = models.CharField(max_length=255)
    number_of_releases = models.IntegerField()
    is_recommend = models.BooleanField()
    template = models.ForeignKey(BuiltInTemplate, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + self.template.name


class BuiltInTemplateRelease(TemplateRelease):
    template_version = models.ForeignKey(BuiltInTemplateVersion, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + self.template_version.name
