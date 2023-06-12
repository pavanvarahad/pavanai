from django.shortcuts import render
from .backend import addfun
def home(request):
    return render(request, "home.html")


def add(request):
    if request.method == "POST":
        a = request.POST['aval']
        b = request.POST['bval']
        sum = addfun(a,b)
        return render(request, "home.html", context={"result":sum})
