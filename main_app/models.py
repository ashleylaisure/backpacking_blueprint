from django.db import models
from django.urls import reverse
from datetime import timedelta

cover_images = (
    ('1', ''),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ('13', '13'),
    ('14', '14'),
    ('15', '15'),
)

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
    ('g', 'g'),
    ('kg', 'kg'),
)

# Create your models here.

class Trail(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField('Starting Date')
    end_date = models.DateField('End Date')
    # how to check that the end date entered is after start date???
    location = models.CharField(max_length=200)
    distance = models.DecimalField(max_digits=10, decimal_places=2,  blank=True, null=True)
    elevation = models.DecimalField(max_digits=10, decimal_places=2,  blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)
    image = models.CharField(max_length=2, choices=cover_images)
    
    # automatically calculate and save the duration based on the date inputs before submitting
    def save(self, *args, **kwargs):
        if self.start_date and self.end_date:
            self.duration = self.end_date - self.start_date
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name
    
    # method to get the url for this particular instance
    def get_absolute_url(self):
        return reverse("trail-detail", kwargs={"trail_id": self.id})
    
class Day(models.Model):
    day = models.IntegerField()
    date = models.DateField()
    
    start_location = models.CharField(max_length=200)
    finish_location = models.CharField(max_length=200)
    distance = models.DecimalField(max_digits=10, decimal_places=2,  blank=True, null=True)
    elevation = models.DecimalField(max_digits=10, decimal_places=2,  blank=True, null=True)
    notes = models.TextField(max_length=250)
    
    trail = models.ForeignKey(Trail, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Day {self.day} on {self.date}"
    
    class Meta:
        ordering = ['date']
        
    # return to the trail-detail that the day belongs to
    def get_absolute_url(self):
        return reverse("trail-detail", kwargs={"trail_id": self.trail.id})
    
class Gear(models.Model):
    category = models.CharField(max_length=20, choices=category_choices)
    name = models.CharField(("Item name"), max_length=200)
    brand = models.CharField(max_length=200, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    own = models.BooleanField()
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    weight_m = models.CharField(("Weight Measurment"), max_length=2, choices=weight_choices, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    # def get_absolute_url(self):
    #     return reverse("gear-detail", kwargs={"pk": self.pk})
    