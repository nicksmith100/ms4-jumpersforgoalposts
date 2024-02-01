from django.db import models


class League(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    
    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Team(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=False, blank=False)
    league = models.ForeignKey('League', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Condition(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Year(models.Model):

    year = models.IntegerField(null=True, blank=True)
    

class Product(models.Model):
    
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    league = models.ForeignKey('League', null=True, blank=True, on_delete=models.SET_NULL)
    team = models.ForeignKey('Team', null=True, blank=True, on_delete=models.SET_NULL)
    year = models.ForeignKey('Year', null=True, blank=True, on_delete=models.SET_NULL)
    condition = models.ForeignKey('Condition', null=True, blank=True, on_delete=models.SET_NULL)
    home_away = models.CharField(max_length=254, null=True, blank=True)
    season = models.CharField(max_length=254, null=True, blank=True)
    player_issue = models.BooleanField(default=False)
    signed = models.BooleanField(default=False)

    def __str__(self):
        return self.name