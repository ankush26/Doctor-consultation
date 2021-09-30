from django import forms
from .models import Patient
class PatientRegistration(forms.ModelForm):
    class Meta:
        model=Patient
        fields = ['email', 'userid','password']