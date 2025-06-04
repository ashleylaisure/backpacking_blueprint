from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Trail
from .forms import TrailForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def discover(request):
    return render(request, 'discover.html')

def dashboard(request):
    return render(request, 'dashboard.html')

# ------------------
def trail_index(request):
    trails = Trail.objects.all()
    return render(request, 'trails/index.html', {'trails' : trails})

def trail_detail(request, trail_id):
    trail = Trail.objects.get(id=trail_id)
    return render(request, 'trails/detail.html', {'trail' : trail})

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