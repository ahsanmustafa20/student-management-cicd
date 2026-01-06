from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Option A: Simple text response
def homepage(request):
    return HttpResponse("<h1>Welcome to Student Management System Ahsan Mustafa</h1>")