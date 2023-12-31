from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('detail/<str:product_code>/', views.ProductDetailView.as_view()),
    path('online-reviews/<str:product_code>/', views.ReviewList.as_view(), name='review-list'),
    path('bareum-reviews/<str:product_code>/', views.BareumReviewList.as_view(), name='bareum-review-list'),
    path('my-reviews/<int:member_id>/',views.MyReviewList.as_view(),name='my-review-list'),
    path('total-ranking/',views.TotalRankingList.as_view()),
    path('search/', views.search_nutraceuticals, name='search_nutraceuticals'),
    path('age-ranking/',views.AgeRankingList.as_view()),
    path('brand-ranking/',views.BrandRankingList.as_view()),
    path('category-ranking/',views.CateogryRankingList.as_view()),
    path('ingredient-ranking/<str:ingredient>/',views.IngredientRankingList.as_view()),
    
    
]
