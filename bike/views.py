from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from .models import TwoWheeler


# Create your views here.
def bike(request):
    bike_all = TwoWheeler.objects.all()
    con = {
        'bike_all': bike_all,
    }
    return render(request, "bike/first.html", con)


def details(request, pk):
    try:
        x = TwoWheeler.objects.get(pk=pk)
    except TwoWheeler.DoesNotExist:
        raise Http404("Vehicle Not Found")
    con = {
        'x': x,
    }
    return render(request, "bike/details.html", con)


class BikeInsert(CreateView):
    model = TwoWheeler
    fields = ['Model_name', 'Company_name', 'Model_Info', 'Model_img', 'Price_before', 'Price_after']


