from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django_daraja.mpesa.core import MpesaClient

from apiApplictation.forms import PaymentForm


# Create your views here.
@csrf_exempt
def mpesa_callback(request):
    # Process Mpesa callback data
    # ...
    return HttpResponse("Callback received.")

def index(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            client = MpesaClient()
            phone_number = '0701582114'
            amount = 1
            account_reference = 'reference'
            transaction_desc = 'Description'
            callback_url = 'https://api.darajambili.com/express-payment'
            response = client.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
            return HttpResponse(response)
        return HttpResponse("Payment initiated successfully.")
    else:
        form = PaymentForm()

    return render(request, 'payment.html', {'form': form})



# def index(request):
#     client = MpesaClient()
#     phone_number = '0701582114'
#     amount = 1
#     account_reference = 'reference'
#     transaction_desc = 'Description'
#     callback_url = 'https://api.darajambili.com/express-payment'
#     response = client.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
#     return HttpResponse(response)
#
