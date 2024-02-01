from django.contrib import admin
from .models import League, Team, Condition, Year, Product

# Register your models here.
admin.site.register(League)
admin.site.register(Team)
admin.site.register(Condition)
admin.site.register(Year)
admin.site.register(Product)
