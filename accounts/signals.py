from accounts.models import Account, User
from django.db.models.signals import post_save
import random

def account_post_save(sender, instance,created, *args, **kwargs):
    if created:
        # Profile.objects.create(user=user)
        Account.objects.create(user=instance, number = str(random.randint(111111111, 999999999)))




post_save.connect(account_post_save, sender=User)