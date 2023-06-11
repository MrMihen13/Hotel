from django.urls import path, include


urlpatterns = [
    path('', include('djoser.urls.base')),
    path('auth/', include('djoser.urls.jwt')),
]
