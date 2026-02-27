from django.urls import path
from . import views

urlpatterns = [
    path('drf-login/', views.DRFLoginView.as_view(), name='drf-login'),
    
]
