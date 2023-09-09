from django.db import models

# Create your models here.
class BlogModel(models.Model):
    Blog_Heading = models.CharField(max_length=50)
    Blog_Image = models.ImageField(upload_to = 'images')
    Blog_Description = models.TextField(max_length=1000)
    Publisher_Name = models.CharField(max_length=20)
    Published_On = models.DateTimeField(auto_now_add=True)