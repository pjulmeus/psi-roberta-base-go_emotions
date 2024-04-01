from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label="Place your input here:", max_length=100)