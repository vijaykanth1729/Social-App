from django import forms
from .models import Post, Comment
class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    class Meta:
        model = Post
        fields = ('content', 'image')

class CommentModelForm(forms.ModelForm):
    #content = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    body = forms.CharField(label='', widget=forms.TextInput({'placeholder' : 'Add a comment here..'}))
    class Meta:
        model = Comment
        fields = ('body',)
