from django.urls import path
from . import views 

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),



    path('', views.getRoutes),
    path('products/', views.getProducts),
    path('products/<str:pk>/', views.getProduct),
    path('products/<str:pk>/vote/', views.productVote),

    path('remove-tag/', views.removeTag)

]