from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import TopMenu, SubMenu, Greeting, Member, Lab, Project, LectureNote, LectureVideo, DemoResource, Publication, Patent, Report, Notice, News, Gallery, Community

from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

from django.core.paginator import Paginator

from django.shortcuts import redirect

# Create your views here.

def index(request):
    # topMenus = TopMenu.objects.all()
    # subMenuDict = dict()
    # for topMenu in topMenus:
    #     subMenus = SubMenu.objects.filter(topmenu_id=topMenu.id)
    #     subMenuDict[topMenu.titleen] = subMenus
    # return render(request, 'web/index.html', {'topMenus' : topMenus, 'subMenuDict' : subMenuDict})

    return render(request, 'web/index.html', {'subMenuDict':getSubMenuDict()})

def getSubMenuDict():
    topMenus = TopMenu.objects.all()
    subMenuDict = dict()
    for topMenu in topMenus:
        subMenus = SubMenu.objects.filter(topmenu_id=topMenu.id)
        subMenuDict[topMenu.titleen] = subMenus
    return subMenuDict

# def menu_detail(request, topMenu):
#     topMenu_id = TopMenu.objects.get(titleen=topMenu)
#     subMenus = get_list_or_404(SubMenu, topmenu_id=topMenu_id.pk)
#     return render(request, 'web/menu_detail.html', {'topMenu': topMenu, 'subMenus': subMenus })

# ListView
class GreetingPage(TemplateView):
    model = Greeting

class MemberImageList(ListView):
    model = Member
    template_name = 'web/member.html'
    context_object_name = 'members'
    paginate_by = 10
    queryset = Member.objects.all()

    def get(self, request):
        return render(request, self.template_name, {'subMenuDict':getSubMenuDict()})

class LabTextList(ListView):
    model = Lab

class ProjectPage(TemplateView):
    model = Project

class LecturenoteImageList(ListView):
    model = LectureNote

class LecturevideoVideoList(ListView):
    model = LectureVideo

class DemoresourceImageList(ListView):
    model = DemoResource

class PublicationTextList(ListView):
    model = Publication

class PatentTextList(ListView):
    model = Patent

class ReportTextList(ListView):
    model = Report

class NoticeTextList(ListView):
    model = Notice

class NewsImageList(ListView):
    model = News
    template_name = 'web/news.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'news_list'
    paginate_by = 5
    queryset = News.objects.order_by('-id') #역순으로 보여주기
    # context={ 'context_object_name':'news_list', 'subMenuDict':getSubMenuDict() }
    def get_context_data(self, **kwargs):
        context = super(NewsImageList, self).get_context_data(**kwargs)
        context['object_name'] = 'news_list'
        context['subMenuDict'] = getSubMenuDict()
        return context



class GalleryImageList(ListView):
    model = Gallery

class CommunityBoard(ListView):
    model = Community

class NewsDetail(DetailView):
    model = News

def githubRedirect(request):
    return redirect('https://www.naver.com/')

def Contact(request):
    topMenus = TopMenu.objects.all()
    subMenuDict = dict()
    for topMenu in topMenus:
        subMenus = SubMenu.objects.filter(topmenu_id=topMenu.id)
        subMenuDict[topMenu.titleen] = subMenus
    return render(request, 'web/contact.html', {'subMenuDict':getSubMenuDict()})
