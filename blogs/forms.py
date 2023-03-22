from django import forms
from django.forms import ModelForm
from .models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','author','body']

        widgets = {
            'title':forms.TextInput(attrs={'placeholder':'Enter your title here'}),
            'author':forms.TextInput(attrs={'value':'','id':'logged-user','type':'hidden'}),
            'body':forms.Textarea(attrs={'placeholder':'Enter your content here'}),
        }

class CommentForm(ModelForm):
    class Meta:
        # room is the model that we wanna create form for
        model = Comment
        # this will create form based on room inside models.py
        fields = '__all__'   
        exclude = ['name','post']     