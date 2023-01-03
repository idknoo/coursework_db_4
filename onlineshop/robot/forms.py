from django import forms
from robot.models import Robot


class ItemChangeListForm(forms.ModelForm):

    # here we only need to define the field we want to be editable
    animal = forms.ModelMultipleChoiceField(queryset=Robot.objects.all(),
                                            required=False)