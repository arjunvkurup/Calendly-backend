import rest_auth.urls
from django.urls import include, path
from .views import CalendlyViewSet, DetailViewSet


urlpatterns = [
    path('', CalendlyViewSet.as_view()),
    path('<int:pk>/', DetailViewSet.as_view()),
    path('auth/', include('rest_auth.urls')),
    path('auth/registration', include('rest_auth.registration.urls')),
]