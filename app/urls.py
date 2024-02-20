from rest_framework.routers import DefaultRouter

from .views import CatViewSets

router = DefaultRouter()
router.register('cat', CatViewSets, basename='cat')


urlpatterns = router.urls
