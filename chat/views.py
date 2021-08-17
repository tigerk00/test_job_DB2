from rest_framework import generics
from .models import Message
from .serializers import MessageSerializer, MessageListSerializer
from .pagination import MessagesPagination

class MessageList(generics.ListAPIView):
    queryset = Message.objects.all()
    pagination_class = MessagesPagination
    serializer_class = MessageListSerializer

class MessageDetail(generics.RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class MessageCreate(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer