from django import forms
from accounts_app.models import User


class UserForm(forms.ModelForm):
    """
    Form to register the user
    """
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'username',
            'password',
            'confirm_password'
        )

    def clean(self):
        cleaned_data = super().clean()
        error_dict = {}
        password = cleaned_data.get('password', '')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            error_dict['password'] = \
                "password and confim password should be exactly same"
            
        if len(error_dict) > 0:
            raise forms.ValidationError(message = error_dict)
        
        return cleaned_data