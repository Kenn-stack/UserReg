from django.urls import path
from .views import Search

urlpatterns = [
    path('search/dashboard/', Search, name = 'search'),
]