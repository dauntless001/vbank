from django.db import models
from django.db.models.fields import TextField
from django.utils.crypto import get_random_string
from accounts.models import User


def gen_slug():
    return get_random_string(length=8)

class TimeBasedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class NameTimeBasedModel(TimeBasedModel):
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True

class NameDescTimeBasedModel(NameTimeBasedModel):
    desc = TextField()

    class Meta:
        abstract = True


