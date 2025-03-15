from django.db import models
from typing import ClassVar


class Species(models.Model):
    id_taxon = models.IntegerField(verbose_name="ID Taxon")
    code = models.CharField(max_length=10, verbose_name="Code")
    nom_vernaculaire = models.CharField(max_length=100, verbose_name="Nom Vernaculaire")
    nom_scientifique = models.CharField(max_length=100, verbose_name="Nom Scientifique")
    categorie = models.CharField(
        max_length=10, verbose_name="Catégorie", blank=True, null=True
    )
    id_ref = models.CharField(
        max_length=10, verbose_name="ID Référence", blank=True, null=True
    )
    recommandation = models.CharField(
        max_length=100, verbose_name="Recommandation", blank=True, null=True
    )
    position = models.CharField(
        max_length=10, verbose_name="Position", blank=True, null=True
    )
    alternative = models.CharField(
        max_length=100, verbose_name="Alternative", blank=True, null=True
    )
    date_mise_a_jour = models.DateField(verbose_name="Date de Mise à Jour")
    commentaire = models.TextField(verbose_name="Commentaire", blank=True, null=True)

    class Meta:
        verbose_name = "Espèce"
        verbose_name_plural = "Espèces"

    def __str__(self):
        return self.nom_vernaculaire


# class Capture(models.Model):
#     """Tracks all capture actions."""

#     pays = models.CharField()
#     centre = models.CharField()
#     bague = models.CharField(
#         max_length=10,
#         blank=False,
#         null=False,
#         verbose_name="Numéro de Bague",
#     )

#     ACTION_CHOICES: ClassVar[dict[str, str]] = {
#         "B": "Baguage",
#         "C": "Contrôle (d'un oiseau vivant déjà bagué)",
#         "R": "Reprise (d'un oiseau mort)",
#         "BREDOUILLE": "Pour signifier une session sans aucune capture",
#         "SANS": "Pour signifier une capture mais sans pose de bague",
#         "PERDUE": "Pour signifier une bague perdue",
#         "DETRUITE": "Pour signifier une bague détruite",
#     }
#     action = models.CharField(
#         max_length=10,
#         choices=ACTION_CHOICES,
#         blank=False,
#         null=False,
#         verbose_name="ACTION = Action de baguage",
#     )

#     # espece = models.CharField()
#     # date
#     # heure
#     # bagueur
#     # dept
#     # localite
#     # insee
#     # lieudit
#     # theme
#     # sexe
#     # age
#     # ma
#     # lp
#     # pi
#     # es
#     # mue
#     # ad
#     # pc
#     # nf
#     # cs
#     # cond_repr
#     # circ_repr
#     memo = models.TextField()
