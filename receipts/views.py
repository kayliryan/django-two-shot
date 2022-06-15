from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from receipts.models import Receipt

# Create your views here.


class ReceiptListView(LoginRequiredMixin, ListView):
    model = Receipt
    template_name = "receipts/list.html"

    def get_query_set(self):
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
        receipt = form.save(commit=False)
        receipt.purchaser = self.request.user
        receipt.save()
        return redirect("home")
