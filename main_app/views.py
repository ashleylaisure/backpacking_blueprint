from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Trail, Day, Gear, category_choices, Food
from .forms import TrailForm, PackedForm
from django.conf import settings

# Create your views here.
def home(request):
    return render(request, 'home.html')

def discover(request):
    return render(request, 'discover.html')

def dashboard(request):
    return render(request, 'dashboard.html')

# --------------------------------- TRAIL
def trail_index(request):
    trails = Trail.objects.all()
    return render(request, 'trails/index.html', {'trails' : trails})

def trail_detail(request, trail_id):
    trail = Trail.objects.get(id=trail_id)
    gear = Gear.objects.all()
    packed_form = PackedForm()

    return render(request, 'trails/detail.html', {
        'trail' : trail,
        'gear': gear,
        'packed' : packed_form,
        'mapbox_access_token' : settings.MAPBOX_ACCESS_TOKEN
        })

class TrailCreate(CreateView):
    model = Trail
    form_class = TrailForm
    # fields = ['name', 'start_date', 'end_date', 'location', 'distance', 'elevation', 'image']
    # automatically calls get_absolutle_url if success_url is not set

    

class TrailUpdate(UpdateView):
    model = Trail
    form_class = TrailForm
    # fields =  ['name', 'start_date', 'end_date', 'location', 'distance', 'elevation', 'image']
    
class TrailDelete(DeleteView):
    model = Trail
    success_url = '/trails/'
    
# --------------------------------- DAY
class DayUpdate(UpdateView):
    model = Day
    fields = ['start_location', 'finish_location', 'distance', 'elevation', 'notes']
    
# --------------------------------- GEAR
def gear_index(request):
    gear = Gear.objects.all()
    trails = Trail.objects.all()
    
    return render(request, 'gear/index.html', {
        'gear' : gear,
        'trails' : trails,
        'categories' : category_choices,
    })
    
class GearCreate(CreateView):
    model = Gear
    fields = '__all__'
    success_url = '/gear/'

    
class GearUpdate(UpdateView):
    model = Gear
    fields = '__all__'
    success_url = '/gear/'

    
class GearDelete(DeleteView):
    model = Gear
    success_url = '/gear/'
    
    # overriding get() to Directly delete
    # def get(self, request, *args, **kwargs):
    #     return self.delete(request, *args, **kwargs)
    
# --------------------------------- M:M TRAIL:GEAR
def available_gear(request, trail_id):
    trail = Trail.objects.get(id=trail_id)
    gear = Gear.objects.exclude(id__in = trail.gear.all().values_list('id'))
    
    return render(request, 'gear/show.html', {
        'trail' : trail,
        'gear' : gear,
    })
    
def trail_gear_details(request, trail_id):
    trail = Trail.objects.get(id=trail_id)
    gear = Gear.objects.all()

    return render(request, 'gear/trail_gear_details.html', {
        'trail' : trail,
        'gear': gear,
        'categories' : category_choices,
        })
    
def associate_gear(request, trail_id, gear_id):
    Trail.objects.get(id=trail_id).gear.add(gear_id)
    return redirect('trail-gear-details', trail_id=trail_id)

def remove_gear(request, trail_id, gear_id):
    Trail.objects.get(id=trail_id).gear.remove(gear_id)
    return redirect('trail-gear-details', trail_id=trail_id)

# --------------------------------- FOOD
class FoodCreate(CreateView):
    model = Food
    fields = '__all__'
    success_url = '/food/'
    
def food_index(request):
    food = Food.objects.all()
    # trails = Trail.objects.all()
    
    return render(request, 'food/index.html', {
        'food' : food,
        # 'trails' : trails,
        # 'categories' : category_choices,
    })
    
class FoodUpdate(UpdateView):
    model = Food
    fields = '__all__'
    success_url = '/food/'
    
class FoodDelete(DeleteView):
    model = Food
    success_url = '/food/'
    
# --------------------------------- MEAL PLAN
def meal_plan(request, trail_id):
    trail = Trail.objects.get(id=trail_id)
    # get all days related to this trail
    days = trail.day_set.all()
    
    return render(request, 'mealplan/index.html', {
        'trail' : trail,
        'days' : days,
    })

def available_food(request, day_id):
    day = Day.objects.get(id=day_id)
    food = Food.objects.all()
    return render(request, 'food/show.html', {
        'day' : day,
        'food' : food,
    })
    
def add_food(request, day_id, food_id):
    day = Day.objects.get(id=day_id)
    day.food.add(food_id)
    
    return redirect('meal-plan', trail_id=day.trail_id)