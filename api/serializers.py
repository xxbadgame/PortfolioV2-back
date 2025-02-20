from rest_framework import serializers

class ChatSerializer(serializers.Serializer):
    data = serializers.CharField(max_length=1000)