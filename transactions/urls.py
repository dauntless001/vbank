from django.urls import path
from transactions import views

app_name = 'transactions'

urlpatterns = [
    path('', views.TransactionView.as_view(), name='transactions'),
    path('download/', views.download_transaction_pdf, name='download'),
]