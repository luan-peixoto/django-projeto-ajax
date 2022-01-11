from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=70, db_index=True, unique=True)
    
    class Meta:
        db_table = 'categoria'

    def __str__(self):
        return self.nome