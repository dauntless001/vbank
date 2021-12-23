from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from transactions.models import Transaction
from transactions.utils import render_to_pdf
# Create your views here.


class TransactionView(LoginRequiredMixin,View):
    template_name = 'transactions.html'
    def get(self, request, *args, **kwargs):
        context = {
            'transactions': Transaction.objects.filter(user=self.request.user).order_by('-created_at')
        }
        return render(request, self.template_name, context)
    
def download_transaction_pdf(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'transactions':transactions
    }
    pdf = render_to_pdf('transaction_pdf.html', context)
    return HttpResponse(pdf, content_type='application/pdf')