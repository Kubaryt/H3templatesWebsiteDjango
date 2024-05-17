from django.shortcuts import HttpResponse

# Create your views here.


def template(request, template_name):
    return HttpResponse(f"Template: {template_name}")
