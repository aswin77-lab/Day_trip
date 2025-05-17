from django.shortcuts import render

# Create your views here.
def guid_home(request):
    return render(request,"guid_index.html")