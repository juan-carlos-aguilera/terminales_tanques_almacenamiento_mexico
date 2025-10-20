# Análisis de Terminales de Almacenamiento y Tanques de México

La trayectoria del petróleo crudo comprende en gran medida desde el yacimiento, pasando por
la transformación en una refinería, hasta su almacenamiento y distribución.
Es por ello que el almacenamiento del petróleo crudo y sus derivados, es muy influyente en este
trayecto.

Este proyecto tiene como principal propósito indagar y visualizar la 'Capacidad Operativa' y 'Capacidad Diseño'
de las terminales de almacenamiento, así como conocer la infraestructura de cada una de estas.
Es así que se plantea la pregunta principal:
-- ¿Cuál es el aprovechamiento operativo nacional de las terminales de México?.
Además se consideran las siguientes preguntas adicionales:
-- ¿Qué región tiene el mejor desempeño de Capacidad Operativa?
-- ¿Todas las terminales de almacenamiento operan por debajo de su Capacidad de Diseño?
-- ¿Cómo es la infraestructura de dichas terminales?

Con esto se pretende resolver la interrogante si todas las terminales operan por debajo de su capacidad operativa.
Y si el desempeño operativo es el apropiado para poder satisfacer la demanda energética del país.

## Estructura del Proyecto

```sh
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
```

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
