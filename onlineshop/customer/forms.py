from phonenumber_field.formfields import PhoneNumberField
from django import forms
from customer.models import Customer, Passport



class EditProfileForm(forms.ModelForm):
    phone = PhoneNumberField(required=False)
    address = forms.Textarea()


    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'patronymic', 'gender', 'date_birthday', 'email', 'phone', 'address', 'username']

class EditProfileFormPassport(forms.ModelForm):

    class Meta:
        model = Passport
        fields = ['series_passport', 'number_passport', 'passport_issue', 'date_issue']

