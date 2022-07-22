from django.shortcuts import render
from django.views import View

# Create your views here.


# class Portfolio(View):
#     def get():
#         pass

#     def post():

def portfolioView(request):
    return render(request, "portfolio/index.html")
