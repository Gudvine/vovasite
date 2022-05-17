from unicodedata import name
from django.urls import path

from newApp import views

urlpatterns = [
	path('', views.index, name='index'),
	path('search_results/', views.SearchResultsView.as_view(), name="search_results")  # подумать
]
