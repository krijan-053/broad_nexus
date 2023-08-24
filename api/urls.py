from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, JobViewSet, ContactListCreateView, JobApplicationListCreateView,\
    UserView, UserProfileView

router = DefaultRouter()
router.register('category', CategoryViewSet, basename="category")
router.register('job', JobViewSet, basename="job")
router.register('user-profile', UserProfileView, basename="user_profile")
router.register('user',UserView,basename='user')


urlpatterns = [
                    path("contact-api/",ContactListCreateView.as_view()),
                    path("job-application/",JobApplicationListCreateView.as_view()),

              ] + router.urls
