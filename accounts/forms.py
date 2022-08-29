from django import forms
from django.contrib.auth.forms import UserCreationForm


class CustomUserForm(forms.ModelForm):
	email = ...
	username = ...
	password1 = m ...
	password2 = forms.CharField() # widget=forms.PasswordInput()

	class Meta:
		model = CustomUser
		fields = ('email', 'usenrame', 'password1', 'password2')

	def clean(self):
		cd = self.cleaned_data
		cd['password2'] == cd ['password1']		
		return cd['password2']