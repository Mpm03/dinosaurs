from django.db import models


class Dinosaur(models.Model):
    class Meta:
        verbose_name_plural = "Dinossauros"
        verbose_name = "Dinossauro"

    name = models.CharField(max_length=30, verbose_name="Nome")
    image = models.ImageField(upload_to='uploads', verbose_name="Imagem")
