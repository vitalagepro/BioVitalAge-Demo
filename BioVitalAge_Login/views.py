from django.shortcuts import render
from django.views import View


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

        print(request.POST)
        #Qui vanno i calcoli per calcolare l'età biologica e salvarli all'interno del database 

        return render(request, "includes/calcolatore.html")


class RisultatiView(View):
    def get(self, request):
        return render(request, "includes/risultati.html")

    def post(self, request):

        return render(request, "includes/risultati.html")
