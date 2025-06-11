from django import forms
from .models import Trail, Note

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
        
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['note']