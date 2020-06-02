from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from api import views
from django.urls import path

router = DefaultRouter(trailing_slash=False)
router.register(r"stocks", views.StockViewSet, basename="stocks")
router.register(r"rebalance",rest_algo.rebalancing, name="PostRebalance")
urlpatterns = router.urls