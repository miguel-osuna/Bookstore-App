from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Review


class ReviewListView(LoginRequiredMixin, ListView):
    model = Review
    template_name = "reviews/review_list.html"
    context_object_name = "review_list"
    login_url = "account_login"


class BookReviewListView(LoginRequiredMixin, ListView):
    model = Review
    template_name = "reviews/book_review_list.html"
    context_object_name = "review_list"
    login_url = "account_login"


class UserReviewListView(LoginRequiredMixin, ListView):
    model = Review
    template_name = "reviews/user_review_list.html"
    context_object_name = "review_list"
    login_url = "account_login"


class ReviewDetailView(LoginRequiredMixin, DetailView):
    model = Review
    template_name = "reviews/review_detail.html"
    context_object_name = "review"
    login_url = "account_login"


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    template_name = "reviews/review_new.html"
    fields = ("book", "review", "author")
    login_url = "account_login"


class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Review
    template_name = "reviews/review_edit.html"
    context_object_name = "review"
    fields = ("review",)
    login_url = "account_login"


class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Review
    template_name = "reviews/review_delete.html"
    context_object_name = "review"
    login_url = "account_login"
    success_url = reverse_lazy("review_list")
