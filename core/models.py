from django.db import models


# Those models are created only for purpose of inheriting them in other apps, so I don't have to copy their code, cuz
# they are similar
class TemplateBase(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name


class TemplateReleaseBase(TemplateBase):
    author = models.CharField(max_length=255)
    graph = models.ImageField()
    release_date = models.DateField()
    is_recommended = models.BooleanField()
