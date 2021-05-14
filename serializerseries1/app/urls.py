from django.contrib import admin
from django.urls import path, include
#from app import views
from rest_framework.routers import DefaultRouter
from .viewset import studentViewset

router = DefaultRouter()
router.register("app", studentViewset, basename="app")

urlpatterns = [
    # path('students/', views.studentDetails, name='students'),
    # path('create/', views.student_creation, name='create'),
    # path('update/<str:pk>/', views.student_update, name='update')
    path('', include(router.urls)),
]
