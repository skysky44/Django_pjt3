from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ('title', 'content', 'movie', 'image')

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        widget = forms.TextInput(
            attrs={
                'class': 'form-control input-group',
                'placeholder' : ' 댓글을 입력해주세요'
            }
        
        )
    )

    class Meta:
        model = Comment
        fields = ('content',)
