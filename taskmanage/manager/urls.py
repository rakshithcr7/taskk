from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, AttendeeViewSet, TaskViewSet, index

router = DefaultRouter()
router.register('events', EventViewSet)
router.register('attendees', AttendeeViewSet)
router.register('tasks', TaskViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # API routes only
    path('', index, name='index'),      # Serve index.html at the root URL
]
