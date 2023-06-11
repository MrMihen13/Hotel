from datetime import date

from rest_framework import generics, permissions, response, status, exceptions
from django.shortcuts import get_object_or_404

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from hotel.booking import serializers
from hotel.booking import models, utils


class CheckBookingAPIView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = models.Booking.objects.all()

    @swagger_auto_schema(
        operation_description="Проверка возможности бронирования",
        manual_parameters=[
            openapi.Parameter(
                type=openapi.TYPE_STRING, in_=openapi.IN_QUERY, name='start', required=True,
                default=date.today().strftime('%Y-%m-%d'),
                description='Date start of booking'
            ),
            openapi.Parameter(
                type=openapi.TYPE_STRING, in_=openapi.IN_QUERY, name='end', required=False,
                description='Date end of booking'
            )
        ],
    )
    def get(self, request, *args, **kwargs):
        serializer = serializers.AvailabilityBookingSerializers(data={
            'is_available': utils.check_booking_availability(date_start=self.request.GET.get('start'),
                                                             date_end=self.request.GET.get('end'))})
        if serializer.is_valid(raise_exception=True):
            return response.Response(data=serializer.data, status=status.HTTP_200_OK)
        return response.Response(status=status.HTTP_400_BAD_REQUEST)


class BookingExtensionAPIView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = models.Booking.objects.all()

    @swagger_auto_schema(
        operation_description="Продление бронирования",
        manual_parameters=[
            openapi.Parameter(
                type=openapi.TYPE_STRING, in_=openapi.IN_QUERY, name='start', required=True,
                default=date.today().strftime('%Y-%m-%d'),
                description='Date start of booking'
            ),
            openapi.Parameter(
                type=openapi.TYPE_STRING, in_=openapi.IN_QUERY, name='end', required=False,
                description='Date end of booking'
            )
        ],
    )
    def get(self, request, number, *args, **kwargs):
        booking = get_object_or_404(self.queryset, number=number)
        date_start = self.request.GET.get('start')
        date_end = self.request.GET.get('end')

        if not utils.check_booking_availability(date_start=date_start, date_end=date_end):
            raise exceptions.APIException(
                detail='Невозможно продлить бронирование на данные даты.', code=status.HTTP_405_METHOD_NOT_ALLOWED)

        booking.date_end = date_end
        booking.save()
        return response.Response(data=booking, status=status.HTTP_200_OK)
