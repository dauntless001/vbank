from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from transactions.models import Transaction
# Create your views here.


class TransactionView(LoginRequiredMixin,View):
    template_name = 'transactions.html'
    def get(self, request, *args, **kwargs):
        context = {
            'transactions': Transaction.objects.filter(user=self.request.user).order_by('-created_at')
        }
        return render(request, self.template_name, context)