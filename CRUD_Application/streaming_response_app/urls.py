from django.urls import path
from .views import UserListCreateView

urlpatterns = [
    path('fetchStreamUsers/', UserListCreateView.as_view()),
]
