from django.urls import path

from . import views

urlpatterns = [
    path('bookings/', views.all_bookings),
    path('bookings/<int:booking_id>/', views.bookings_details),
    path('set_booking_read/<int:booking_id>/', views.set_read),
    path('set_booking_approved/<int:booking_id>/', views.set_approved)
]
