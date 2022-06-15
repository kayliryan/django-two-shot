from django.contrib import admin

from receipts.models import Receipt, Account, ExpenseCategory

# Register your models here.


class ReceiptAdmin(admin.ModelAdmin):
    pass


class ExpenseCategoryAdmin(admin.ModelAdmin):
    pass


class AccountAdmin(admin.ModelAdmin):
    pass


admin.site.register(Receipt, ReceiptAdmin)
admin.site.register(ExpenseCategory, ExpenseCategoryAdmin)
admin.site.register(Account, AccountAdmin)
