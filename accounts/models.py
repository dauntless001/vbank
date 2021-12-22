from django.db import models
from django.contrib.auth.models import AbstractUser

from vbank.settings.helpers.image_helper import get_upload_path
import random
# Create your models here.



class User(AbstractUser):
    pass


class Account(models.Model):
    user = models.OneToOneField('accounts.User', on_delete=models.CASCADE)
    number = models.CharField(max_length=12, unique=True, default=1)
    balance = models.DecimalField(max_digits=50, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.user.email} account'
    