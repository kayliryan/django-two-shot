from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from receipts.models import Receipt

# Create your views here.


class ReceiptListView(LoginRequiredMixin, ListView):
    model = Receipt
    template_name = "receipts/list.html"

    def get_query_set(self):
        return Receipt.objects.filter(purchaser=self.request.user)
        # this filters the Receipt objects where purchaser equals the logged in user
