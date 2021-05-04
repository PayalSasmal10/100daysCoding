from django.urls import path

from api_app import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view())
]