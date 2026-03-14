from pymol import cmd
import glob
import os

# Путь к PDB-файлам
pdb_files = sorted(glob.glob("analysis/pdb_frames/frame_*.pdb"))

# Цвета атомов
atom_colors = {
    'C': 'gray',
    'H': 'white',
    'O': 'red',
    'P': 'orange',
    'N': 'blue',
    'S': 'yellow'
}

# Создаём папку для PNG
os.makedirs("png_frames2", exist_ok=True)

for i, pdb_file in enumerate(pdb_files):
    obj_name = f"frame_{i}"
    cmd.load(pdb_file, obj_name)
    cmd.remove(f"/{obj_name}///SOL")
    cmd.show("sticks", obj_name)
    
    # Красим атомы по элементу
    for atom_type, color in atom_colors.items():
        selection = f"elem {atom_type} and {obj_name}"
        cmd.color(color, selection)

    if i == 0:
        cmd.zoom(obj_name)
    
    png_file = f"png_frames2/frame_{i:04d}.png"
    cmd.png(png_file, width=600, height=600, ray=1)
    
    # Удаляем объекты, чтобы не накапливались
    cmd.delete(obj_name)


