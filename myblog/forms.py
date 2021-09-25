from django import forms
from .models import PostContactModel, PostModel 

class PostContactForm(forms.ModelForm):
    class Meta:
        model = PostContactModel
        fields = "__all__"


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        exclude = ['post_date', 'user_id']
