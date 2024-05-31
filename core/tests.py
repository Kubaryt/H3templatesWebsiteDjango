from django.test import TestCase

from builtin_templates.models import BuiltInTemplate, BuiltInTemplateVersion
from original_templates.models import OriginalTemplate, OriginalTemplateRelease


class CountingTemplateVersionsTest(TestCase):
    def setUp(self):
        BuiltInTemplate.objects.create(name="test_template")
        BuiltInTemplateVersion.objects.create(
            name="test_template_tp",
            is_recommended=True,
            template=BuiltInTemplate.objects.get(name="test_template"),
        )
        BuiltInTemplateVersion.objects.create(
            name="test_template_1.1",
            is_recommended=False,
            template=BuiltInTemplate.objects.get(name="test_template"),
        )
        BuiltInTemplate.objects.create(name="test_template_2")
        BuiltInTemplateVersion.objects.create(
            name="test_template_2.1",
            is_recommended=True,
            template=BuiltInTemplate.objects.get(name="test_template_2"),
        )

    def test_number_is_count_correctly(self):
        excepted_number_of_version = 2
        number_of_version = BuiltInTemplate.objects.get(
            name="test_template"
        ).number_of_versions()
        self.assertEqual(excepted_number_of_version, number_of_version)


class AuthorsOfTemplateVersionsTest(TestCase):
    def setUp(self):
        OriginalTemplate.objects.create(name="test_template", main_author="author1")
        OriginalTemplateRelease.objects.create(
            name="test_template_tp",
            author="author1",
            short_description="short_description",
            description="description",
            graph="graph",
            release_date="2021-01-01",
            is_recommended=True,
            template=OriginalTemplate.objects.get(name="test_template"),
        )
        OriginalTemplateRelease.objects.create(
            name="test_template_1.1",
            author="author2",
            short_description="short_description",
            description="description",
            graph="graph",
            release_date="2021-01-01",
            is_recommended=False,
            template=OriginalTemplate.objects.get(name="test_template"),
        )

    def test_authors_are_listed_correctly(self):
        excepted_authors = ["author1", "author2"]
        authors = OriginalTemplate.objects.get(name="test_template").releases_authors()
        self.assertEqual(excepted_authors, authors)
