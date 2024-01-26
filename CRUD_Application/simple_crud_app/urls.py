
from django.urls import path
from .views import UserListCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path('fetch_Create_Users/', UserListCreateView.as_view()),
    path('Delete_Update_User/<int:pk>/', UserRetrieveUpdateDestroyView.as_view()),
]
