from django.contrib import admin
from django.urls import path
from api.views import chat_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/chat/', chat_view),
]
