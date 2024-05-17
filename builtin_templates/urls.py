from django.urls import path

from . import views

urlpatterns = [
    path("<str:template_name>/", views.template, name="template"),
]
