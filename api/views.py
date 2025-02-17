from django.http import JsonResponse

def chat_view(request):
    print("hello")
    return JsonResponse({"message": "Hello from the backend!"})