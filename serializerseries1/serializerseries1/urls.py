from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app import viewset
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()
router.register("app", viewset.studentViewset, basename="app")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('gettoken/', TokenObtainPairView.as_view(), name='gettoken'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='refreshtoken'),
    path('verifytoken/', TokenVerifyView.as_view(), name='verifytoken')
    # path('admin/', admin.site.urls),
]
