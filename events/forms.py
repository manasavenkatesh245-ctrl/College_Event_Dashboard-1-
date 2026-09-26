from django import forms
from .models import Registration


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = Registration
        fields = [
            'student_name',
            'student_email',
            'student_phone'
        ]