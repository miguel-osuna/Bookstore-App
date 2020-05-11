from django.contrib import admin

from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "book",
        "author",
        "review",
    )
    list_filter = ("book", "review", "author")
    search_fields = ("book",)
    ordering = ("book", "author")


admin.site.register(Review, ReviewAdmin)
