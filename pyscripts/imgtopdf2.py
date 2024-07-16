import os
import img2pdf


newdir = input("Pone el path absoluto donde estan las imagenes: ")
dirname = r"C:/Users/Don/Documents/pyscripts/cv"
imgs = []

for fname in os.listdir(dirname):
    if (not fname.endswith(".png")):
        continue
    path = os.path.join(dirname, fname)
    if os.path.isdir(path):
        continue
    imgs.append(path)

if not imgs:
    print("No PNG files found in the directory.")
    exit()

with open("name2.pdf", "wb") as f:
    try:
        f.write(img2pdf.convert(imgs))
        print("PDF conversion successful.")
    except Exception as e:
        print("An error occurred during PDF conversion:", str(e))





























