from django.db import models

class Farmacia(models.Model):
    cliente = models.CharField(max_length=100)
    data_compra = models.DateField()
    produto = models.CharField(max_length=100)
    lote_produto = models.CharField(max_length=20)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    pagamento = models.CharField(max_length=50)

    def __str__(self):
        return self.cliente