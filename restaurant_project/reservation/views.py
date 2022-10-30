from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Menu
from .models import Bookings

def index(request):
    template = loader.get_template('reservation/index.html')
    context = {
        'menu':['Jollof Rice', 'Beans porridge', 'Potato Fries', 'Egusi soup']
    }
    return HttpResponse(template.render(context, request))