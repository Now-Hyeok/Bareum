from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login',views.login_user),
    path('signup',views.signup),
    path('kakao/login',views.KakaoLogin.as_view())
]