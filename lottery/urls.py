from django.urls import path
from rest_framework.routers import DefaultRouter
from lottery.views import LotteryView

router = DefaultRouter(trailing_slash=False)

router.register("lottery", LotteryView, basename="lottery")


urlpatterns = router.urls
