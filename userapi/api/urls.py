from django.urls import include, path
# from userapi.api.views import ProfileList
from rest_framework.routers import DefaultRouter
from userapi.api.views import AvatarUpdateView, ProfileViewSet, ProfileStatusViewSet

router = DefaultRouter()
router.register(r"profiles", ProfileViewSet)
router.register(r"status", ProfileStatusViewSet, basename="status-list")

urlpatterns = [
    path("", include(router.urls)),
    path("avatar/", AvatarUpdateView.as_view(), name="avatar-update"),
]
