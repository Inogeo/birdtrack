# BirdMark

Ce projet vise à proposer un outil de saisie web pour les bagueurs du CRBPO afin de faciliter la saisie et la consolidation des données.

# Prérequis

Ce projet nécéssite l'installation préalable des dépendances ci-dessous:
1. [Poetry](https://python-poetry.org/docs/)
2. [git](https://git-scm.com/book/fr/v2/D%C3%A9marrage-rapide-Installation-de-Git)

# Développement

Pour démarrer le projet en développement, utiliser les commandes ci-dessous:

```sh
## Cloner le repo
git clone https://github.com/Inogeo/birdtrack.git
cd birdtrack

## Installer les dépendances
poetry install

## Initialiser la base de données
poetry run python ./src/manage.py migrate

## Lancer le serveur de développement
poetry run python ./src/manage.py runserver
```