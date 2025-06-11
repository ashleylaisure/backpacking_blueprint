from django.contrib import admin
from .models import Trail, Day, Gear, Food, Note

# Register your models here.
admin.site.register(Trail)
admin.site.register(Day) 
admin.site.register(Gear)
admin.site.register(Food)
admin.site.register(Note)

