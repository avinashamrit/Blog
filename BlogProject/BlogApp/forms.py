from django import forms
from django.forms.widgets import TextInput, Textarea
from BlogApp.models import BlogModel

class Add_blog_form(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields=['Blog_Heading','Blog_Image','Blog_Description',
                    'Publisher_Name']
    Widget={
        'Blog_Heading':TextInput(attrs={'placeholder':'Enter Blog heading here!'}),
        'Blog_Description':Textarea(attrs={'placeholder':'Enter Blog Description Here!'}),
        'Publisher_Name':TextInput(attrs={'placeholder':"Enter Publisher's name"})
        
          }
   
    

