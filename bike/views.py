from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import TwoWheeler


# Create your views here.
def bike(request):
    a = TwoWheeler.objects.all()
    template = loader.get_template("bike/first.html")
    con = {
        'a': a,
    }
    return HttpResponse(template.render(con, request))

def details(request, v_id):
    try:
        x = TwoWheeler.objects.get(pk=v_id)
    except TwoWheeler.DoesNotExist:
        raise Http404("Vehicle Not Found")
    template = loader.get_template("bike/details.html")
    con = {
        'x': x,
    }
    return HttpResponse(template.render(con, request))