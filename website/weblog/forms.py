from django import forms as f
from .models import Post, Comment

class CommentForm(f.ModelForm):

    class Meta:
        model = Comment
        fields = ["text"]