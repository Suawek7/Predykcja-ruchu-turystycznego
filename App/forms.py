from django import forms

class SelectProvince_Months_Form(forms.Form):

    provinces_data = (('0', 'Wszystkie razem'), ('1', 'Dolnośląskie'), ('2', 'Kujawsko-pomorskie'), ('3', 'Lubelskie'), ('4', 'Lubuskie'), ('5', 'Łódzkie'), ('6', 'Małopolskie'), ('7', 'Mazowieckie'), ('8', 'Opolskie'), ('9', 'Podkarpackie'), ('10', 'Podlaskie'), ('11', 'Pomorskie'), ('12', 'Śląskie'), ('13', 'Świętokrzyskie'), ('14', 'Warmińsko-mazurskie'), ('15', 'Wielkopolskie'), ('16', 'Zachodniopomorskie'))
    provinces = forms.ChoiceField(choices=provinces_data)

    months = (('i', 'Styczeń'), ('ii', 'Luty'), ('iii', 'Marzec'), ('iv', 'Kwiecień'), ('v', 'Maj'), ('vi', 'Czerwiec'), ('vii', 'Lipiec'), ('viii', 'Sierpień'), ('ix', 'Wrzesień'), ('x', 'Październik'), ('xi', 'Listopad'), ('xii', 'Grudzień'))

    month_from = forms.ChoiceField(choices=months)
    month_from.label = "Od"
    month_to = forms.ChoiceField(choices=months)
