from django.db import models

 
class Status(models.TextChoices):
    OCUPADO = 'O'
    DISPONIVEL = 'D'


class Ramais(models.Model):
    setor = models.CharField(max_length=50)
    colaborador = models.CharField(max_length=50)
    ramal = models.IntegerField()
    whatsapp = models.CharField(max_length=50)
    status = models.CharField(max_length=1, choices=Status.choices, default=Status)
    time = models.DateField(auto_now=True)

    def __str__(self):
        return  f'{self.setor} - {self.colaborador} - {self.ramal} - {self.whatsapp} - {self.status}'