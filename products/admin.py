from django.contrib import admin
from .models import League, Team, Condition, Product

# Register your models here.
class LeagueAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class TeamAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class ConditionAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'team',
        'year',
        'condition',
        'price',
        'image',
    )

    ordering = ('year', 'team',)

admin.site.register(League, LeagueAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Condition, ConditionAdmin)
admin.site.register(Product, ProductAdmin)