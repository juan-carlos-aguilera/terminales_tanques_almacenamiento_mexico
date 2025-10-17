# Raíz del proyecto
root = pyprojroot.here()

# Agregar raíz al sys.path
if str(root) not in sys.path:
    sys.path.append(str(root))

# Librerías principales
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Rutas y entorno
import sys
import pyprojroot
from pathlib import Path
from scipy.stats import normaltest, norm

# Machine Learning
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Configuración visual y rutas
from scripts.config import *

# Mostrar números con 2 decimales
pd.set_option("display.float_format", "{:,.2f}".format)

print('Librerías y entorno configurado correctamente')

