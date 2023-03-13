from django import forms


class RelativeForm(forms.Form):
    relative_name = forms.CharField(max_length=100)
    relative_email = forms.EmailField()
    relative_phone_number = forms.CharField(max_length=20, required=False)
