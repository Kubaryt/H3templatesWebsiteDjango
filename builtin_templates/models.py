from django.db import models

from core.models import TemplateBase, TemplateReleaseBase


class BuiltInTemplate(TemplateBase):
    def get_recommended_template_version(self):
        return BuiltInTemplateVersion.objects.get(template=self, is_recommended=True)

    def get_template_versions(self):
        return list(BuiltInTemplateVersion.objects.filter(template=self))

    def number_of_versions(self):
        return BuiltInTemplateVersion.objects.filter(template=self).count()


class BuiltInTemplateVersion(TemplateBase):
    is_recommended = models.BooleanField()
    template = models.ForeignKey(BuiltInTemplate, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + self.template.name

    def get_version_releases(self):
        return list(BuiltInTemplateRelease.objects.filter(template_version=self))

    def get_recommended_release(self):
        return BuiltInTemplateRelease.objects.get(template_version=self, is_recommended=True)

    def number_of_releases(self):
        return BuiltInTemplateRelease.objects.filter(template_version=self).count()


class BuiltInTemplateRelease(TemplateReleaseBase):
    template_version = models.ForeignKey(BuiltInTemplateVersion, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + self.template_version.name
