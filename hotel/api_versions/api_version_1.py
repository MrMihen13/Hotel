from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Hotel API",
        default_version='v1',
        description="Test description",
        contact=openapi.Contact(email="test@mail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='chema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='chema-redoc'),

    path('', include('hotel.room.urls')),
    path('', include('hotel.guest.urls')),
    path('', include('hotel.hotel.country_urls')),
    path('booking/', include('hotel.booking.urls')),
    path('', include('hotel.cauth.urls'))
]
