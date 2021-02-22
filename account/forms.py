from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model

class SignUpForm(UserCreationForm):
    email=forms.EmailField()
    confirm_email=forms.EmailField()
    contact=forms.RegexField(regex="^[6-9]\d{9}", required=False)
    bio=forms.CharField()
    class Meta:
        model = get_user_model()
        fields=('first_name','last_name','username','email','confirm_email','contact','category','password1','password2','profile','bio')

    def clean(self):
        cleaned_data=super().clean()
        if cleaned_data.get('email') != cleaned_data.get('confirm_email'):
            raise forms.ValidationError('Your Email and Confirm Email is not match',code='Invalid')
class UserUpdateForm(forms.ModelForm):
    bio=forms.CharField()
    class Meta:
        model = get_user_model()
        fields=('first_name','last_name','username','email','contact','profile','bio')

