from django.urls import path
from receipts.views import (
    ReceiptListView,
    ReceiptCreateView,
    ExpenseCategoryListView,
    AccountListView,
    ExpenseCategoryCreateView,
)


urlpatterns = [
    path("", ReceiptListView.as_view(), name="home"),
    path("create/", ReceiptCreateView.as_view(), name="create_receipt"),
    path(
        "categories/",
        ExpenseCategoryListView.as_view(),
        name="list_expensecategories",
    ),
    path("accounts/", AccountListView.as_view(), name="list_accounts"),
    path(
        "categories/create/",
        ExpenseCategoryCreateView.as_view(),
        name="create_category",
    ),
]
