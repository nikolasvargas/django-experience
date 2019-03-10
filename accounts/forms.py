from django.forms import ModelForm
from accounts.models import Transaction, Category


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['description', 'value', 'category', 'note']


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']
