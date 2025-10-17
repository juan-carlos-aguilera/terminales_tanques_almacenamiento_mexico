import os
import matplotlib.pyplot as plt
import pyprojroot

root = pyprojroot.here()
FIGURES_PATH = os.path.join(root, "reports", "figures")

def save_figure(figure_name, subfolder='general', dpi=300, tight=True):
    
    folder_path = os.path.join(FIGURES_PATH, subfolder)
    os.makedirs(folder_path, exist_ok=True)

    path = os.path.join(folder_path, figure_name)
    plt.savefig(path, dpi=dpi, bbox_inches='tight' if tight else None)
    print(f'Figura guardada correctamente en: {path}')
