from django.http import HttpResponse
from django.http import Http404
from django.template import loader


# Create your views here.
def index(request):
    template = loader.get_template("home/top.htm")
    con = {

    }
    return HttpResponse(template.render(con, request))
