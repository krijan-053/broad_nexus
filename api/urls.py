from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import CategoryListCreateView, JobAPIView, ContactCreateView, JobViewSet

# from .views import JobListView

router = DefaultRouter()
router.register('job-viewset', JobViewSet, basename="job")

urlpatterns = [
                  path("category-api/", CategoryListCreateView.as_view()),
                  # path("job-list/", JobListView.as_view()),
                  path("job-api/", JobAPIView.as_view()),
                  path("contact-api/", ContactCreateView.as_view())
              ] + router.urls
