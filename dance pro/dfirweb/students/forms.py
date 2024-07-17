# students/forms.py
from django import forms
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'gender', 'age', 'style', 'date', 'state', 'email']
