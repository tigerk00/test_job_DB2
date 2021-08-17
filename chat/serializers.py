from rest_framework import serializers
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Message


class MessageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'author', 'email', 'text')