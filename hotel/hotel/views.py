from rest_framework import generics, permissions

from hotel.hotel import models, serializers


class ListCountryAPIView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.CountrySerializer
    queryset = models.Country.objects.all()
