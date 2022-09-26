from django.forms import ModelForm
from .models import Patient,Doctor


class PatientForm(ModelForm):
    class Meta:
        model=Patient
        fields='__all__'

class DoctorForm(ModelForm):
    class Meta:
        model=Doctor
        fields='__all__'