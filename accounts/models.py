from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=150)
    value = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    note = models.TextField(null=True, blank=True)

    # class Meta:
    #     verbose_name_plural = "Transactions"

    def __str__(self):
        return self.description
