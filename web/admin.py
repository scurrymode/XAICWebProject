from django.contrib import admin
from web.models import TopMenu, Greeting, About, Member, LectureNote, LectureVideo, DemoResource, Patent, Publication, News, Notice, Gallery, Community

# Register your models here.

admin.site.register(TopMenu)
admin.site.register(Greeting)
admin.site.register(About)
admin.site.register(Member)
admin.site.register(LectureVideo)
admin.site.register(LectureNote)
admin.site.register(DemoResource)
admin.site.register(Publication)
admin.site.register(Patent)
admin.site.register(Notice)
admin.site.register(News)
admin.site.register(Gallery)
admin.site.register(Community)