from django.test import TestCase

from builtin_templates.models import BuiltInTemplate, BuiltInTemplateVersion


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
