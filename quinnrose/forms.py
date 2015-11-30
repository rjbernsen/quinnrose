from django import forms

from quinnrose.config import CONTACT_SUBJECT_EMAILS

def get_choices():

    subject_choices = [('', 'Select...')]

    for i in range(len(CONTACT_SUBJECT_EMAILS)):
        subject_choices.append((i,CONTACT_SUBJECT_EMAILS[i][0]))
            
    return (subject_choices)

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
#     subject = forms.ChoiceField(
#         label='Subject',
#         choices=get_choices(),
#         widget=forms.Select(
#             attrs={
#                 'class': 'form-control select-placeholder',
#                 'required': 'required',
#             }
#         ),
#         required=True
#     )
#     message = forms.CharField(
#         label='Message',
#         widget=forms.Textarea(
#             attrs={
#                 'placeholder': 'Type your message...',
#                 'class': 'form-control',
#                 'rows': 4,
#                 'required': 'required',
#             }
#         ),
#         required=True
#     )

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
    