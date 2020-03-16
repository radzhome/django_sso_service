from django import forms


class LoginForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['password'].widget = forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'autocomplete': "on",
            }
        )

    email = forms.EmailField(label=u'User email', required=True)
    password = forms.CharField(
        label=u'Password',
        required=True,
        widget=forms.PasswordInput()
    )
