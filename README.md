# README

## Quickstart

``` 
pip install openrouteservice
``` 

Modifier le script `findinghome.py` pour indiquer le département, la lattitude et la longitude du lieu de travail, la clé d'api openrouteservice (https://openrouteservice.org/).

``` 
python ./findinghome.py
```

Le script affiche le résultat et l'enregistre également dans un fichier csv (towns.csv) avec les champs suivant : nom de ville, code postal, temps de voyage en secondes.