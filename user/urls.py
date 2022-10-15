from .views import UserView
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register("users", UserView)

urlpatterns = [
    path("", include(router.urls))
]