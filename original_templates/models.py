from django.db import models

from core.models import Template, TemplateRelease


class OriginalTemplate(Template):
    main_author = models.CharField(max_length=255)

    def number_of_releases(self):
        return OriginalTemplateRelease.objects.filter(template=self).count()

    def releases_authors(self):
        return list(OriginalTemplateRelease.objects.filter(template=self).values_list('author', flat=True))


class OriginalTemplateRelease(TemplateRelease):
    template = models.ForeignKey(OriginalTemplate, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + "-" + self.template.name
