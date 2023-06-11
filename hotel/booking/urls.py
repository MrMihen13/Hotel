from django.urls import path

from hotel.booking import views

urlpatterns = [
    path('availability', views.CheckBookingAPIView.as_view()),
    path('<int:number>', views.BookingExtensionAPIView.as_view()),
]
