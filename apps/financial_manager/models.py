from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal


class UserProfile(models.Model):
    user = models.OneToOneField(User, max_length=100, on_delete=models.CASCADE, related_name='profile')

    def update_balance(self):
        transactions = self.transactions.all()

        balance = Decimal(0)

        for transaction in transactions:
            if transaction.amount > 0:
                balance += transaction.amount
            else:
                balance -= abs(transaction.amount)

        self.balance = balance
        self.save()

    def __str__(self):
        return str(self.user)


class UserAccount(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='accounts')
    name = models.CharField(max_length=50, blank=False)
    balance = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.name


class TransactionCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    name = models.CharField(max_length=50, null=False)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(TransactionCategory)
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE, related_name='transactions')

    def __str__(self):
        return self.name

