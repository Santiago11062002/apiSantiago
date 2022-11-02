from rest_framework import routers
from .api import BarsaviewSet

router = routers.DefaultRouter()
router.register('api/ApiBarsa',BarsaviewSet,'ApiBarsa')

urlpatterns=router.urls