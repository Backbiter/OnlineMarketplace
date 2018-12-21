from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import Http404
from bike.models import TwoWheeler
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm


# Create your views here.
def index(request):
    bike_all = TwoWheeler.objects.all()
    cont = {
        'bike_all': bike_all,
    }
    return render(request, 'home/homepage.html', cont)


class UserFormView(View):
    form_class = UserForm
    template_name = 'home/register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home:index')

        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
