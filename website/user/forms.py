from django import forms as f
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
User = get_user_model()


class RegisterForm(UserCreationForm):


    first_name = f.CharField(
        required = True,
        min_length = 2,
        max_length = 32,
        widget = f.TextInput(
            {
                "class": "input",
                "id": "first-name-input",
            }
        ),
        label = "First Name"
    )

    last_name = f.CharField(
        required = True,
        min_length = 2,
        max_length = 32,
        widget = f.TextInput(
            {
                "class": "input",
                "id": "last-name-input"
            }
        ),
        label = "Last Name"
    )

    phone_number = f.CharField(
        required = True,
        min_length = 11,
        max_length = 11,
        widget = f.TextInput(
            {
                "class": "input",
                "id": "phone-number-input"
            }
        ),
        label = "Phone Number"
    )

    national_code = f.CharField(
        required = True,
        min_length = 10,
        max_length = 10,
        widget = f.TextInput(
            {
                "class": "input",
                "id": "national-code-input"
            }
        ),
        label = "National Code"
    
    )

    born_date = f.DateField(
        required = True,
        widget = f.DateInput(
            {
                "class": "input",
                "id": "born-date-input"
            }
        ),
        label = "Born Date"
    )

    email = f.EmailField(
        required = True,
        min_length = 8,
        max_length = 64,
        widget = f.EmailInput(
            {
                "class": "input",
                "id": "email-address-input"
            }
        ),
        label = "Email Address"
    )

    username = f.CharField(
        required = True,
        min_length = 2,
        max_length = 16,
        widget = f.TextInput(
            {
                "class": "input",
                "id": "username-input"
            }
        ),
        label = "Username"
    
    )

    password1 = f.CharField(
        required = True,
        min_length = 8,
        max_length = 64,
        widget = f.PasswordInput(
            {
                "class": "input",
                "id": "password-input"
            }
        ),
        label = "Password"
    )

    password2 = f.CharField(
        required = True,
        min_length = 8,
        max_length = 64,
        widget = f.PasswordInput(
            {
                "class": "input",
                "id": "password-confirm-input"
            }
        ),
        label = "Confirm password"
    )

    


    class Meta:
        model = User
        fields = ["username"]

        widgets = {
            "username": f.TextInput(
                {
                    "class": "input"
                }
            )
        }


class LoginForm(AuthenticationForm):
    username = f.CharField(widget=f.TextInput(attrs={
        "class": "input"
    }))
    password = f.CharField(widget=f.PasswordInput(attrs={
        "class": "input"
    }))
