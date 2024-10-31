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
