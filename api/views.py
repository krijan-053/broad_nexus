from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from core.models import Category, Job, JobApplication, Contact

from .serializers import CategorySerializers, JobModelSerializer


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

# video date 4th July 2023 startapp - api-crud - 18:16 min
# video date 6th July 2023 auth token login 12 min
