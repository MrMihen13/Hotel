from django.urls import path

from hotel.hotel import views

urlpatterns = [
    path('countries', views.ListCountryAPIView.as_view()),
]
