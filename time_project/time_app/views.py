from django.shortcuts import render, redirect
from time import gmtime, strftime, localtime

# Create your views here.
def index(request):
  context = {
    "time": strftime("%m-%d-%Y %I:%M %p", localtime())
  }
  return render(request, 'index.html', context)
