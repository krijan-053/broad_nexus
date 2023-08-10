from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from core.models import Category, Job, JobApplication, Contact

from .serializers import CategorySerializers, JobModelSerializer


# Create your views here.

class CategoryListCreateView(APIView):
    def get(self, *args, **kwargs):
        category = Category.objects.all()
        serializer = CategorySerializers(category, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = CategorySerializers(data=data)
        serializer.is_valid(raise_exception=True)
        title = serializer.validated_data.get('title')
        Category.objects.create(title=title)
        return Response(serializer.data)


# class JobListView(APIView):
#
#     def get(self, *args, **kwargs):
#         job_list = []
#         for job in Job.objects.all():
#             job = {
#                 "title": job.title,
#                 "description": job.description,
#                 "category": job.category.title,
#                 "application_deadline": job.application_deadline,
#                 "is_active": job.is_active,
#             }
#             job_list.append(job)
#         return Response(job_list)


class JobAPIView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Job.objects.all()
        serializer = JobModelSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = JobModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        Job.objects.create(**validated_data)
        return Response(serializer.data)


class JobViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobModelSerializer


class ContactCreateView(CreateAPIView):
    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = seralizer.validated_data
        Contact.objects.create(**validated_data)
        return Response(serializer.data)


# video date 4th July 2023 startapp - api-crud - 18:16 min
# video date 6th July 2023 auth token login 12 min