from django.db import models

class Veiculo(models.Model):
    ano = models.IntegerField(null=True, blank=True, default=0)
    preco = models.DecimalField(max_digits=7, decimal_places=2,blank=True, null=True, default=0)
    cor = models.ForeignKey('Cor', on_delete=models.CASCADE)
    modelo = models.ForeignKey('Modelo', on_delete=models.CASCADE)
    acessorios = models.ManyToManyField('Acessorio')
    

    def _str_(self):
        return f'({self.id} {self.ano} {self.modelo})'