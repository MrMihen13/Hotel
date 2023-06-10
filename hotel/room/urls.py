from django.urls import path

from hotel.room import views

urlpatterns = [
    path('rooms', views.ListRoomAPIView.as_view()),
]
