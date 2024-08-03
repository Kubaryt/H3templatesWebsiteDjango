from django.db import models

from core.models import TemplateBase, TemplateReleaseBase


class OriginalTemplate(TemplateBase):
    main_author = models.CharField(max_length=255)

    def get_recommended_template_release(self):
        return OriginalTemplateRelease.objects.get(template=self, is_recommended=True)

    def get_template_release(self):
        return list(OriginalTemplateRelease.objects.filter(template=self))

    def number_of_releases(self):
        return OriginalTemplateRelease.objects.filter(template=self).count()

    def releases_authors(self):
        return list(OriginalTemplateRelease.objects.filter(template=self).values_list('author', flat=True))


class OriginalTemplateRelease(TemplateReleaseBase):
    template = models.ForeignKey(OriginalTemplate, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + "-" + self.template.name
