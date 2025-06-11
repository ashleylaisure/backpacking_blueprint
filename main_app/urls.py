from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    
    path('discover/', views.discover, name="discover"),
    path('dashboard/', views.dashboard, name="dashboard"), 
    
    # TRAIL
    path('trails/', views.trail_index, name="trail-index"),
    path('trails/archive/', views.trail_archive, name="trail-archive"),
    path('trails/<int:trail_id>/', views.trail_detail, name="trail-detail"),
    path('trails/create/', views.TrailCreate.as_view(), name="trail-create"),
    path('trails/<int:pk>/update/', views.TrailUpdate.as_view(), name='trail-update'),
    path('trails/<int:pk>/delete/', views.TrailDelete.as_view(), name='trail-delete'),
    
    
    # DAY
    path('days/<int:day_id>/', views.day_detail, name="day-detail"), 
    path('days/<int:pk>/update/', views.DayUpdate.as_view(), name ="update-day"),
    
    # GEAR
    path('gear/', views.gear_index, name='gear-index'),
    path('gear/create/', views.GearCreate.as_view(), name='gear-create'),
    path('gear/<int:pk>/update/', views.GearUpdate.as_view(), name='gear-update'),
    # path('gear/<int:pk>/packed/', views.packed_gear, name='packed'),
    path('gear/<int:pk>/delete/', views.GearDelete.as_view(), name='gear-delete'),
    
    # M:M TRAIL:GEAR
    path('trails/<int:trail_id>/associate-gear/', views.available_gear, name='available-gear-index'), 
    path('trails/<int:trail_id>/gear-details/', views.trail_gear_details, name='trail-gear-details'), 
    path('trails/<int:trail_id>/associate-gear/<int:gear_id>/', views.associate_gear, name='associate-gear'),
    path('trails/<int:trail_id>/remove-gear/<int:gear_id>/', views.remove_gear, name='remove-gear'), 
    
    #FOOD
    path('food/', views.food_index, name="food-index"), 
    path('food/create/', views.FoodCreate.as_view(), name='food-create'), 
    path('food/<int:pk>/update', views.FoodUpdate.as_view(), name='food-update'), 
    path('food/<int:pk>/delete', views.FoodDelete.as_view(), name='food-delete'),
    
    # M:M DAY:MEALS
    path('trails/<int:trail_id>/mealplan', views.meal_plan, name='meal-plan'),
    path('days/<int:day_id>/mealplan', views.available_food, name='available-food'),
    path('days/<int:day_id>/add-food/<int:food_id>/', views.add_food, name='add-food'), 
    path('days/<int:day_id>/remove-food/<int:food_id>/', views.remove_food, name='remove-food'), 
    
    # O2M TRAILS:todo
    # path('trails/<int:trail_id>/add-todo', views.add_todo, name="add-todo"),
    # path('todos/<int:pk>/update/', views.update_todo, name ="update-todo"),
    
]