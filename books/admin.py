from django.contrib import admin
from .models import Book
from reviews.models import Review


class ReviewInline(admin.TabularInline):
    model = Review


class BookAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]
    list_display = (
        "id",
        "title",
        "author",
        "price",
    )


admin.site.register(Book, BookAdmin)
