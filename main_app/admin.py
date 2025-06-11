from django.contrib import admin
from .models import Trail, Day, Gear, Food, Todo

# Register your models here.
admin.site.register(Trail)
admin.site.register(Day) 
admin.site.register(Gear)
admin.site.register(Food)
admin.site.register(Todo)

