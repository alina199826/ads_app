from django import forms
from django.forms import widgets
from webapp.models import Ads, Comment


class AdForm(forms.ModelForm):
    class Meta:
        model = Ads
        fields = ['photo', 'text', 'description', 'category', 'price']
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
        error_messages = {
            'text': {
                'required': 'Поле должно быть заполнено'
            }
        }




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']




class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False, label='Найти',
                             widget=widgets.TextInput(attrs={'class': "form-control w-25"}))