from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    
    path('discover/', views.discover, name="discover"),
    path('dashboard/', views.dashboard, name="dashboard"), 
    
    # TRAIL
    path('trails/', views.trail_index, name="trail-index"),
    path('trails/<int:trail_id>/', views.trail_detail, name="trail-detail"),
    path('trails/create/', views.TrailCreate.as_view(), name="trail-create"),
    path('trails/<int:pk>/update/', views.TrailUpdate.as_view(), name='trail-update'),
    path('trails/<int:pk>/delete/', views.TrailDelete.as_view(), name='trail-delete'),
    
    # DAY
    path('days/<int:pk>/update/', views.DayUpdate.as_view(), name ="update_day"),
    
    # GEAR
    path('gear/', views.GearList.as_view(), name='gear-index'),
    path('gear/<int:pk>/', views.GearDetail.as_view(), name='gear-detail'),
    path('gear/create/', views.GearCreate.as_view(), name='gear-create'),
    path('gear/<int:pk>/update/', views.GearUpdate.as_view(), name='gear-update'), 
    path('gear/<int:pk>/delete/', views.GearDelete.as_view(), name='gear-delete'), 
    
]