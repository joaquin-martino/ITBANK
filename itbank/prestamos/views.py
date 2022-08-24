from django.shortcuts import render

# Create your views here.

def pedido_prestamos(request):

    return render(request, "prestamos.html")