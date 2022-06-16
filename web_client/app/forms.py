from django import forms


class InputPhoneForm(forms.Form):
    phone_to = forms.CharField(max_length=50)


class InputPhones(forms.Form):
    phone_from = forms.CharField(max_length=50)
    phone_to = forms.CharField(max_length=50)
