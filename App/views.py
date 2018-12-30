from django.shortcuts import render
from django.conf import settings

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import TStat14
from .models import TStat15
from .models import TStat16
from .models import TStat17
from .forms import SelectProvincesForm
from django.core import serializers


def index(request):
    data = TStat14.objects.all()
    datanameofcolumns = TStat14._meta.get_fields()

    return render(request, 'App/index.html', {'data': data})


def result(request, id, month_from, month_to):
    template = loader.get_template('App/result.html')
    context = {}
    return HttpResponse(template.render(context, request))
