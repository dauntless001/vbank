from django.urls import reverse_lazy

ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS =3
ACCOUNT_EMAIL_REQUIRED =True
ACCOUNT_EMAIL_VERIFICATION = ["madatory","optional","none"][2]
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_AUTHENTICATION_METHOD = ["username", "email", "username_email"][1]
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT =300 #In seconds
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL  = reverse_lazy('accounts:settings')
ACCOUNT_UNIQUE_EMAIL =True
ACCOUNT_FORMS = {
    'add_email': 'vbank.settings.helpers.form_helper._AddEmailForm',
    'login': 'vbank.settings.helpers.form_helper._LoginForm',
    'signup': 'vbank.settings.helpers.form_helper._SignupForm',
    'reset_password' : 'vbank.settings.helpers.form_helper._ResetPasswordForm',
    'change_password' : 'vbank.settings.helpers.form_helper._ChangePasswordForm',
}

ACCOUNT_USERNAME_REQUIRED = False