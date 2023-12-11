from django import forms

class Contact(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    category=forms.ChoiceField(choices=[('Question','question'),('Other','other')])
    subject=forms.CharField()
    