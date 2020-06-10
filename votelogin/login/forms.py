from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.db import transaction


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
             'matric_no',
            'email',
            'first_name',
            'last_name',
            'Department',
            'faculty',
            'password1',
            'password2',

        ]
