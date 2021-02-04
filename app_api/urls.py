from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers

from api.serializer.owner_serializer import OwnersSearchByUserName
from api.view.farm_view import FarmsViewSet
from api.view.owner_view import OwnersViewSet
from api.view.planting_view import PlantingsViewSet
from api.view.sampling_point_view import SamplingPointsViewSet
from api.view.users_view import CreateNewUser

router = routers.DefaultRouter()
router.register('farms', FarmsViewSet, basename='Farm')
router.register('owners', OwnersViewSet, basename='Owner')
router.register('plantings', PlantingsViewSet, basename='Planting')
router.register('sampling-points', SamplingPointsViewSet, basename='Sampling Point')
router.register('owners-search-by-username', OwnersSearchByUserName, basename='Clients Search By Name')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('users/', CreateNewUser.as_view()),

    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
