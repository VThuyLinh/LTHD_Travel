from django.contrib import admin
from django.db.models import Count
from django.utils.safestring import mark_safe

from travel.models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.urls import path
from django.template.response import TemplateResponse


class UserAdmin(admin.ModelAdmin):
    list_display=['username','last_name','vaitro']


class MyAdminSite(admin.AdminSite):
    site_header = 'TL_Travel;'

    def get_urls(self):
        return [path('stats_amountimageintour/', self.stats_view)] + super().get_urls()

    def stats_view(self, request):
        stats =Album.objects.annotate(counter=Count('image__id')).values('id','Name','counter')
        return TemplateResponse(request, 'admin/stats.html', {
            'stats': stats
        })


admin_site = MyAdminSite(name='TL_Travel')




class TourForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)
    popup_response_template = True
    class Meta:
        model = Tour
        fields = '__all__'



class TourAdmin(admin.ModelAdmin):
    list_display = ['Id_Tour','album','album1']
    search_fields = ['Tour_Name']
    list_filter = ['Ngày cập nhật']
    # readonly_fields = ['my_image']
    form = TourForm
    #
    # # def my_image(self,tour ):
    # #     if tour.album:
    # #         return mark_safe(f"<img width='200' src='{tour.image.url}' />")
    # def album1(self, request):
    #     # for a in request.image_set.all():
    #     #     {
    #     #
    #     #     }
    #     print(request.image_set.all())



class NewsForm(forms.ModelForm):
    Content= forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = News
        fields = '__all__'




class NewsAdmin(admin.ModelAdmin):
    list_display = [ 'Name_News']
    search_fields = ['Name_News']
    # list_filter = ['DatePost']
    readonly_fields = ['my_image']
    form = NewsForm

    def my_image(self, news):
        if news.image:
            return mark_safe(f"<img src='https://res.cloudinary.com/dqcjhhtlm/image/upload/{news.image.name}' width='200' />")

class ImageAdmin(admin.ModelAdmin):

    list_display = ['Name','my_image']
    readonly_fields = ['my_image']
    def my_image(self, image):
        if (image):
            print(image.Path)
            return mark_safe(f"<img src='https://res.cloudinary.com/dqcjhhtlm/image/upload/{image.Path}' width='200' />")






# Register your models here.
admin_site.register(News, NewsAdmin)
admin_site.register(Tour, TourAdmin)
admin_site.register(BookTour)
admin_site.register(CMT_News)
admin_site.register(Image, ImageAdmin)
admin_site.register(Album)

admin_site.register(User, UserAdmin)

# admin.site.register(C)
