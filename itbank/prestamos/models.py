from django.db import models

# Create your models here. aca definimos los modelos de la base de datos, con solo definirlos al momento de realizar las migraciones django crea la base de datos y las tablas
class Prestamo(models.Model):
    fecha = models.TextField()
    monto = models.FloatField()
    interes = models.FloatField()
    cuotas = models.IntegerField()

    def __str__(self):
        return "Prestamo de %s a %s cuotas" % (self.monto, self.cuotas)