from app1 model import *
from django import forms
class studentform(forms.ModelForm):
    class Meta :
        model=student
        fields=' __all__'