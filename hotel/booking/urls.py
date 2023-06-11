from django.urls import path

from hotel.booking import views

urlpatterns = [
    path('availability', views.CheckBookingAPIView.as_view()),
]
