from rembg import remove
from PIL import Image

input_path = 'ImagesBefore/mohamed.png'  # Chemin vers l'image d'entrée.
output_path = 'ImagesAfter/mohamed_nobg.png'  # Chemin complet de l'image de sortie, incluant le dossier, le nom du fichier et l'extension.

input = Image.open(input_path)
output = remove(input)
output.save(output_path)