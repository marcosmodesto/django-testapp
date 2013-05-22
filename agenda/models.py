from django.db import models

class ItemAgenda(models.Model):
	titulo = models.CharField(max_length=100)
	data = models.DateField()
	hora = models.TimeField()
	descricao = models.TextField()
