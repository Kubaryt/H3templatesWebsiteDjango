from django.shortcuts import render

from builtin_templates.models import BuiltInTemplate
from original_templates.models import OriginalTemplate


def index(request):
    builtin_templates = BuiltInTemplate.objects.all()
    original_templates = OriginalTemplate.objects.all()
    return render(
        request,
        "core/index.html",
        context={
            "original_templates": original_templates,
            "builtin_templates": builtin_templates,
        },
    )
