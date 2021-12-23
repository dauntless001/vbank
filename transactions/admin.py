from django.contrib import admin
from transactions.models import Transaction
# Register your models here.


class TransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'desc','type','created_at']

admin.site.register(Transaction, TransactionAdmin)