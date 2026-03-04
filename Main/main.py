



import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from pathlib import Path


today = datetime.now().strftime('%d_%m_%Y_%H-%M')
dir_path = Path(__file__).parent
dir_path.mkdir(parents=True, exist_ok=True)
#os.makedirs(dir_path, exist_ok=True)
data_file = Path(__file__).parent.parent / "Data Generation" / "ventes_janvier.csv"
print(data_file)