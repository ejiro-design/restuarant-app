from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Menu
from .models import Bookings

def index(request):
    if (request.POST):
        menuOption = Menu.objects.get(id=request.POST['menu'])
        query = Bookings(name=request.POST['name'], email=request.POST['email'], menu=menuOption, seats=request.POST['seats'], date=request.POST['date'], time=request.POST['time'])
        query.save()
    menuItems = Menu.objects.order_by('name')
    template = loader.get_template('reservation/index.html')
    context = {
        'menu': menuItems
    }
    return HttpResponse(template.render(context, request))