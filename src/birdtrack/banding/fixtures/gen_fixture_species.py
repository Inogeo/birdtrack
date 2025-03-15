import csv
import yaml
from datetime import datetime
csv_file = 'fixture_species.csv'
yaml_file = 'fixture_species.yaml'
data = []
with open(csv_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        entry = {
            "model": "banding.Species",
            "pk": int(row["id_taxon"]),
            "fields": {
                "id_taxon": row["id_taxon"],
                "code": row["code"],
                "nom_vernaculaire": row["nom_vernaculaire"],
                "nom_scientifique": row["nom_scientifique"],
                "categorie": row["categorie"] if row["categorie"] else None,
                "id_ref": row["id_ref"],
                "recommandation": row["recommandation"],
                "position": row["position"],
                "alternative": row["alternative"] if row["alternative"] else None,
                "date_mise_a_jour": datetime.strptime(row["date_mise_a_jour"], "%d/%m/%Y").strftime('%Y-%m-%d'),
                "commentaire": row["commentaire"] if row["commentaire"] else None,
            }
        }
        data.append(entry)
with open(yaml_file, 'w') as outfile:
    yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True)