from datetime import date

from rest_framework import generics, permissions, response, status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from hotel.booking import serializers
from hotel.booking import models, utils


class CheckBookingAPIView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = models.Booking.objects.all()

    @swagger_auto_schema(
        operation_description="Get document",
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


class BookingsListAPIView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ...
    queryset = models.Booking.objects.all()

    def get_queryset(self):
        return self.queryset.filter()
