from django.contrib import admin
from .models import UserProfile, UserAccount, TransactionCategory, Transaction


class UserAccountInline(admin.TabularInline):
    model = UserAccount
    extra = 0


class TransactionInline(admin.TabularInline):
    model = Transaction
    extra = 0


class UserProfileAdmin(admin.ModelAdmin):
    inlines = [UserAccountInline, TransactionInline]


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserAccount)
admin.site.register(TransactionCategory)
admin.site.register(Transaction)


