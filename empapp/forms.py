from django import forms
from empapp.models import empdet
class EmployeeForm(forms.ModelForm):
    class Meta:
        model =  empdet
        fields = "__all__"