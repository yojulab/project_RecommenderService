from django.shortcuts import render

# Create your views here.
from django.shortcuts import render		# add
def home(request):
    return render(request, 'home/home.html')
