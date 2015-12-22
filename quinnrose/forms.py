from django import forms

from quinnrose.config import CONTACT_SUBJECT_EMAILS
from quinnrose.temp_data import SUBSCRIPTION_CHOICES
from artist.temp_data import artist_profiles
from organization.temp_data import organization_profiles
from quinnrose.fields import CreditCardField, ExpiryDateField, VerificationValueField

mock_user = artist_profiles['1']

def get_subject_choices():

    choices = [('', 'Select...')]

    for i in range(len(CONTACT_SUBJECT_EMAILS)):
        choices.append((i,CONTACT_SUBJECT_EMAILS[i][0]))
            
    return (choices)

def get_subscription_choices(subtype):

    choices = [('', 'Select...')]

#     print('SUBSCRIPTION_CHOICES[subtype] = {}'.format(SUBSCRIPTION_CHOICES[subtype]))
    for i in range(len(SUBSCRIPTION_CHOICES[subtype])):
        choices.append((i,SUBSCRIPTION_CHOICES[subtype][i]))
            
    return (choices)

def get_organization_choices(user_id):

    choices = [('', 'Select...')]

#     print('SUBSCRIPTION_CHOICES[subtype] = {}'.format(SUBSCRIPTION_CHOICES[subtype]))
    for org_id in organization_profiles.keys():
        choices.append((org_id,organization_profiles[org_id]['name']))
            
    return (choices)

class SignInForm(forms.Form):

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
    )
    password = forms.CharField(
        label='Password',
        help_text="Use something really secure!",
        min_length=6,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-control',
                'required': 'required',
                'data-minlength': 6,
                'data-toggle':'validator',
#                 'data-error': "Don't forget to enter your email address!"
            }
        ),
        required=True
    )
    password_confirm = forms.CharField(
        label='Confirm Password',
        help_text="Both entries must be the same",
        min_length=6,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirm',
                'class': 'form-control',
                'required': 'required',
                'data-minlength': 6,
                'data-match': '#id_password',
                'data-match-error':"Whoops, these don't match",
#                 'data-error': "Don't forget to enter your email address!"
            }
        ),
        required=True
    )
    first_name = forms.CharField(
        label='First name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'John',
                'class': 'form-control',
                'required': 'required',
            }
        ),
        required=True
    )
    last_name = forms.CharField(
        label='Last name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Doe',
                'class': 'form-control',
                'required': 'required',
            }
        ),
        required=True
    )

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
        choices=get_subject_choices(),
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

class SubscribeForm(forms.Form):

    def __init__(self, subtype=None, *args, **kwargs):

#         self.subtype = kwargs.pop('subtype', None)
        super().__init__(*args, **kwargs)
        print('subtype')
        print(subtype)
        self.fields['level'].choices = get_subscription_choices(subtype)
        self.fields['organization'].choices = get_organization_choices('dummy')
        
    organization = forms.ChoiceField(
        label='Organization',
        choices=(),
        widget=forms.Select(
            attrs={
                'class': 'form-control select-placeholder',
                'required': 'required',
            }
        ),
        required=True
    )
    level = forms.ChoiceField(
        label='Level',
        choices=(),
        widget=forms.Select(
            attrs={
                'class': 'form-control select-placeholder',
                'required': 'required',
            }
        ),
        required=True
    )
    email = forms.EmailField(
        label='Email',
        initial=mock_user['email'],
        help_text="An email address is required",
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'user@something.com',
                'class': 'form-control',
                'required': 'required',
            }
        ),
        required=True
    )
    name_on_card = forms.CharField(
        label='Name on Card',
        initial=mock_user['first_name'] + ' ' + mock_user['last_name'],
        widget=forms.TextInput(
            attrs={
                'placeholder': 'John Smith',
                'class': 'form-control',
                'required': 'required',
            }
        ),
        required=True
    )
    card_number = CreditCardField(
        label='Credit Card Number',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'XXXXXXXXXXXXXXXX',
                'class': 'form-control',
                'required': 'required',
            }
        ),
        required=True
    )
    expiration_date = ExpiryDateField(
        label='Expiration',
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'XXXXXXXXXXXXXXXX',
#                 'class': 'form-control',
#                 'required': 'required',
#             }
#         ),
        required=True
    )
    card_code = VerificationValueField(
        label='Verification Code',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'XXX',
                'class': 'form-control',
                'required': 'required',
            }
        ),
        required=True
    )

if __name__ == "__main__":
    f = ContactForm()
    