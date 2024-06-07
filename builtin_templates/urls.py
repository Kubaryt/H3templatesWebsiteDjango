from django.urls import path

from . import views

urlpatterns = [
    path("<str:template_name>/", views.template, name="template"),
    path(
        "<str:template_name>/<str:template_version_name>/",
        views.template_version,
        name="template_version",
    ),
    path(
        "<str:template_name>/<str:template_release_name>/",
        views.template_release,
        name="template_release",
    ),
]
