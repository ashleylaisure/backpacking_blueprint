from django.db import models
from django.conf import settings
import geocoder
from django.urls import reverse
from django.db.models.functions import Lower
from django.utils import timezone
from datetime import timedelta
from django.db.models import Sum
from decimal import Decimal
from collections import defaultdict
from django.contrib.auth.models import User

category_choices = (
    ('big_three', 'Big Three (Backpack, Tent, Sleeping Bag)'),
    ('water', 'Water'),
    ('food', 'Food Storage'),
    ('cooking', 'Cooking & Utensils'),
    ('clothing', 'Clothing & Footwear'),
    ('toiletries', 'Toiletries'),
    ('tools', 'Tools'),
    ('saftey', 'Saftey'),
    ('electronics', 'Electronics'),
    ('entertainment', 'Entertainment'),
)

weight_choices = (
    ('oz', 'oz'),
    ('lb', 'lb'),
)

meal_category = (
    ('breakfast', 'Breakfast'),
    ('lunch', 'Lunch'),
    ('snack', 'Snack'),
    ('dinner', 'Dinner'),
    ('drinks', 'Drinks'),
)

cover_image_choices = (
    ('cover_image_1.jpg', 'Image 1'),
    ('cover_image_2.jpg', 'Image 2'),
    ('cover_image_3.jpg', 'Image 3'),
    ('cover_image_4.jpg', 'Image 4'),
    ('cover_image_5.jpg', 'Image 5'),
    ('cover_image_6.jpg', 'Image 6'),
    ('cover_image_7.jpg', 'Image 7'),
    ('cover_image_8.jpg', 'Image 8'),
    ('cover_image_10.jpg', 'Image 10'),
)

# Create your models here.
class Gear(models.Model):
    category = models.CharField(max_length=20, choices=category_choices)
    name = models.CharField(("Item name"), max_length=200)
    brand = models.CharField(max_length=200, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    own = models.BooleanField(default=False)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    weight_m = models.CharField(("Weight Measurment"), max_length=2, choices=weight_choices, blank=True, null=True)
    packed = models.BooleanField(default=False)
    # is_suggested = models.BooleanField(default=False)

    weight_lb = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    
    # foreign key linking to a user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        if self.weight and self.weight_m :
            if self.weight_m == 'oz':
                self.weight_lb = self.weight * Decimal('0.0625')
            else:
                self.weight_lb = self.weight
                
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = [Lower('name')]
        

class Trail(models.Model):
    name = models.CharField(('Adventure Name'),max_length=200)
    start_date = models.DateField('Start Date')
    end_date = models.DateField('End Date')
    location_name = models.CharField(('Name'), max_length=200, blank=True, null=True)
    location = models.CharField(('Address'), max_length=200, blank=True, null=True)
    distance = models.DecimalField( ('Distance (mi)'), max_digits=10, decimal_places=2,  blank=True, null=True)
    elevation = models.DecimalField(('Elevation Gain (ft)'), max_digits=10, decimal_places=2,  blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)
    # image = models.ImageField(('Cover Image'), upload_to='cover_image/', default='cover_image_1.jpg', blank=True, null=True)
    image = models.CharField(('Cover Image'), max_length=100, choices=cover_image_choices)
    
    # foreign key linking to a user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # MAP FEATURE
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    
    
    # when the instance is saved convert the location into lat/long
    def save(self, *args, **kwargs):
        if self.location:
            # API call
            g = geocoder.mapbox(self.location, key=settings.MAPBOX_ACCESS_TOKEN)
            # return the lat/long of the location in a list
            g = g.latlng
            # assign lat/long to model
            self.lat = g[0]
            self.long = g[1]

    # automatically calculate and save the duration based on the date inputs before submitting
        if self.start_date and self.end_date:
            self.duration = self.end_date - self.start_date + timedelta(days=1)
            
        super().save(*args, **kwargs)
    
    # when instance is deleted, delete image file
    # def delete(self):
    #     self.image.delete()
    #     super().delete()
        
    class Meta:
        ordering = ['start_date']
        
    # M:M relationship with Gear
    gear = models.ManyToManyField(Gear)
    
    def total_weight(self):
        return sum(gear.weight_lb for gear in self.gear.all() if gear.weight_lb)
    
    # defaultdict(float) initializes each new category with a default value of 0.0
    def weight_by_category(self):
        category_totals = defaultdict(float)
        for gear in self.gear.all():
            if gear.weight_lb:
                category_totals[gear.category] += float(gear.weight_lb)
        return dict(category_totals)
    
    def __str__(self):
        return self.name
    
    # method to get the url for this particular instance
    def get_absolute_url(self):
        return reverse("trail-detail", kwargs={"trail_id": self.id})

class Food(models.Model):
    name = models.CharField(max_length=200)
    calories = models.IntegerField(blank=True, null=True)
    weight = models.DecimalField(("Weight (g)"), max_digits=10, decimal_places=2, default=Decimal('0.00'), blank=True, null=True)
    # category = models.CharField(max_length=20, choices=meal_category, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    # foreign key linking to a user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        ordering = [Lower('name')]
    
class Day(models.Model): 
    day = models.IntegerField()
    date = models.DateField()
    start_campsite = models.CharField(('Name'),max_length=200, blank=True, null=True)
    finish_campsite = models.CharField(('Name'),max_length=200, blank=True, null=True)
    start_location = models.CharField(('Address'), max_length=200, blank=True, null=True)
    finish_location = models.CharField(('Address'), max_length=200, blank=True, null=True)
    distance = models.DecimalField(('Distance (mi)'), max_digits=10, decimal_places=2,  blank=True, null=True)
    elevation = models.DecimalField(('Elevation Gain (ft)'), max_digits=10, decimal_places=2,  blank=True, null=True)
    # notes = models.TextField(max_length=250, blank=True, null=True)
    
    # MAP FEATURE
    start_lat = models.FloatField(blank=True, null=True)
    start_long = models.FloatField(blank=True, null=True)
    
    finish_lat = models.FloatField(blank=True, null=True)
    finish_long = models.FloatField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if self.start_location:
            g = geocoder.mapbox(self.start_location, key=settings.MAPBOX_ACCESS_TOKEN)
            g = g.latlng
            self.start_lat = g[0]
            self.start_long = g[1]
            
        if self.finish_location:
            g = geocoder.mapbox(self.finish_location, key=settings.MAPBOX_ACCESS_TOKEN)
            g = g.latlng
            self.finish_lat = g[0]
            self.finish_long = g[1]
            
        super().save(*args, **kwargs)

    # relationships
    trail = models.ForeignKey(Trail, on_delete=models.CASCADE)
    food = models.ManyToManyField(Food)
    
    def total_calories(self):
        return sum(food.calories for food in self.food.all())
    
    def total_weight_g(self):
        return sum(food.weight for food in self.food.all())
    
    def total_weight_lb(self):
        return self.total_weight_g() * Decimal(0.00220462)
    
    def __str__(self):
        return f"Day {self.day} on {self.date}"
    
    class Meta:
        ordering = ['date']
        
    def get_absolute_url(self):
        return reverse("day-detail", kwargs={"day_id": self.id})
    
class Note(models.Model):
    note = models.TextField(max_length=250)
    created = models.DateField(auto_now_add=True)
    
    # Trail Foreign Key
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    # foreign key linking to a user instance
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['created']
    
    def __str__(self):
        return f'Note created on {self.created}'
