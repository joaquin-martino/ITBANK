from django.shortcuts import render

# Create your views here.
def home(request):
    if request.user.username:
        return render(request,"home/index.html", {'name':request.user.username})
    else:
        return render(request,"home/index.html")
