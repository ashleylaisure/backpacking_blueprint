from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Trail, Day, Gear, category_choices, Food, meal_category, Note
from .forms import TrailForm, NoteForm, UserForm, LoginForm
from django.conf import settings
from django.utils import timezone
from django.db.models import Sum
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class Signin(LoginView):
    template_name = 'signin.html'
    authentication_form = LoginForm
    
def home(request):
    return render(request, 'home.html',)

def discover(request):
    return render(request, 'discover.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # add user to the database
            user = form.save()
            # log the user in
            login(request, user)
            return redirect('trail-index')
        else:
            error_message = 'Invalid sign up - try again'
    # if Post or Get request is bad render empty form
    form = UserForm()

    return render(request, 'signup.html', {
        'form' : form,
        'error_message' : error_message
    })

# --------------------------------- TRAIL
@login_required
def trail_index(request):
    today = timezone.now().date()
    view_type = request.GET.get('view', 'upcoming')
    
    if view_type == 'archive':
        trails = request.user.trail_set.filter(end_date__lt=today)
        is_archive = True
    else:
        trails = request.user.trail_set.filter(end_date__gte=today)
        is_archive = False
        
    return render(request, 'trails/index.html', {
        'trails' : trails,
        'is_archive' : is_archive,
        })


@login_required
def trail_detail(request, trail_id):
    trail = Trail.objects.get(id=trail_id)
    gear = Gear.objects.all()
    all_packed = all(item.packed for item in trail.gear.all())
    
    # Packed Gear Form - checkbox submission
    if request.method =="POST":
        # get the requesting gear item 
        gear_id = request.POST.get('gear_id')
        #get the input checkbox and store at True/checked
        packed = request.POST.get('packed') == 'True'
        
        # save the change to the database
        # get the gear id
        gear = Gear.objects.get(id=gear_id)
        gear.packed = packed
        gear.save()
        
        return redirect(request.path_info)

    return render(request, 'trails/detail.html', {
        'trail' : trail,
        'gear': gear,
        'all_packed' : all_packed,
        'mapbox_access_token' : settings.MAPBOX_ACCESS_TOKEN,
        })

class TrailCreate(LoginRequiredMixin, CreateView):
    model = Trail
    form_class = TrailForm
    
    # assing the loggin in user to the trail creation
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TrailUpdate(LoginRequiredMixin, UpdateView):
    model = Trail
    form_class = TrailForm

    
class TrailDelete(LoginRequiredMixin, DeleteView):
    model = Trail
    success_url = '/trails/'
    
# --------------------------------- DAY
@login_required
def day_detail(request, day_id):
    day = Day.objects.get(id=day_id)
    food = Food.objects.all()
    note_form = NoteForm()

    return render(request, 'days/detail.html', {
        'day' : day,
        'mapbox_access_token' : settings.MAPBOX_ACCESS_TOKEN,
        'food' : food,
        'category' : meal_category,
        'note_form' : note_form,
        })

class DayUpdate(LoginRequiredMixin, UpdateView):
    model = Day
    fields = ['start_campsite', 'finish_campsite', 'start_location', 'finish_location', 'distance', 'elevation']
    
# --------------------------------- GEAR
@login_required
def gear_index(request):
    gear = Gear.objects.filter(user=request.user)
    trails = Trail.objects.filter(user=request.user)
    
    return render(request, 'gear/index.html', {
        'gear' : gear,
        'trails' : trails,
        'categories' : category_choices,
    })
    
class GearCreate(LoginRequiredMixin, CreateView):
    model = Gear
    fields = ['category', 'name', 'brand', 'link', 'price', 'own', 'weight', 'weight_m', 'packed']
    success_url = '/gear/'
    
    # assing to the logged in user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    
class GearUpdate(LoginRequiredMixin, UpdateView):
    model = Gear
    fields = ['category', 'name', 'brand', 'link', 'price', 'own', 'weight', 'weight_m', 'packed']
    success_url = '/gear/'

    
class GearDelete(LoginRequiredMixin, DeleteView):
    model = Gear
    success_url = '/gear/'
    
    # overriding get()
    # def get(self, request, *args, **kwargs):
    #     return self.delete(request, *args, **kwargs)
    

# --------------------------------- M:M TRAIL:GEAR
@login_required
def available_gear(request, trail_id):
    trail = Trail.objects.get(id=trail_id)
    gear = Gear.objects.filter(user=request.user).exclude(id__in = trail.gear.all().values_list('id'))
    
    return render(request, 'gear/show.html', {
        'trail' : trail,
        'gear' : gear,
    })

@login_required
def trail_gear_details(request, trail_id):
    trail = Trail.objects.get(id=trail_id)
    gear = Gear.objects.all()
    
    category_totals = Gear.objects.filter().values('category').aggregate(total_amount=Sum('weight_lb'))

    return render(request, 'gear/trail_gear_details.html', {
        'trail' : trail,
        'gear': gear,
        'categories' : category_choices,
        'totals' : category_totals,
        })

@login_required
def associate_gear(request, trail_id, gear_id):
    Trail.objects.get(id=trail_id).gear.add(gear_id)
    return redirect('trail-gear-details', trail_id=trail_id)

@login_required
def remove_gear(request, trail_id, gear_id):
    Trail.objects.get(id=trail_id).gear.remove(gear_id)
    return redirect('trail-gear-details', trail_id=trail_id)

# --------------------------------- FOOD
class FoodCreate(LoginRequiredMixin, CreateView):
    model = Food
    fields = ['name', 'calories', 'weight', 'category']
    success_url = '/food/'
    
    # assing to the logged in user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@login_required
def food_index(request):
    food = Food.objects.filter(user=request.user)
    trails = Trail.objects.filter(user=request.user)
    
    return render(request, 'food/index.html', {
        'food' : food,
        'trails' : trails,
        # 'categories' : category_choices,
    })
    
class FoodUpdate(LoginRequiredMixin, UpdateView):
    model = Food
    fields = ['name', 'calories', 'weight', 'category']
    success_url = '/food/'
    
class FoodDelete(LoginRequiredMixin, DeleteView):
    model = Food
    success_url = '/food/'
    
# --------------------------------- MEAL PLAN
@login_required
def meal_plan(request, trail_id):
    trail = Trail.objects.get(id=trail_id)
    # get all days related to this trail
    days = trail.day_set.all()
    
    return render(request, 'mealplan/index.html', {
        'trail' : trail,
        'days' : days,
    })

@login_required
def available_food(request, day_id):
    day = Day.objects.get(id=day_id)
    # food = Food.objects.all()
    available_food = Food.objects.filter(user=request.user).exclude(id__in = day.food.all().values_list('id'))
    
    return render(request, 'food/show.html', {
        'day' : day,
        'food' : available_food,
    })

@login_required
def add_food(request, day_id, food_id):
    day = Day.objects.get(id=day_id)
    day.food.add(food_id)
    
    return redirect('meal-plan', trail_id=day.trail_id)

@login_required
def remove_food(request, day_id, food_id):
    day = Day.objects.get(id=day_id)
    day.food.remove(food_id)
    
    return redirect('meal-plan', trail_id=day.trail_id)

# --------------------------------- note
@login_required
def add_note(request, day_id):
    form = NoteForm(request.POST)
    
    if form.is_valid():
        new_note = form.save(commit=False)
        new_note.day_id = day_id
        new_note.save()
        
    return redirect('day-detail', day_id=day_id)

@login_required
def note_delete(request, day_id, note_id):
    note = Note.objects.get(id=note_id, day=day_id).delete()
    
    return redirect('day-detail', day_id=day_id)