from phonenumber_field.formfields import PhoneNumberField
from django import forms
from customer.models import Customer, Passport, User



class EditProfileForm(forms.ModelForm):
    phone = PhoneNumberField(required=False)
    address = forms.Textarea()

    class Meta:
        model = User
        # fields = ['first_name', 'last_name', 'patronymic', 'gender', 'date_birthday', 'email', 'phone', 'address']
        fields = ['first_name', 'last_name', 'email', 'phone', 'username']

# class EditProfileFormPassport(forms.ModelForm):
#
#     class Meta:
#         model = Passport
        # fields = ['series_passport', 'number_passport', 'passport_issue', 'date_issue']
        # fields = ['series_passport', 'number_passport', 'passport_issue', 'date_issue']

# class EditProfileUserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username']
