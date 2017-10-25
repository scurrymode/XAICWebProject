from django.shortcuts import render, get_object_or_404
from .models import TopMenu

# Create your views here.

def index(request):
    topMenu = TopMenu.objects.all()
    return render(request, 'web/index.html', {'Menu' : topMenu})

def menu_detail(request, pk):
    menu = get_object_or_404(TopMenu, pk=pk)
    return render(request, 'web/menu_detail.html', {'menu': menu})

