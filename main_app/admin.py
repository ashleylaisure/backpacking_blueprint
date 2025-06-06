from django.contrib import admin
from .models import Trail, Day, Gear, Meal, MealPlan

# Register your models here.
admin.site.register(Trail)
admin.site.register(Day)
admin.site.register(Gear)
admin.site.register(Meal)
admin.site.register(MealPlan)