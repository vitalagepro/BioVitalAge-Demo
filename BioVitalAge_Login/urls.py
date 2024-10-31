from django.urls import path
from django.urls import path, include



from . import views

urlpatterns = [
    path("", views.MainPageView.as_view(), name="main-page"),
    path('HomePage', views.HomePageView.as_view(), name='home_page'),

]