
from django.urls import path
from superhero_app.views import MessageDetailView

urlpatterns = [
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='message-detail'),
]
