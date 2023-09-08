from apps.financial_manager.models import UserProfile, Transaction
# #
# def calculate_balance(self):
#
#     transactions = self.transactions.all()
#
#
#     balance = Decimal(0)
#
#     for transaction in transactions:
#         if transaction.amount > 0:
#             balance += transaction.amount
#         else:
#             balance -= abs(transaction.amount)
#
#     return balance