from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('hotel_owners/', include('hotel_owner.urls')),
    path('cities/', include('city.urls')),
    path('clients/', include('client.urls')),
    path('hotels/', include('hotel.urls')),
    path('bookings/', include('booking.urls')),
    path('token/', include('user.urls')),
    path('reviews/', include('review.urls')),
    path('admin/', admin.site.urls)
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
