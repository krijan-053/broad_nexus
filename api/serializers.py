from rest_framework import serializers
from core.models import Category, Job, JobApplication, Contact
from account.models import User, UserProfile


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


class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = ['job', 'user', 'interview_date', 'status']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'account_activated']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'profile_picture', 'resume', 'address', 'phone_number', 'about_me']
