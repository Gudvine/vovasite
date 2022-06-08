from django.urls import path

from newApp import views

urlpatterns = [
	path('', views.index, name='index'),
	path('search_results/', views.SearchResultsView.as_view(), name="search_results"),
	path('search_results/<int:pk>/', views.VideomakerDetailView.as_view(), name="maker"),
	path('filter/', views.FilterVideomakerView.as_view(), name="filter"),
	path('cabinet/', views.CabinetView.as_view(), name="cabinet"),
]
