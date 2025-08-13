from django.shortcuts import render
from .models import Experience

# Create your views here.
def index_page(request):
    experiences = Experience.objects.all().order_by('-id')

    return render(request, "base.html", {'experiences': experiences})


def about(request):
    return render(request, "about.html")
