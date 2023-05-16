from django import forms
from .models import Student
# creating a form

class InputForm(forms.Form):
    ﬁrst_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)
    roll_number = forms.IntegerField(help_text = "Enter 6 digit roll number")
    password = forms.CharField(widget = forms.PasswordInput())
