from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField('nome', max_length=100)
    email = models.EmailField('e-mail')

    class Meta:
        verbose_name_plural = 'pessoas'
        verbose_name = 'pessoa'

    def __str__(self):
        return self.nome