from django import forms
from .models import Medidas
from .models import Pernas

class MedidasForm(forms.ModelForm):
    class Meta:
        model = Medidas
        fields = ('nome','data_medida','peitoral','braco_esq','braco_dir','antebraco_esq','antebraco_dir','gluteos','coxa_esq','coxa_dir','abdomen','pantu_esq','pantu_dir')

class PernasForm(forms.ModelForm):
    class Meta:
        model = Pernas
        fields = ('data_treino','agachamneto','leg_press','extensora','rack','bulgaro','stiff','cadeira_flexora','mesa_flexora','ele_pelvica','aga_sumo','abdutora','adutora','panturilha')


   