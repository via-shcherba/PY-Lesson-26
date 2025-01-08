from django.contrib.auth.forms import UserCreationForm
from .models import StandardUser

class RegistrationForm(UserCreationForm):
    class Meta:
        model = StandardUser
        fields = ('username', 'password1', 'password2', 'email')