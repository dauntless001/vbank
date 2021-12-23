from django.db import models
from vbank.settings.helpers import model_helper
# Create your models here.
class Transaction(model_helper.TimeBasedModel):
    class TransactionTypeChoice(models.TextChoices):
        credit = 'Credit', 'Credit'
        debit = 'Debit', 'Debit'
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    desc = models.TextField()
    type = models.CharField(max_length=20, default=TransactionTypeChoice.credit,
    choices=TransactionTypeChoice.choices)

    def __str__(self):
        return f'{self.user.get_full_name()} transaction'
