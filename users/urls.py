from rest_framework.routers import DefaultRouter

from users.views import UserViewSet

# Описание маршрутизации для ViewSet
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
urlpatterns = router.urls