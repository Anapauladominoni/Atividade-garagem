from django.db import models

class Cor(models.Model):
    descricao = models.CharField(max_length=40)

    def _str_(self):
        return self.nome