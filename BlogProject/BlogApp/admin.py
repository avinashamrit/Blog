from django.contrib import admin

from BlogApp.models import BlogModel

# Register your models here.
@admin.register(BlogModel)
class Adminmodel(admin.ModelAdmin):
    list_display = ['Blog_Heading','Blog_Image','Blog_Description',
    'Publisher_Name','Published_On']


