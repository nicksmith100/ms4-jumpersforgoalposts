from django.contrib import admin

from .models import Subscriber
from products.models import Team


class NewsletterAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'email',
        'favourite_team',
        'other_team',
        'team_news_only',
    )


admin.site.register(Subscriber, NewsletterAdmin)
