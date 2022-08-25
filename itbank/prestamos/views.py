from django.shortcuts import render

# Create your views here.
from .models import Prestamo

def pedido_prestamos(request):

    if request.method == 'POST':
        fecha = request.POST['fecha']
        monto = request.POST['monto']
        interes = request.POST['interes']
        cuotas = request.POST['cuotas']

        prestamo = Prestamo(fecha=fecha, monto=monto, interes=interes, cuotas=cuotas)
        prestamo.save()

    return render(request, "prestamos.html")


    