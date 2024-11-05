from django.shortcuts import render
from django.views import View
from .utils import calculate_biological_age 


class MainPageView(View):
    
    def get(self, request):
        return render(request, "includes/index.html")

    def post(self, request):
        return print('working in progress')


class HomePageView(View):
    
    def get(self, request):
        return render(request, "includes/homePage.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        print(username, password)

        return render(request, "includes/homePage.html", {
            "username": username,
            "message": "Login tentativo eseguito"
        })



class CalcolatoreView(View):
    def get(self, request):
        return render(request, "includes/calcolatore.html")

    def post(self, request):

        data = {key: value for key, value in request.POST.items() if key != 'csrfmiddlewaretoken'}

        chronological_age = int(data.get('chronological_age'))
        obri_index = float(data.get('obri_index'))
        d_roms = float(data.get('d_roms'))
        aa_epa = float(data.get('aa_epa'))
        aa_dha = float(data.get('aa_dha'))
        homa_test = float(data.get('homa_test'))
        cardiovascular_risk = float(data.get('cardiovascular_risk'))
        osi = float(data.get('osi'))
        pat = float(data.get('pat'))
        
        glucose = float(data.get('glucose'))
        creatinine = float(data.get('creatinine'))
        ferritin = float(data.get('ferritin'))
        albumin = float(data.get('albumin'))
        protein = float(data.get('protein'))
        bilirubin = float(data.get('bilirubin'))
        uric_acid = float(data.get('uric_acid'))

        exams = [glucose, creatinine, ferritin, albumin, protein, bilirubin, uric_acid]


        # Calcola l'età biologica
        biological_age = calculate_biological_age(
                chronological_age,
                obri_index, d_roms,
                aa_epa, aa_dha,
                homa_test,
                cardiovascular_risk,
                osi,
                pat,
                exams
        )

        context = {
            "show_modal": True,
            "biological_age": biological_age,
            "data" : data
        }

        return render(request, "includes/calcolatore.html", context)


class RisultatiView(View):
    def get(self, request):
        return render(request, "includes/risultati.html")

    def post(self, request):

        return render(request, "includes/risultati.html")
