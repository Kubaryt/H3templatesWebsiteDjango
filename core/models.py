from django.db import models


# Those models are created only for purpose of inheriting them in other apps, so I don't have to copy their code, cuz
# they are similar
class Template(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TemplateRelease(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    short_description = models.TextField()
    description = models.TextField()
    graph = models.ImageField()
    release_date = models.DateField()
    is_recommended = models.BooleanField()
