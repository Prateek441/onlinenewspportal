from django import forms
from kg_news.models import Add_news_ch, ChPost, ChannelDetails
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

class Add_News_Form(forms.ModelForm):
    class Meta:
        model = ChPost
        fields = ('title','sub_title','img','Description','related_img','category','state', 'city','status')

    # ch_post = forms.CharField(label="",
    #                         widget=forms.TextInput(
    #                             attrs={
    #
    #                                 'class': 'form-control,col-md-3  ',
    #                                 'value': 'AAJ TAK',
    #
    #                             }
    #                         )
    #                         )

    title = forms.CharField(label="",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter News Title Here..',
                'class': 'form-control,col-md-3  ',

            }
        )
    )


    sub_title = forms.CharField(label="",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter sub title Here..',
                'class': 'form-control, col-md-4',


            }
        )
    )


    Description = forms.CharField(label="",
                                 widget=forms.Textarea(
                                     attrs={
                                         'placeholder': 'Enter Description Here..',
                                         'class': 'form-control, col-md-11',
                                         'rows':4
                                     }
                                 )
                                 )


