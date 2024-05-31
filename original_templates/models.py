from django.db import models

from core.models import Template, TemplateRelease


class OriginalTemplate(Template):
    main_author = models.CharField(max_length=255)
    other_authors = models.JSONField()
    number_of_releases = models.IntegerField()


class OriginalTemplateRelease(TemplateRelease):
    template = models.ForeignKey(OriginalTemplate, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + self.template.name
