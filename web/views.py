from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import TopMenu, SubMenu

# Create your views here.

def index(request):
    topMenu = TopMenu.objects.all()
    return render(request, 'web/index.html', {'Menu' : topMenu})

def menu_detail(request, submenu):
    topMenu = get_object_or_404(TopMenu, titleen=submenu)
    topMenu_id = TopMenu.objects.get(titleen=submenu)
    subMenus = get_list_or_404(SubMenu, topmenu_id=topMenu_id.pk)
    return render(request, 'web/menu_detail.html', {'topMenu': topMenu, 'subMenus': subMenus })

