from django.urls import path, re_path
from . import views
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
# from rest_framework import permissions

# schema_view = get_schema_view(
#     openapi.Info(
#         title="Snippets API",
#         default_version='v1',
#         description="Test description",
#         terms_of_service="https://www.google.com/policies/terms/",
#         contact=openapi.Contact(email="contact@snippets.local"),
#         license=openapi.License(name="BSD License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )

urlpatterns = [
    path('category/', views.CategoryAPI.as_view()),
    path('products/', views.ProductsAPI.as_view()),
    path('contact/', views.ContactAPI.as_view()),
    path('social_link/', views.SocialLinkAPI.as_view()),
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
