from rest_framework import serializers
from core.models import Category, Job, JobApplication, Contact


# Create your serializers here.

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "title"]


class JobModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ["title", "description", "category", "application_deadline", "is_active"]


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ["name", "email", "phone_number", "message"]
