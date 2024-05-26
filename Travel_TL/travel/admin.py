from django.contrib import admin
from django.utils.safestring import mark_safe

from travel.models import News, Tour, Place, Transport,Image, Album
from django.db.models import Count
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.urls import path
from django.template.response import TemplateResponse


class MyAdminSite(admin.AdminSite):
    site_header = 'TL_Travel;'

    def get_urls(self):
        return [path('cate-stats/', self.stats_view)] + super().get_urls()

    def stats_view(self, request):
        stats = Tour.objects.annotate(counter=Count('id')).values('id', 'name', 'counter')
        return TemplateResponse(request, 'admin/stats.html', {
            'stats': stats
        })


admin_site = MyAdminSite(name='TL_Travel')


class TourForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Tour
        fields = '__all__'


class ImageAdmin(admin.ModelAdmin):
    list_display = ['my_image','Name']
    search_fields = ['Name']
    list_filter = ['created_date']

    def my_image(self, image):
        if (image):
            return mark_safe(f"<img src='https://res.cloudinary.com/dqcjhhtlm/image/upload/{image.Path}' width='200' />")

    class Media:
        css = {
            'all': ('/static/css/style.css',)
        }




# Register your models here.
admin.site.register(News)
admin.site.register(Tour)
admin.site.register(Place)
admin.site.register(Transport)
admin.site.register(Image, ImageAdmin)
admin.site.register(Album)
# admin.site.register(C)
