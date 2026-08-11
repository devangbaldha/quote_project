from django.shortcuts import render
from .models import Quote


def home(request):
    quote = Quote.objects.filter(is_current=True).first()

    return render(request,"home.html",{"quote": quote})