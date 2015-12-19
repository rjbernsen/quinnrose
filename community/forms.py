from django import forms

from .temp_data import CATEGORIES

def get_category_choices():

    category_choices = [('', 'Select...')]

    for category in CATEGORIES:
        category_choices.append((category[0],category[1]))
            
    return (category_choices)

class BlogEntryForm(forms.Form):

    email = forms.EmailField(
        label='Email',
        help_text="An email address is required",
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'user@example.com',
                'class': 'form-control',
                'required': 'required',
            }
        ),
        required=True
    )
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'John',
                'class': 'form-control',
            }
        ),
        required=False
    )
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'New entry title...',
                'class': 'form-control',
                'required': 'required',
            }
        ),
        required=True
    )
    lead_text = forms.CharField(
        label='Lead Text',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Text...',
                'class': 'form-control',
                'rows': 3,
#                 'required': 'required',
            }
        ),
        required=False
    )
    article_text = forms.CharField(
        label='Article Text',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Text...',
                'class': 'form-control',
                'rows': 5,
                'required': 'required',
            }
        ),
        required=True
    )
    subject = forms.ChoiceField(
        label='Category',
        choices=get_category_choices(),
        widget=forms.Select(
            attrs={
                'class': 'form-control select-placeholder',
                'required': 'required',
            }
        ),
        required=False
    )
    name = forms.CharField(
        label='Tags',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Tag1, Tag2...',
                'class': 'form-control',
            }
        ),
        required=False
    )


if __name__ == "__main__":
    f = BlogEntryForm()
    