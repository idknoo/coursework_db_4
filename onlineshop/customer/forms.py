from phonenumber_field.formfields import PhoneNumberField
from django import forms
from customer.models import Customer


class EditProfileForm(forms.ModelForm):
    phone = PhoneNumberField(required=False)
    address = forms.Textarea()

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'username', ]
