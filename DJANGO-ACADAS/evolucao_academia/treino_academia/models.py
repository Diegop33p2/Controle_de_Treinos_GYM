from django.db import models

class Medidas(models.Model):
    nome = models.CharField(max_length=100)
    data_medida = models.DateField()
    peitoral = models.IntegerField()
    braco_esq = models.IntegerField()
    braco_dir = models.IntegerField()
    antebraco_esq = models.IntegerField()
    antebraco_dir = models.IntegerField()
    gluteos = models.IntegerField()
    coxa_esq = models.IntegerField()
    coxa_dir = models.IntegerField()
    abdomen = models.IntegerField()
    pantu_esq = models.IntegerField()
    pantu_dir = models.IntegerField()

    class Meta:
        app_label = 'treino_academia'

    def __str__(self):
        return self.nome

class Pernas(models.Model):
    data_treino = models.DateField()
    agachamneto = models.TextField()
    leg_press = models.TextField()
    extensora = models.TextField()
    rack = models.TextField()
    bulgaro = models.TextField()
    stiff = models.TextField()
    cadeira_flexora = models.TextField()
    mesa_flexora = models.TextField()
    ele_pelvica = models.TextField()
    aga_sumo = models.TextField()
    abdutora = models.TextField()
    adutora = models.TextField()
    panturilha = models.TextField()

    class Meta:
        app_label = 'treino_academia'
    
    def __str__(self):
        return f'{self.data_treino} - Treino de Pernas' 
    # def __str__(self):
    #     return self.data_treino

