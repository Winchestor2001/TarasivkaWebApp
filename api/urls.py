from django.urls import path
from . import views


urlpatterns = [
    path('category/', views.CategoryAPI.as_view()),
    path('products/', views.ProductsAPI.as_view()),
    path('contact/', views.ContactAPI.as_view()),
    path('social_link/', views.SocialLinkAPI.as_view()),
]
