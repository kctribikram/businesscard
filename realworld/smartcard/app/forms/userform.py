from django import forms
from app.models import UserLogin

class UserForm(forms.ModelForm):
	class Meta:
		model=UserLogin
		fields="__all__"