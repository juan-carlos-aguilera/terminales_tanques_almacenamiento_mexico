import matplotlib.pyplot as plt
import seaborn as sns
import pyprojroot
from pathlib import Path

# Raíz del proyecto
root = pyprojroot.here()

# Estilo visual
sns.set_style('whitegrid')
sns.set_context('notebook')

# Parámetros de visualización
plt.rcParams['figure.figsize'] = (11, 9.4)
plt.rcParams['axes.titlesize'] = 14

# Rutas principales
DATA_PATH = root / "data"
REPORTS_PATH = root / "reports"
FIGURES_PATH = REPORTS_PATH / "figures"

# Crear carpetas si no existen
for path in [FIGURES_PATH, REPORTS_PATH]:
    path.mkdir(parents=True, exist_ok=True)