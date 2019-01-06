from django.shortcuts import render
from django.conf import settings

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import Perceptron



from sklearn.neighbors import KNeighborsClassifier


# Create your views here.

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .models import TStat14
from .models import TStat15
from .models import TStat16
from .models import TStat17
from django.urls import reverse

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


    data = [
        TStat14.objects.filter(id=data_provinces).values().get(),
        TStat15.objects.filter(id=data_provinces).values().get(),
        TStat16.objects.filter(id=data_provinces).values().get(),
        TStat17.objects.filter(id=data_provinces).values().get()
    ]

    monthbegin = getValuesFromRomeSigns(month_from)
    monthend = getValuesFromRomeSigns(month_to)
    if(monthbegin > monthend):
        monthbegin, monthend = monthend, monthbegin


    arrayLearnValues = []

    for month in range(monthbegin, (monthend + 1)):
        learnValues = []
        for x in data:
            key = getKey(month)
            res = x[key]
            learnValues.append(res)
        arrayLearnValues.append(learnValues)


    # print(res)
    # res = TStat14.objects.filter(id=data_provinces).values().get()
    # res[month_from] -------value

    iris = load_iris()

    X = iris.data
    X = arrayLearnValues

    y = iris.target

    print(y)

    # print(X.shape)
    # print(y.shape)

    knn = KNeighborsClassifier(n_neighbors=5)

    knn.fit(X, y)

    predictets = knn.predict(arrayLearnValues)

    # print(predictets)



    return render(request, 'App/index.html')

    # return render(request, 'App/result.html')


def getValuesFromRomeSigns(value):
    values = getValues()
    return values[value]

def getValues():
    return {
        'i': 1,
        'ii': 2,
        'iii': 3,
        'iv': 4,
        'v': 5,
        'vi': 6,
        'vii': 7,
        'viii': 8,
        'ix': 9,
        'x': 10,
        'xi': 11,
        'xii': 12,
    }

def getKey(value):

    for key, val in getValues().items():
        if value == val:
            return key




