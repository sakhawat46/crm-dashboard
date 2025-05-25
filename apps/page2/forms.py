from django import forms
from .models import AboutUs,ContactMessage,ContactUs
class AboutUsForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = '__all__'
        widgets = {
            'title_white': forms.TextInput(attrs={'class': 'form-control'}),
            'title_red': forms.TextInput(attrs={'class': 'form-control'}),
            'heading': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'what_do': forms.TextInput(attrs={'class': 'form-control'}),
            'Why_Choose_Softvence': forms.TextInput(attrs={'class': 'form-control'}),
            'our_misson': forms.TextInput(attrs={'class': 'form-control'}),
            'count_01_title': forms.TextInput(attrs={'class': 'form-control'}),
            'count_01': forms.NumberInput(attrs={'class': 'form-control'}),
            'count_02_title': forms.TextInput(attrs={'class': 'form-control'}),
            'count_02': forms.NumberInput(attrs={'class': 'form-control'}),
            'button_text': forms.TextInput(attrs={'class': 'form-control'}),
            'button_url': forms.URLInput(attrs={'class': 'form-control'}),
            # Repeat as needed for other fields
        }


from django import forms
from .models import Service

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'description', 'icon']







class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']



class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['Title', 'call_us', 'mail', 'address', 'map']
        widgets = {
            'Title': forms.TextInput(attrs={'class': 'form-control'}),
            'call_us': forms.NumberInput(attrs={'class': 'form-control'}),
            'mail': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'map': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
