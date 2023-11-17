from django.shortcuts import get_object_or_404, render
from superhero_app.models import Message

def message_detail_view(request, pk):
    message = get_object_or_404(Message, pk=pk)
    return render(request, 'message_detail.html', {'message': message})
