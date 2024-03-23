from django.urls import path
from .views import tables

urlpatterns = [
    path('', tables, name='tables'),  # This should display the chat template at '127.0.0.1:8000/chat'
]
