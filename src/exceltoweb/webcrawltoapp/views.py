from django.shortcuts import render
from .models import PlantsPest
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
# Create your views here.


class PlantListView(ListView):
    template_name = "plantspest/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return PlantsPest.objects.all()
