from django.shortcuts import render
from django.conf import settings

# Create your views here.

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .models import TStat14
from .models import TStat15
from django.urls import reverse
from .models import TStat16
from .models import TStat17
from django.core import serializers
from django.shortcuts import redirect

from .forms import SelectProvince_Months_Form

#def get_province_monthfrom_monthto(request):


def index(request):

    if request.method == "POST":
        form = SelectProvince_Months_Form(request.POST)
        if form.is_valid():
            request.session['provinces'] = request.POST['provinces']
            request.session['month_from'] = request.POST['month_from']
            request.session['month_to'] = request.POST['month_to']
            return redirect('result')
    else:
        form = SelectProvince_Months_Form()
        print("Nie Wszedł")

    return render(request, 'App/index.html', {'form': form})


def result(request):

    data_provinces = request.session.get('provinces')
    month_from = request.session.get('month_from')
    month_to = request.session.get('month_to')

    print(data_provinces)
    print(month_from)
    print(month_to)

    return render(request, 'App/result.html')
