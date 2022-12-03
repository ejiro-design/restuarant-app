from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Menu
from .models import Bookings


def index(request):
    context = {'menu': "", 'error': "", 'success': ""}
    if (request.POST):
        try:
            existing = Bookings.objects.get(name=request.POST['name'], email=request.POST['email'], date=request.POST['date'], time=request.POST['time'])
            context['error'] = 'Double booking detected'
        except:
            menuOption = Menu.objects.get(id=request.POST['menu'])
            query = Bookings(name=request.POST['name'], email=request.POST['email'], menu=menuOption, seats=request.POST['seats'], date=request.POST['date'], time=request.POST['time'])
            query.save()
            context['success'] = "Booking sucessfull"
    menuItems = Menu.objects.order_by('name')
    template = loader.get_template('reservation/index.html')
    context['menu'] = menuItems
    return HttpResponse(template.render(context, request))


# @login_required
def manage(request):
    context = {'bookings': "", 'error': "", 'success': ""}
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        Bookings.objects.filter(id=item_id).delete()  

    bookings = Bookings.objects.all()
    template = loader.get_template('reservation/manage.html')
    context['bookings'] = bookings
    return HttpResponse(template.render(context, request))
