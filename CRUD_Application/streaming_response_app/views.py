# users/views.py

from rest_framework import generics, status
from django.http import StreamingHttpResponse
from .models import UserStream
from .serializers import UserSerializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = UserStream.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        # Generate the streaming content (e.g., CSV data) here
        users = self.get_queryset()
        serialized_users = UserSerializer(users, many=True)

        # Streaming response generator function
        def stream_data():
            for user_data in serialized_users.data:
                yield f"{user_data['name']},{user_data['email']},{user_data['number']}\n"

        # Create a StreamingHttpResponse with the generator function
        response = StreamingHttpResponse(stream_data(), content_type='text/event-stream')
        response['Cache-Control']= 'no-cache',
        return response

    def create(self, request, *args, **kwargs):
        # Your existing create method for POST requests
        return super().create(request, *args, **kwargs)
