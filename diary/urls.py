from django.urls import path
from . import views

app_name = 'diary'

urlpatterns = [
    path('top/', views.diary_top, name='diary_top'),
]