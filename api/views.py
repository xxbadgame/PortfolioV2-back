from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ChatSerializer
from .api_service import ApiService

@api_view(['POST'])
def chat_view(request):
    serializer = ChatSerializer(data=request.data)
    if serializer.is_valid():
        message = serializer.validated_data['data']
        mistral_service = ApiService()
        agent_id = "ag:99d3226f:20250217:yannis-ai:cfd93f55"
        response = mistral_service.get_chat_response(agent_id, message)
        return Response({'responseYAI': response}, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)