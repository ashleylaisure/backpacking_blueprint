from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Trail, Day
from datetime import timedelta

# function is triggered after trail has been saved
@receiver(post_save, sender=Trail)
# the function create_days is the reciver listing for the signal
# and the signal is loaded in apps.py
def create_days(sender, instance, created, **kwargs):
    start_date = instance.start_date
    end_date = instance.end_date
    # check if a trail was created
    if created:
        # loop over the days set in Trail
        current_date = start_date
        trail_day = 1
        while current_date <= end_date:
            Day.objects.create(trail=instance, date=current_date, day=trail_day)
            trail_day += 1
            current_date += timedelta(days=1)
    
    # if the trip dates change
    else:
        #filter out days that are outside the new date range
        Day.objects.filter(trail=instance).exclude(date__range=(start_date, end_date)).delete()
        
        # fetch all the existing day.date for that trail in the date range as a set
        overlap_dates = set(
            Day.objects.filter(trail=instance)
            .values_list('date', flat=True)
        )
        
        # add any missing days
        current_date = start_date
        trail_day = 1
        while current_date <= end_date:
            if current_date not in overlap_dates:
                Day.objects.create(trail=instance, date=current_date, day=trail_day)
            else:
                Day.objects.filter(trail=instance, date=current_date).update(day=trail_day)
            trail_day += 1
            current_date += timedelta(days=1)