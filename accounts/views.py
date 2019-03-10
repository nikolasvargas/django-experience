from django.shortcuts import render, redirect
from datetime import datetime
from accounts.models import Transaction
from accounts.forms import TransactionForm


def home(request):
    data = {
        'now': datetime.now(),
        'transactions': ['t1', 't2', 't3']
    }
    return render(request, 'accounts/home.html', data)


def listing(request):
    data = {}
    data['transactions'] = Transaction.objects.all()
    return render(request, 'accounts/listing.html', data)


def new_transaction(request):
    data = {}
    data['form'] = TransactionForm(request.POST or None)

    if data['form'].is_valid():
        data['form'].save()
        return redirect('list-transactions')

    return render(request, 'accounts/form.html', data)


def update_transaction(request, pk):
    data = {}
    transaction = Transaction.objects.get(pk=pk)
    form = TransactionForm(request.POST or None, instance=transaction)

    if form.is_valid():
        form.save()
        return redirect('list-transactions')

    data['form'] = form
    data['transaction'] = transaction
    return render(request, 'accounts/form.html', data)


def delete_transaction(request, pk):
    transaction = Transaction.objects.get(pk=pk)
    transaction.delete()
    return redirect('list-transactions')
