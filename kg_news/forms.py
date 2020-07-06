from django import forms
from .models import Add_news_ch
from .models import ChPost
from .models import State
class AddNewsChForm(forms.ModelForm):
    class Meta:
        model = Add_news_ch
        fields =('__all__')

class AddNewsForm(forms.ModelForm):
    class Meta:
        model = ChPost
        fields =('__all__')

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter News Title',
                'class': 'form-control '
            }
        )
    )

    sub_title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter News Title',
                'class': 'form-control '
            }
        )
    )

    Description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Enter News Title',
                'class': 'form-control ',
                'rows':3,

            }
        )
    )

    # img = forms.FileField(
    #     widget=forms.ClearableFileInput(
    #         attrs={
    #             'class': 'form-control ',
    #
    #         }
    #     )
    # )

class AddStateForm(forms.ModelForm):
    class Meta:
        model = State
        fields =('__all__')


class LoginForm(forms.ModelForm):
    class Meta:
        model = Add_news_ch
        fields = ('email', 'password')

    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Enter Email Address',
                'class': 'form-control  '
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter Password',
                'class': 'form-control  '
            }
        )
    )

class FilterForm(forms.ModelForm):
    class Meta:
        model = ChPost
        fields = ('state', 'category')


