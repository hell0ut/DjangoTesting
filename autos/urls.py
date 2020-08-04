from django.views import generic
from django.urls import path

app_name='autos'
urlpatterns=[
    path('',generic.TemplateView.as_view(template_name='autos/auto.html'),name='auto'),
]