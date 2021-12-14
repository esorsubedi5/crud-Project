from django import forms
from .models import StudentDetail
class StudentDetailForm(forms.ModelForm):
    class Meta:
        model = StudentDetail
        fields = ['id', 'rollno', 'name', 'email']