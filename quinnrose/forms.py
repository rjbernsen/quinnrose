from django import forms

class ContactForm(forms.Form):

    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Message', widget=forms.Textarea)