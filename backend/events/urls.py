from django.urls import path
from .views import EventListCreateView, EventRetrieveUpdateDestroyView

urlpatterns = [
    path('', EventListCreateView.as_view(), name='event-list-create'),
    path('<uuid:id>/', EventRetrieveUpdateDestroyView.as_view(), name='event-detail'),
]
