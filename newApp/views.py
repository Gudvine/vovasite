from urllib import request
from django.views.generic import ListView
from django.shortcuts import render


from .models import Order, Videomaker, Score


class ScoreExp:
	def get_score(self):
		return Score.objects.all()


def index(request):
	return render(request, "index.html")


class SearchResultsView(ListView):
	paginate_by = 3
	model = Videomaker
	template_name = 'search_results.html'

	def get_queryset(self):
		queryset = self.request.GET.get('value', default="")
		object_list = Videomaker.objects.filter(work_tag__tag_name__icontains=queryset)
		return object_list

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context["value"] = self.request.GET.get("value")
		return context


class CabinetView(ListView):
	model = Order
	template_name = 'cabinet.html'


class FilterVideomakerView(ListView):
	model = Videomaker
	template_name = 'search_results.html'

	def get_queryset(self):
		queryset = self.request.GET.get('optionchecked')
		object_list = Videomaker.objects.filter(experience_level__contains=queryset)
		return object_list
