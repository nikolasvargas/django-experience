from django.forms import ModelForm
from accounts.models import Transaction


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['description', 'value', 'category', 'note']
