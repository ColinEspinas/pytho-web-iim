from django.http import HttpRequest
from django.shortcuts import render

from messages.models import Messages

# Create your views here.
def index(request: HttpRequest):
  messages = Messages.objects.all().order_by('created_at')
  return render(request, 'messages/index.html', { 'messages': messages })