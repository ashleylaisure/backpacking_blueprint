from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Trail, Day, Gear
from .forms import TrailForm

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
    
    return render(request, 'trails/detail.html', {
        'trail' : trail,

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
class GearList(ListView):
    model = Gear
    
class GearDetail(DetailView):
    model = Gear
    
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
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)