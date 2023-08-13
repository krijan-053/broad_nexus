from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from core.models import Category, Job, JobApplication, Contact

from .serializers import CategorySerializers, JobModelSerializer, ContactSerializer


# Create your views here.

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


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

class ContactListCreateView(APIView):

    def get(self, *args, **kwargs):
        contact = Contact.objects.all()
        serializer = ContactSerializer(contact, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        Contact.objects.create(**validated_data)
        return Response(serializer.data)
