from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    
    path('discover/', views.discover, name="discover"),
    path('dashboard/', views.dashboard, name="dashboard"), 
    
    # Trails
    path('trails/', views.trail_index, name="trail-index"),
    path('trails/<int:trail_id>/', views.trail_detail, name="trail-detail"),
    path('trails/create/', views.TrailCreate.as_view(), name="trail-create"),
    path('trails/<int:pk>/update/', views.TrailUpdate.as_view(), name='trail-update'),
    path('trails/<int:pk>/delete/', views.TrailDelete.as_view(), name='trail-delete'),
]