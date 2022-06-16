from django import forms


class InputPhoneForm(forms.Form):
    phone = forms.CharField(max_length=50)
