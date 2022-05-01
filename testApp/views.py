import json
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from testApp.models import Question

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
  questions = Question.objects.all()
  return render(request, 'testApp/index.html', { 'questions': questions })

def edit(request: HttpRequest, id: int) -> HttpResponse | HttpResponseRedirect:
  question = Question.objects.get(pk=id)
  if request.method == 'GET':
    return render(request, 'testApp/edit.html', { 'question': question })
  elif request.method == 'POST':
    question.text = request.POST['text']
    question.save()
    return redirect('index')

def create(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
  if request.method == 'GET':
    return render(request, 'testApp/add.html')
  elif request.method == 'POST':
    question = Question(text=request.POST['text'])
    question.save()
    return redirect('index')

def delete(request: HttpRequest, id: int) -> HttpResponseRedirect:
  question = Question.objects.get(pk=id)
  question.delete()
  return redirect('index')