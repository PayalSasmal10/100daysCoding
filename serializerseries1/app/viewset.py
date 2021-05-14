from rest_framework import viewsets
from .serializers import studentSerializer
from .models import Student
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


class studentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = studentSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
