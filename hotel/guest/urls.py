from django.urls import path

from hotel.guest import views

urlpatterns = [
    path('guests', views.ListGuestAPIView.as_view()),
]
