from django.contrib import admin

from .models import Newsletter
from products.models import Team

class NewsletterAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'email',
        'favourite_team',
        'other_team',
        'team_news_only',
    )

admin.site.register(Newsletter, NewsletterAdmin)