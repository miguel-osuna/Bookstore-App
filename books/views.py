from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

from .models import Book


class BookListView(LoginRequiredMixin, ListView):
    # BookListView model
    model = Book
    # BookListView template
    template_name = "books/book_list.html"
    context_object_name = "book_list"
    login_url = "account_login"


class BookSearchResultsListView(LoginRequiredMixin, ListView):
    model = Book
    # BookSearchResultsListView template
    template_name = "books/book_search_results.html"
    # Context object name for template
    context_object_name = "book_list"
    # Redirection URL for login
    login_url = "account_login"

    def get_queryset(self):
        query = self.request.GET.get("q")

        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    # BookDetailView template
    template_name = "books/book_detail.html"
    # Context object name for template
    context_object_name = "book"
    # Redirection URL for login
    login_url = "account_login"
    # Permissions required for the view
    permission_required = "books.special_status"


class BookCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Book
    # Form fields available
    fields = ("title", "author", "price", "cover")
    # BookCreateView template
    template_name = "books/book_new.html"
    # Redirection URL for login
    login_url = "account_login"
    # Permissions required for the view
    permission_required = "books.special_status"


class BookUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Book
    # BookUpdateView template
    template_name = "books/book_edit.html"
    # Context object name for template
    context_object_name = "book"
    # Form fields available
    fields = ("title", "author", "price")
    # Redirection URL for login
    login_url = "account_login"
    # Permissions required for the view
    permission_required = "books.special_status"


class BookDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Book
    # BookDeleteView template
    template_name = "books/book_delete.html"
    # Context object name for template
    context_object_name = "book"
    # Redirection URL for login
    login_url = "account_login"
    # Permissions required for the view
    permission_required = "books.special_status"
    # Redirection url name after deleting entry
    success_url = reverse_lazy("book_list")
