from django.urls import path
from base import views

app_name = 'base'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('deposit-withdraw/', views.DepositWithdrawView.as_view(), name= 'deposit_withdraw'),
    path('transfer/', views.VerifyTransferView.as_view(), name= 'transfer'),
]