from django import forms
from .models import Admin, Adminprofile
from kg_news.models import Slider, ChPost, Add_news_ch, Media, WelMsg
from users.models import Users
class LoginForm(forms.ModelForm):
    class Meta:
        model = Admin
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

class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = ('__all__')

class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ('__all__')

class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('__all__')

class Add_News_Form(forms.ModelForm):
    class Meta:
        model = ChPost
        fields = ('__all__')

class Add_Newsch_Form(forms.ModelForm):
    class Meta:
        model = Add_news_ch
        fields = ('__all__')

class WelMsgForm(forms.ModelForm):
    class Meta:
        model = WelMsg
        fields = ('__all__')

class AdminprofileForm(forms.ModelForm):
    class Meta:
        model = Adminprofile
        fields = ('__all__')