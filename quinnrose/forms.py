from django import forms

from quinnrose.config import CONTACT_SUBJECT_EMAILS
from quinnrose.temp_data import SUBSCRIPTIONS, CREDIT_CARD_TYPES
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
#     print(SUBSCRIPTIONS.get_choices(subtype))
    for choice in SUBSCRIPTIONS.get_choices(subtype):
        choices.append((choice[0],choice[1]))
            
    return (choices)

def get_subscription_billing_frequency_choices():

    choices = [('', 'Select...')]

#     print('SUBSCRIPTION_CHOICES[subtype] = {}'.format(SUBSCRIPTION_CHOICES[subtype]))
    for frequency in SUBSCRIPTIONS.frequencies:
        choices.append((frequency.freq_id, frequency.billing_frequency))
            
    return (choices)

def get_organization_choices(user_id):

    choices = [('', 'Select...')]

#     print('SUBSCRIPTION_CHOICES[subtype] = {}'.format(SUBSCRIPTION_CHOICES[subtype]))
    for org_id in organization_profiles.keys():
        choices.append((org_id,organization_profiles[org_id]['name']))
            
    return (choices)

def get_credit_card_type_choices():
    choices = [('', 'Select...')]
    
    for cc_type in CREDIT_CARD_TYPES:
        choices.append(cc_type)
    
    return choices

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
    have_read_privacy_policy = forms.BooleanField(
        label='I have read the Privacy Policy',
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-control custom-form-checkbox custom-form-checkbox-round',
                'required': 'required',
            }
        )
    )
    accept_terms = forms.BooleanField(
        label='I accept the Terms and Conditions',
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-control custom-form-checkbox custom-form-checkbox-round',
                'required': 'required',
            }
        )
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
#         print('subtype')
#         print(subtype)
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
    billing_frequency = forms.ChoiceField(
        label='Billing Frequency',
        choices=get_subscription_billing_frequency_choices(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
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
    card_type = forms.ChoiceField(
        label='Card Type',
        choices=get_credit_card_type_choices(),
        widget=forms.Select(
            attrs={
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
    