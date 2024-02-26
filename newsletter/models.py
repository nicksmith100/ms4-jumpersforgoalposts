from django.db import models

from products.models import Team
from profiles.models import UserProfile

class Subscriber(models.Model):

    name = models.CharField(max_length=254)
    email = models.CharField(max_length=254)
    favourite_team = models.ForeignKey(
        'products.Team', null=True, blank=True, on_delete=models.SET_NULL)
    other_team = models.CharField(max_length=254, null=True, blank=True)
    team_news_only = models.BooleanField(default=False)

    def __str__(self):
        return self.name
