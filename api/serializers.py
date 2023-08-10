from rest_framework import serializers
from core.models import Category, Job, JobApplication, Contact


class CategorySerializers(serializers.Serializer):
    title = serializers.CharField(max_length=50)


class JobModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ["title", "description", "category", "application_deadline", "is_active"]

    def create(self, validated_data):
        title = validated_data.pop("address", None)
        email


class ContactSerializer(serializers.Serializer):
    class Meta:
        model = Contact
        fields = ["name", "email", "phone_number", "message"]
