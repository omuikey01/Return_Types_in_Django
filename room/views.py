from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import JsonResponse
# Create your views here.

def homepage(request):
    return render(request, "index.html")

    # return HttpResponse("Successfully Registered")
    # return render(request, "index.html")
    # return render(request, "index.html")
    # return render(request, "about.html")
    # return render(request, "service.html")

def redirectpage(request):
    return redirect("https://www.facebook.com/")


def aboutpage(request):
    return JsonResponse({"Name" : "Uikey", "age" : 10, "City" : "Bhopal", "Auth1" : True, "Auth2" : False })