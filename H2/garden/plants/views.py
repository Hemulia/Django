from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Plant

class AboutView(TemplateView):
	template_name = "plants/about.html"

class PlantListView(ListView):
	model = Plant

