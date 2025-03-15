# Fixture species

Cette fixture permet de charger les données depuis le fichier xls recensant les types de bagues.
Ce fichier est disponible ici: https://crbpo.mnhn.fr/les-donnees/saisir-les-donnees/article/codes-especes-tailles-et-types-de-bagues

L'utilisation du script python permet de générer la fixture à partir du fichier au format CSV.

```sh
poetry run python gen_fixture_species.py
```