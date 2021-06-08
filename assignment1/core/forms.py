from django import forms

class ProfileForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    work = forms.CharField(required=False)
    github = forms.URLField(required=False)

class SubscriberForm(forms.Form):
    email = forms.EmailField()
