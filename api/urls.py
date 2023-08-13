from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, JobViewSet, ContactCreateView , ContactListCreateView

router = DefaultRouter()
router.register('category', CategoryViewSet, basename="category")
router.register('job', JobViewSet, basename="job")
# router.register('c-app', ContactListCreateView, basename="c-app")


urlpatterns = [
                  path("contact-api/",ContactListCreateView.as_view())
              ] + router.urls
