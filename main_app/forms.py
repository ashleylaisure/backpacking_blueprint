from django import forms
from .models import Trail, Gear, MealPlan

class TrailForm(forms.ModelForm):
    class Meta:
        model = Trail
        fields = ['name', 'start_date', 'end_date', 'location', 'distance', 'elevation', 'image']
        widgets = {
            'start_date' : forms.DateInput(
                format=('%Y-%m-%d'),
                attrs= {
                    'placeholder': "Select a date",
                    'type': 'date'
                    # customize further with Flatpickr or jQuery UI Datepicker?
                }
            ),
            'end_date' : forms.DateInput(
                format=('%Y-%m-%d'),
                attrs= {
                    'placeholder': "Select a date",
                    'type': 'date'
                }
            ),
        }

class MealPlanForm(forms.ModelForm):
    class Meta:
        model = MealPlan
        fields = ['meal', 'category']
        widgets = {
            'category': forms.Select(attrs={'class': 'border px-2 py-1 rounded'}),
            'food': forms.Select(attrs={'class': 'border px-2 py-1 rounded'}),
        }

class PackedForm(forms.ModelForm):
    class Meta:
        model = Gear
        fields = ['packed']
        labels = {
            'packed' : '',
        }