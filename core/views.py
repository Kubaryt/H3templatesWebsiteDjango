from django.shortcuts import render


def index(request):
    # This is a mock data for the templates
    builtin_templates = [
        {"name": "6lm10a"},
        {"name": "8xm12a"},
        {"name": "h3dm1"}
    ]
    original_templates = [
        {"name": "Conquest"},
        {"name": "Kubaryt"},
        {"name": "Sapphire"}
    ]
    return render(request, "core/index.html", context={
        "original_templates": original_templates,
        "builtin_templates": builtin_templates
    })
