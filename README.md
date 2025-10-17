# Análisis de Terminales de Almacenamiento y Tanques de México

Este proyecto tiene como principal propósito indagar y visualizar la 'Capacidad Operativa' y 'Capacidad Diseño'
de las terminales de almacenamiento. Además de contestar la pregunta principal ¿Cuál es el aprovechamiento operativo
nacional de las terminales de México?

## Estructura del Proyecto

├── data
│ ├── raw/ # Datos originales sin procesar
│ ├── processed/ # Datos limpios listos para análisis
│
├── notebooks
│ ├── 01_clean_data_terminales.ipynb
│ ├── 02_clean_data_tanques_terminales.ipynb
│ ├── 03_eda_univariate_analysis_terminales.ipynb
│ ├── 04_eda_univariate_analysis_tanques_terminales.ipynb
│ └── 05_univariate_analysis_terminales_gaslp.ipynb
│ └── 06_bivariable_analysis_terminales.ipynb
│ └── 07_bivariable_analysis_tanques_terminales.ipynb
│ └── 08_machine_learning_terminales.ipynb
│ └── 09_conclusiones_terminales.ipynb
│
├── scripts/
│ ├── init.py
│ ├── config.py # Configuración global del entorno
│ ├── data_loader.py # Función para leer CSV/Excel
│ ├── plotting_utils.py # Función para guardar figuras automáticamente
│ ├── setup_environment.py # Importación automática de librerías
│
├── reports/
│ ├── figures/ # Carpeta con las visualizaciones generadas
│ └── README_REPORT.md # Informe detallada sobre resultados encontrados
│
├── docs/
│
├── requirements.txt # Dependencias y versiones necesarias
├── .gitignore # Archivos/carpetas a excluir del control de versiones
└── README.md

## Versión de Python

python==3.12.3

## Instalación y uso

### 1. Clonar el repositorio

```sh
git clone
```

### 2. Crear un ambiente virtual y activarlo

```sh
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```sh
pip install --upgrade pip
pip3 install -r requirements.txt
```

### 4. Ejecutar los notebooks
