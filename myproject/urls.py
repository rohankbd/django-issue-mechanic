from django.urls import path
from myapp import views

urlpatterns = [
    path('create_issue/', views.create_issue, name='create_issue'),
    path('check_mechanic_availability/', views.check_mechanic_availability, name='check_mechanic_availability'),
]
