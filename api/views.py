from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from core.models import Category, Job, JobApplication, Contact
from account.models import User, UserProfile

from .serializers import CategorySerializers, JobModelSerializer, ContactSerializer, JobApplicationSerializer, \
    UserProfileSerializer, UserSerializer


# Create your views here.

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class JobViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobModelSerializer


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


class JobApplicationListCreateView(APIView):

    def get(self, *args, **kwargs):
        application = JobApplication.objects.all()
        serializer = JobApplicationSerializer(application, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = JobApplicationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        JobApplication.objects.create(**validated_data)
        return Response(serializer.data)


class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfileView(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
