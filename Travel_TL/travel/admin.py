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
        stats =Album.objects.annotate(counter=Count('image_id')).values('id','Name','counter')
        return TemplateResponse(request, 'admin/stats.html', {
            'stats': stats
        })


admin_site = MyAdminSite(name='TL_Travel')




class TourForm(forms.ModelForm):
    Description = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Tour
        fields = '__all__'



class TourAdmin(admin.ModelAdmin):
    list_display = ['Tour_Name']
    search_fields = ['Tour_Name']
    form= TourForm

    def my_image(self, tour):
        if tour.image:
            return mark_safe(f"<img src='/static/ckeditor/{tour.image.Path}' width='200' />")



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
            return mark_safe(f"<img src='/static/ckeditor/{images.Path}' width='200' />")

class ImageAdmin(admin.ModelAdmin):

    list_display = ['Name','my_image']
    readonly_fields = ['my_image']
    def my_image(self, imageForTour):
        if (imageForTour):
            print(imageForTour.Path)
            return mark_safe(f"<img src='/static/{imageForTour.Path}' width='200' />")






# Register your models here.
admin_site.register(News, NewsAdmin)
admin_site.register(Tour,TourAdmin)
admin_site.register(BookTour)
admin_site.register(CMT_News)
admin_site.register(CMT_Tour)
admin_site.register(Image, ImageAdmin)
admin_site.register(Album)
admin_site.register(User, UserAdmin)


# admin.site.register(C)
