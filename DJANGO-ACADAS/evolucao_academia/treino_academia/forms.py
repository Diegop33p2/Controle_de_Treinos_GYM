from django import forms
from .models import Medidas

class MedidasForm(forms.ModelForm):
    class Meta:
        model = Medidas
        fields = ('nome','data_medida','peitoral','braco_esq','braco_dir','antebraco_esq','antebraco_dir','gluteos','coxa_esq','coxa_dir','abdomen','pantu_esq','pantu_dir')

