import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from books.models import Book

CustomUser = get_user_model()


class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews",)
    review = models.CharField(max_length=255)
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="reviews",
    )

    def __str__(self):
        return self.review

    def get_absolute_url(self):
        return reverse("review_detail", args=[str(self.id)])
