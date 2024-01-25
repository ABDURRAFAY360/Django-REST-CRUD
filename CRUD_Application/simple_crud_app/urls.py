
from django.urls import path
from .views import UserListCreateView

urlpatterns = [
    path('fetch_Create_Users/', UserListCreateView.as_view()),
]
