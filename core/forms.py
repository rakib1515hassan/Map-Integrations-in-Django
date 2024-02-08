from django import forms
from core.models import School

class SchoolForm(forms.ModelForm):
    selected_location = forms.CharField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = School
        fields = ('school_name', 'latitude', 'longitude', 'selected_location',)

        widgets = {
            'school_name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Given School Name'
            }),

            'latitude': forms.NumberInput(attrs={
                'class': 'form-control', 
                'type': 'hidden'
            }),
            
            'longitude': forms.NumberInput(attrs={
                'class': 'form-control', 
                'type': 'hidden'
            }),
        }