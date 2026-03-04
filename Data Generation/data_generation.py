


import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from pathlib import Path


today = datetime.now().strftime('%d_%m_%Y_%H-%M')
dir_path = Path(__file__).parent
os.makedirs(dir_path, exist_ok=True)
data_file = dir_path / "ventes_janvier.csv"



np.random.seed(42)

# Paramètres
n = 250
start_date = datetime(2026, 1, 1)

produits = ["Laptop", "Smartphone", "Tablette", "Casque", "Clavier", "Souris"]
regions = ["Dakar", "Thies", "Saint-Louis", "Kaolack", "Ziguinchor"]


# Génération données
data = {
    "Date": [start_date + timedelta(days=np.random.randint(0, 31)) for _ in range(n)],
    "Produit": np.random.choice(produits, n),
    "Region": np.random.choice(regions, n),
    "Quantité": np.random.randint(1, 20, n),
    "Prix_Unitaire": np.random.randint(50, 1500, n),
    "Coût_Unitaire": np.random.randint(30, 1200, n),
    "Heure_d'achat" : np.random.randint(0, 86400, n) #[str(timedelta(seconds=int(s))) for s in np.random.randint(0, 86400, n)]
}

df = pd.DataFrame(data)

# Sauvegarde CSV
df.to_csv(data_file, index=False)

print("Fichier ventes_janvier.csv généré avec succès.")
print(df.head())