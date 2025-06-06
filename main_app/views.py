from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Trail, Day, Gear, category_choices, Meal
from .forms import TrailForm, PackedForm

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

# --------------------------------- MEAL
class MealCreate(CreateView):
    model = Meal
    fields = '__all__'
    success_url = '/meals/'
    
def meal_index(request):
    meal = Meal.objects.all()
    # trails = Trail.objects.all()
    
    return render(request, 'meal/index.html', {
        'meal' : meal,
        # 'trails' : trails,
        # 'categories' : category_choices,
    })
    
class MealUpdate(UpdateView):
    model = Meal
    fields = '__all__'
    success_url = '/meals/'
    
class MealDelete(DeleteView):
    model = Meal
    success_url = '/meals/'