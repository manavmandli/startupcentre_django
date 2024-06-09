import django
from django.urls import reverse
from startup_app.models import Contact,FreeQuote
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')