from django import forms

from quinnrose.config import CONTACT_SUBJECT_EMAILS

def get_choices():

    subject_choices = [('', 'Select...')]

    for i in range(len(CONTACT_SUBJECT_EMAILS)):
        subject_choices.append((i,CONTACT_SUBJECT_EMAILS[i][0]))
            
    return (subject_choices)
    
class ContactForm(forms.Form):

    email = forms.EmailField(
        label='Email',
        help_text="An email address is required",
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'user@example.com',
                'class': 'form-control',
                'required': 'required',
#                 'data-error': "Don't forget to enter your email address!"
            }
        ),
        required=True
    )
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'John Doe',
                'class': 'form-control',
            }
        ),
        required=False
    )
    subject = forms.ChoiceField(
        label='Subject',
        choices=get_choices(),
        widget=forms.Select(
            attrs={
                'class': 'form-control select-placeholder',
                'required': 'required',
            }
        ),
        required=True
    )
    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Type your message...',
                'class': 'form-control',
                'rows': 4,
                'required': 'required',
            }
        ),
        required=True
    )


if __name__ == "__main__":
    f = ContactForm()
    