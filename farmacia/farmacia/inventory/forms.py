from django import forms
from .models import Farmacia

class FarmaciaForm(forms.ModelForm):
    class Meta:
        model = Farmacia
        fields = ('cliente', 'data_compra', 'produto', 'lote_produto', 'valor', 'pagamento')