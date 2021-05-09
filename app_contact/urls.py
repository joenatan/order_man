from rest_framework import routers

from .views import ContactApiView

router = routers.DefaultRouter()
router.register('contacts', ContactApiView)

urlpatterns = router.urls