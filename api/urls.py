from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import ContactCreateView, JobViewSet, CategoryViewSet

router = DefaultRouter()
router.register('category', CategoryViewSet, basename="category")
router.register('job', JobViewSet, basename="job")

urlpatterns = [
                  path("contact-api/", ContactCreateView.as_view())
              ] + router.urls
