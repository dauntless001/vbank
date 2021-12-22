from allauth.account import forms
from django import forms as d_forms


def add_form_control(form):
    for field_name, field in form.fields.items():
        if field_name != 'remember':
            field.widget.attrs['class'] = 'form-control'


class _LoginForm(forms.LoginForm):
    def __init__(self, *args, **kwargs):
        super(_LoginForm, self).__init__(*args, **kwargs)
        add_form_control(self)


class _SignupForm(forms.SignupForm):
    first_name = d_forms.CharField(max_length=50)
    last_name = d_forms.CharField(max_length=50)
    def __init__(self, *args, **kwargs):
        super(_SignupForm, self).__init__(*args, **kwargs)
        add_form_control(self)

class _ResetPasswordForm(forms.ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(_ResetPasswordForm, self).__init__(*args, **kwargs)
        add_form_control(self)


class _ChangePasswordForm(forms.ChangePasswordForm):
    def __init__(self, *args, **kwargs):
        super(_ChangePasswordForm, self).__init__(*args, **kwargs)
        add_form_control(self)

class _AddEmailForm(forms.AddEmailForm):
    def __init__(self, *args, **kwargs):
        super(_AddEmailForm, self).__init__(*args, **kwargs)
        add_form_control(self)