from django import forms

class SubscriberForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    work = forms.CharField(required=False)
    github = forms.URLField(required=False)