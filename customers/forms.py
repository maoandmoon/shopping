from django import forms
# from customers.models import UserProfileInfo, UserProfile
from customers.models import User, CustomerProfile
# from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')
        # fields = ('username', 'first_name', 'last_name', 'middle_name', 'phone', 'email', 'password')


class CustomerProfileForm(forms.ModelForm):

    class Meta():
        model = CustomerProfile
        fields = ('middle_name', 'phone', 'birth_date', 'destination_address', 'profile_picture', 'orders')


