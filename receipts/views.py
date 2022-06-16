from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from receipts.models import Account, ExpenseCategory, Receipt

# Create your views here.


class ReceiptListView(LoginRequiredMixin, ListView):
    model = Receipt
    template_name = "receipts/list.html"

    def get_queryset(self):
        return Receipt.objects.filter(purchaser=self.request.user)
        # this filters the Receipt objects where purchaser equals the logged in user
        # makes sense that it's purchaser because that's defined in our model, not
        # owner or user. .... the .user comes from the USER_MODEL so it's defined
        # by django in the black magic, not by us


class ReceiptCreateView(LoginRequiredMixin, CreateView):
    model = Receipt
    template_name = "receipts/create.html"
    fields = [
        "vendor",
        "total",
        "tax",
        "date",
        "category",
        "account",
    ]

    def form_valid(self, form):
        receipt = form.save(
            commit=False
        )  # receipt could be replaced with item throughout
        receipt.purchaser = self.request.user
        receipt.save()
        return redirect("home")


class ExpenseCategoryListView(LoginRequiredMixin, ListView):
    model = ExpenseCategory
    template_name = "expense_categories/list.html"

    def get_queryset(self):
        return ExpenseCategory.objects.filter(owner=self.request.user)


class AccountListView(LoginRequiredMixin, ListView):
    model = Account
    template_name = "accounts/list.html"

    def get_queryset(self):
        return Account.objects.filter(owner=self.request.user)


class ExpenseCategoryCreateView(LoginRequiredMixin, CreateView):
    model = ExpenseCategory
    template_name = "expense_categories/create.html"
    fields = [
        "name",
    ]

    def form_valid(self, form):
        item = form.save(commit=False)
        item.owner = self.request.user
        item.save()
        return redirect("list_expensecategories")


class AccountCreateView(LoginRequiredMixin, CreateView):
    model = Account
    template_name = "accounts/create.html"
    fields = [
        "name",
        "number",
    ]

    def form_valid(self, form):
        item = form.save(commit=False)
        item.owner = self.request.user
        # we have to get owner from somewhere since it's specified in our
        # model and we didn't make the user input it
        # that's why we have to do this function form_valid, to stop it from saving
        # add something to the owner field, and then save it again
        item.save()
        return redirect("list_accounts")
