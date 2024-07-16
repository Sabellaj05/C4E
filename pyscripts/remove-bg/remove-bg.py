# Importing
from rembg import remove 
from PIL import Image
import os

img_path = r'C:/Users/manum/Documents/pyscripts/remove-bg/imgs'
output_path = r'C:/Users/manum/Documents/pyscripts/remove-bg/out_img'

# Ver imagenes de la carpeta
path_content = os.listdir(img_path)

# Crear las opciones
options = {str(n): item for n, item in enumerate(path_content)}

# Elegir la imagen 
print("Opciones: \n")
print(options)
img_index = input("Elegi la imagen a procesar") 

# Guardar la imagen elegida
img_elegida = options[img_index]

#absolute path para ambos
path_img = os.path.join(img_path, img_elegida)
out_img = os.path.join(output_path, img_elegida)
#print(path_img)
#print(out_img)

# La abrimos
img_a_procesar = Image.open(path_img)
# La procesamos
outt = remove(img_a_procesar)
# La guardamos
outt.save(out_img)




