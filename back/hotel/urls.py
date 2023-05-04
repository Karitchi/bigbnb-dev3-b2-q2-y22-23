from django.urls import include, path
from rest_framework import routers
from .views import HotelViewSets, HotelListAPIView

router = routers.DefaultRouter()
router.register(r'hotels', HotelViewSets)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('filter_hotels/', HotelListAPIView.as_view(), name='hotel-list')
]
