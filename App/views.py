import numpy as np
import random
from django.shortcuts import render
from .models import TStat14
from .models import TStat15
from .models import TStat16
from .models import TStat17
from django.shortcuts import redirect
from .forms import SelectProvince_Months_Form


def index(request):

    if request.method == "POST":  # jeżeli formularz został wypełniony
        form = SelectProvince_Months_Form(request.POST)
        if form.is_valid():  # jeżeli formularz jest poprawny
            #  zapisz dane z formularza do sesji
            request.session['provinces'] = request.POST['provinces']
            request.session['month_from'] = request.POST['month_from']
            request.session['month_to'] = request.POST['month_to']
            return redirect('result') # przejdź do widoku result
    else:  # jeżeli formularz nie został wypełniony
        form = SelectProvince_Months_Form()   # utwórz nową instancję formularza
    return render(request, 'App/index.html', {'form': form}) # wyrenderuj stronę z wzorca index.html


def sigmoid(x):
    # sigmoid to funkcja aktywująca, którą wykorzystywana jest w sieciach
    # neuronowych, i z jej pomocą wyznaczamy neurony sigmoidalne
    return 1/(1+np.exp(-x))


def sigmoid_p(x):  # sigmoid prime - pochodna funkcji sigmoid
    return sigmoid(x) * (1-sigmoid(x))


def train(data):
    # zainicjowanie wag dla wartości pierwszej, drugiej, trzeciej, oraz
    w1 = random.uniform(0.25, 0.35)
    w2 = random.uniform(0.35, 0.45)
    w3 = random.uniform(0.45, 0.55)
    b = random.uniform(0.35, 0.45)

    iterations = 10000  # ilość iteracji
    learning_rate = 0.1
    costs = []  # keep costs during training, see if they go down

    for i in range(iterations):  # wchodzimy do pętli tyle razy, ile ustawiliśmy iteracjii
        # get a random point
        ri = np.random.randint(len(data))  # losowy index od 0 do ilości elementów w tablicy data
        point = data[ri]

        z = point[0] * w1 + point[1] * w2 + point[2] * w3 + b  # wartość predykcji na podstawie wag wraz z
        # danymi dla poszczególnych lat i parametru b - "bias"
        pred = sigmoid(z)  # networks prediction

        target = point[3]  # czwarta wartość statystyczna

        # koszt aktualnej wartości predykcji
        cost = np.square(pred - target)  # np.square to funkcja potęgująca

        # print the cost over all data points every 1k iters
        if i % 100 == 0:
            c = 0
            for j in range(len(data)):
                p = data[j]
                p_pred = sigmoid(w1 * p[0] + w2 * p[1] + w3 * p[2] + b)
                c += np.square(p_pred - p[3])
            costs.append(c)

        dcost_dpred = 2 * (pred - target)  # pochodna z kosztu predykcji
        dpred_dz = sigmoid_p(z)  # pochodna z wartości predykcji

        dz_dw1 = point[0]  # pierwsza losowa wartość z wysolowanej wcześniej tabeli
        dz_dw2 = point[1]  # druga losowa wartość z wysolowanej wcześniej tabeli
        dz_dw3 = point[2]  # trzecia losowa wartość z wysolowanej wcześniej tabeli
        # (są to dokładnie trzy wartości dla jakiegoś miesiąca)
        dz_db = 1  # ilość współczynnika "bias", czyli b, w naszym wzorze jest tylko jeden

        dcost_dz = dcost_dpred * dpred_dz

        dcost_dw1 = dcost_dz * dz_dw1
        dcost_dw2 = dcost_dz * dz_dw2
        dcost_dw3 = dcost_dz * dz_dw3
        dcost_db = dcost_dz * dz_db

        w1 = w1 - learning_rate * dcost_dw1
        w2 = w2 - learning_rate * dcost_dw2
        w3 = w3 - learning_rate * dcost_dw3
        b = b - learning_rate * dcost_db

    return costs, w1, w2, w3, b


def result(request):

    data_provinces = request.session.get('provinces')
    month_from = request.session.get('month_from')
    month_to = request.session.get('month_to')

    monthbegin = getValuesFromRomeSigns(month_from)
    monthend = getValuesFromRomeSigns(month_to)

    if(monthbegin > monthend):
        monthbegin, monthend = monthend, monthbegin

    data = [
        TStat14.objects.filter(id=data_provinces).values().get(),
        TStat15.objects.filter(id=data_provinces).values().get(),
        TStat16.objects.filter(id=data_provinces).values().get(),
        TStat17.objects.filter(id=data_provinces).values().get()
    ]

    arrayLearnValues = []

    for month in range(monthbegin, (monthend + 1)):
        learnValues = []
        for x in data:
            key = getKey(month)
            res = x[key]
            learnValues.append(res)
        arrayLearnValues.append(learnValues)
        print(arrayLearnValues)

    costs, w1, w2, w3, b = train(arrayLearnValues)

    data_for_charts = []

    #fig = plt.plot(costs)
    for value in arrayLearnValues:
        data_to_pred_from = value[0:3]
        predicted_value = abs(w1 * data_to_pred_from[0] + w2 * data_to_pred_from[1] + w3 * data_to_pred_from[2] + b)
        print("Statistic value  "
              "2014:" + str(value[0]) + "\n" +
              "2015: " + str(value[1]) + "\n" +
              "2016: " + str(value[2]) + "\n" +
              "2017: " + str(value[3]) + "\n" +
              "Predicted value for 2017: " +
              str(predicted_value))
         data_for_charts.append(value[0], value[1], value[2], value[3], predicted_value)






    return render(request, 'App/result.html')

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