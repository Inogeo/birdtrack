from django.db import models

# Create your models here.
class Capture(models.Model):
    """Tracks all capture actions."""

    pays=models.CharField(

    )
    centre=models.CharField(

    )
    bague=models.CharField(
        max_length=10,
        blank=False,
        null=False,
        verbose="Numéro de Bague",
    )
    action=models.CharField(
        choices=
    )
    espece
    date
    heure
    bagueur
    dept
    localite
    insee
    lieudit
    theme
    sexe
    age
    ma
    lp
    pi
    es
    mue
    ad
    pc
    nf
    cs
    cond_repr
    circ_repr
    memo=models.TextField()