from django.urls import path

from . import views, add_item

urlpatterns = [
    path('', views.index, name='index'),
    path('add', add_item, name='add')
]