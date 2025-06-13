from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Trail, Note, User

class TrailForm(forms.ModelForm):
    class Meta:
        model = Trail
        fields = ['name', 'start_date', 'end_date', 'location', 'distance', 'elevation', 'image']
        widgets = {
            'start_date' : forms.DateInput(
                format=('%Y-%m-%d'),
                attrs= {
                    'placeholder': "Select a date",
                    'type': 'text',
                    'id' : 'start-date'
                }
            ),
            'end_date' : forms.DateInput(
                format=('%Y-%m-%d'),
                attrs= {
                    'placeholder': "Select a date",
                    'type': 'text',
                    'id' : 'end-date'
                }
            ),
        }
        
    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get('start_date')
        end = cleaned_data.get('end_date')
        
        if start and end and end < start:
            self.add_error('end_date', 'End date cannot be before start date')
        
        
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['note']
        
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    
    # need to 
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # set placeholders
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Username',
            'autofocus': True,
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Password',
        })