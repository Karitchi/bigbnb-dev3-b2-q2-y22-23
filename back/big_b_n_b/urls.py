from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('hotel_owners/', include('hotel_owner.urls')),
    path('cities/', include('city.urls')),
    path('clients/', include('client.urls')),
    path('hotels/', include('hotel.urls')),
    path('bookings/', include('booking.urls')),
    path('token/', include('user.urls')),
    path('admin/', admin.site.urls)
]
