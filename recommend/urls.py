from django.urls import path
from . import views

urlpatterns = [
    path('', views.pr_recommend),
]