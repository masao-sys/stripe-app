from django.contrib.auth.forms import UserCreationForm
from myapp.models.custom_user import CustomUser

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
        )
