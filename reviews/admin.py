from django.contrib import admin

from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "book",
        "review",
        "author",
    )


admin.site.register(Review, ReviewAdmin)
