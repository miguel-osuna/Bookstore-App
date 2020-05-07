from django.urls import path

from .views import (
    ReviewListView,
    BookReviewListView,
    UserReviewListView,
    ReviewCreateView,
    ReviewDetailView,
    ReviewUpdateView,
    ReviewDeleteView,
)

urlpatterns = [
    path("", ReviewListView.as_view(), name="review_list"),
    path("<book>/", BookReviewListView.as_view(), name="book_review_list"),
    path("<username>/", UserReviewListView.as_view(), name="user_review_list"),
    path("new/", ReviewCreateView.as_view(), name="review_new"),
    path("<uuid:pk>/", ReviewDetailView.as_view(), name="review_detail"),
    path("<uuid:pk>/edit/", ReviewUpdateView.as_view(), name="review_edit"),
    path("<uuid:pk>/delete/", ReviewDeleteView.as_view(), name="review_delete"),
]
