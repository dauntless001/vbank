from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
import decimal, datetime
from accounts.models import Account
from django.contrib import messages

from base.utils import greeting

# Create your views here.


class IndexView(LoginRequiredMixin, View):
    template_name = 'index.html'
    def get(self, request, *args, **kwargs):
        currentTime = datetime.datetime.now()
        context = {
            'greeting' : greeting(currentTime),
        }
        return render(request, self.template_name, context)


class DepositWithdrawView(LoginRequiredMixin,View):
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            ajaxData = request.POST
            data = {}
            action = ajaxData['action']
            amount = ajaxData['amount']
            
            if action.lower() == 'deposit':
                self.request.user.account.balance += decimal.Decimal(amount)
            else:
                self.request.user.account.balance -= decimal.Decimal(amount)
            self.request.user.account.save()
            data['message'] = f'{action} of {amount} was successful'
            data['amount'] = amount
            data['availableBalance'] = self.request.user.account.balance
            return JsonResponse(data, safe=False)


class VerifyTransferView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            data = {}
            data['error'] = False
            ajaxData = request.GET
            try:
                accountNumber = ajaxData['accountNumber']
                account = Account.objects.get(number=accountNumber)
                data['name'] = account.user.get_full_name()
                if account == self.request.user.account:
                    data['name'] = 'You can\'t transfer to your Account, Try Deposit'
                    data['error']= True 
            except:
                data['name'] = 'Account Not Found'
                data['error'] = True
            return JsonResponse(data, safe=False)
    
    def post(self, request, *args, **kwargs):
        ajaxData = request.POST
        amount = ajaxData['amount']
        account = Account.objects.get(number=ajaxData['accountNumber'])
        account.balance += decimal.Decimal(amount)
        account.save()
        self.request.user.account.balance -= decimal.Decimal(amount)
        self.request.user.account.save()
        messages.success(request, f'Transfer of {amount} to {account.user.get_full_name()}')
        return redirect('base:index')
