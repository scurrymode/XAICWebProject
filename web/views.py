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
    template_name = 'web/greetingTemp.html'

    def get_context_data(self, **kwargs):
        context = super(GreetingPage, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

class MemberImageList(ListView):
    model = Member
    template_name = 'web/memberTemp.html'  # Default: <app_label>/<model_name>_list.html
    # context_object_name = 'member_list'
    paginate_by = 5
    queryset = Member.objects.order_by('-id')  # 역순으로 보여주기

    # context={ 'context_object_name':'news_list', 'subMenuDict':getSubMenuDict() }
    def get_context_data(self, **kwargs):
        context = super(MemberImageList, self).get_context_data(**kwargs)
        context['object_name'] = 'member_list'
        context['subMenuDict'] = getSubMenuDict()
        return context

class LabTextList(ListView):
    model = Lab
    template_name = 'web/lab_detailTemp.html'

    def get_context_data(self, **kwargs):
        context = super(LabTextList, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context


class ProjectPage(TemplateView):
    model = Project
    template_name = 'web/preparing.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectPage, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

class LecturenoteImageList(ListView):
    model = LectureNote
    template_name = 'web/preparing.html'

    def get_context_data(self, **kwargs):
        context = super(LecturenoteImageList, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

class LecturevideoVideoList(ListView):
    model = LectureVideo
    template_name = 'web/preparing.html'

    def get_context_data(self, **kwargs):
        context = super(LecturevideoVideoList, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context


class DemoresourceImageList(ListView):
    model = DemoResource
    template_name = 'web/preparing.html'

    def get_context_data(self, **kwargs):
        context = super(DemoresourceImageList, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

class PublicationTextList(ListView):
    model = Publication
    template_name = 'web/preparing.html'

    def get_context_data(self, **kwargs):
        context = super(PublicationTextList, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

class PatentTextList(ListView):
    model = Patent
    template_name = 'web/preparing.html'

    def get_context_data(self, **kwargs):
        context = super(PatentTextList, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

class ReportTextList(ListView):
    model = Report
    template_name = 'web/preparing.html'

    def get_context_data(self, **kwargs):
        context = super(ReportTextList, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

class NoticeTextList(ListView):
    model = Notice
    template_name = 'web/preparing.html'

    def get_context_data(self, **kwargs):
        context = super(NoticeTextList, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

class NewsImageList(ListView):
    model = News
    template_name = 'web/news.html'  # Default: <app_label>/<model_name>_list.html
    # context_object_name = 'news_list'
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
    template_name = 'web/gallery.html'

    def get_context_data(self, **kwargs):
        context = super(GalleryImageList, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

class CommunityBoard(ListView):
    model = Community
    template_name = 'web/preparing.html'

    def get_context_data(self, **kwargs):
        context = super(CommunityBoard, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

class NewsDetail(DetailView):
    model = News
    template_name = 'web/preparing.html'

    def get_context_data(self, **kwargs):
        context = super(NewsDetail, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

def githubRedirect(request):
    return redirect('http://sail.unist.ac.kr')

def Contact(request):
    topMenus = TopMenu.objects.all()
    subMenuDict = dict()
    for topMenu in topMenus:
        subMenus = SubMenu.objects.filter(topmenu_id=topMenu.id)
        subMenuDict[topMenu.titleen] = subMenus
    return render(request, 'web/contact.html', {'subMenuDict':getSubMenuDict()})
