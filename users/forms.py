from django import forms #in the form we can add any types of field and widget
from  .models import Users
from .models import Userprofile
class SignpForm(forms.ModelForm):
    class Meta:
        model = Users
        fields =('username','email','password','mobile')

    password =forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter password',
                'class':'form-control'
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Enter Email Address',
                'class': 'form-control'
            }
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter Your Name',
                'class': 'form-control'
            }
        )
    )
    mobile = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Enter Contact',
                'class': 'form-control'
            }
        )
    )

class LoginForm(forms.Form):
    email =forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'placeholder' : 'Enter Email',
                'class' : 'form-control'
            }
        )
    )

    password =forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter password',
                'class': 'form-control'
            }
        )
    )


class UprofileForm(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields =('image','about','gender','dob','address','cover')

    about = forms.CharField(
        widget=forms.TextInput(
            attrs={

                'class': 'form-control'
            }
        )
    )
    gender = forms.CharField(
        widget=forms.TextInput(
            attrs={

                'class': 'form-control',

            }
        )
    )
    address = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows':3,
                'class': 'form-control',

            }
        )
    )




