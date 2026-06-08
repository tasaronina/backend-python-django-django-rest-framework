from rest_framework.routers import DefaultRouter

from .views import NewsImageViewSet, NewsMaterialViewSet, NewsViewSet


router = DefaultRouter()
router.register("news-materials", NewsMaterialViewSet, basename="news-materials")
router.register("news", NewsViewSet, basename="news")
router.register("news-images", NewsImageViewSet, basename="news-images")

urlpatterns = router.urls
