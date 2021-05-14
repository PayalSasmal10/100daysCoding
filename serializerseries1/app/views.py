# from django.shortcuts import render
# from rest_framework.response import Response
# from .models import Student
# from .serializers import studentSerializer
# from rest_framework.decorators import api_view

# # Create your views here.


# @api_view(['GET'])
# def studentDetails(request):
#     stu = Student.objects.all()
#     serializer = studentSerializer(stu, many=True)
#     return Response(serializer.data)


# @api_view(['POST'])
# def student_creation(request):
#     serializer = studentSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)


# @api_view(['POST'])
# def student_update(request, pk):
#     stu = Student.objects.get(id=pk)
#     serializer = studentSerializer(instance=stu, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
