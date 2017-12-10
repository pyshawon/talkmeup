from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

<<<<<<< HEAD
from userprofile.models import ContactedUserProfile
=======
>>>>>>> f0cfdcab2a9d074b95c0dd39f7859486b0e90596

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Input a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
        
<<<<<<< HEAD

class ContactedUserForm(forms.ModelForm):
    class Meta:
        model = ContactedUserProfile
        fields = ('contactName', 'contactEmail', 'contactPhone', 'contactMessage', )
=======
>>>>>>> f0cfdcab2a9d074b95c0dd39f7859486b0e90596
