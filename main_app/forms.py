from django import forms
from .models import Trail, Gear, Todo

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


# class PackedForm(forms.ModelForm):
#     class Meta:
#         model = Gear
#         fields = ['name', 'packed']
#         labels = {
#             'name' : '',
#             'packed' : '',
#         }

# class TodoForm(forms.ModelForm):
#     class Meta:
#         model = Todo
#         fields = ['todo']