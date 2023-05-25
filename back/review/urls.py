from django.urls import include, path
from rest_framework import routers
from .views import ClientReviewViewSet, hotel_review_list

router = routers.DefaultRouter()
router.register(r'reviews', ClientReviewViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('hotel/<int:hotel_id>/', hotel_review_list, name='hotel_review_list'),
]