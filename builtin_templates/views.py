from django.shortcuts import HttpResponse

# Create your views here.


def template(request, template_name):
    return HttpResponse(f"Template: {template_name}")


def template_version(request, template_name, template_version_name):
    return HttpResponse(f"Template: {template_name}, version {template_version_name}")


def template_release(request, template_name, template_release_name):
    return HttpResponse(f"Template: {template_name}, release {template_release_name}")
