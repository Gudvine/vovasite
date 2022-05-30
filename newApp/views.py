from urllib import request
from django.views.generic import ListView
from django.shortcuts import render


from .models import Videomaker


def index(request):
	return render(request, "index.html")


class SearchResultsView(ListView):
	model = Videomaker
	template_name = 'search_results.html'

def cabinet(request):
	return render(request, "cabinet.html")
