from django import forms
from django.utils.text import slugify
from django.core.exceptions import ObjectDoesNotExist
from event.models import Category,BookEvent,Event

# class DateInput(forms.DateInput):
#     input_type='date'

class DateTimeInput(forms.DateTimeInput):
    input_type='datetime-local'

class ContactUsForm(forms.Form):
    name=forms.CharField(max_length=100,help_text='your name please')
    email=forms.EmailField(required=False)
    contact=forms.RegexField(regex="^[6-9]\d{9}", required=False)

    def clean(self):
        cleaned_data=super().clean()
        if not (cleaned_data.get('email') or cleaned_data.get('contact')):
            raise forms.ValidationError('Please Enter Email or Phone Number',code="Invalid")


class EventCreateForm(forms.ModelForm):
    start_date=forms.DateTimeField(widget=DateTimeInput())
    end_date=forms.DateTimeField(widget=DateTimeInput())
    class Meta:
        model= Event
        fields=('name','category','image','start_date','end_date','vanue','maximum_participants','description')

    def clean_name(self):
        cleaned_data=super().clean()
        name=cleaned_data.get('name')
        slug=slugify(name)
        try:
            event = Event.objects.get(slug=slug)
            raise forms.ValidationError('Evant Name already Exits',code='Invalid')
        except ObjectDoesNotExist:
            return name
class EventUpdateForm(forms.ModelForm):
    class Meta:
        model= Event
        fields=('name','category','image','start_date','end_date','vanue','maximum_participants','description') 
    