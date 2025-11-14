from PIL import Image

# Abre el JPG
img = Image.open("fondo_ahorcado.jpg").convert("RGBA")

# Hace transparente el color blanco (por ejemplo)
datas = img.getdata()
nuevos_datos = []

for item in datas:
    # Si el pixel es blanco, lo hacemos transparente
    if item[0] > 240 and item[1] > 240 and item[2] > 240:
        nuevos_datos.append((255, 255, 255, 0))
    else:
        nuevos_datos.append(item)

img.putdata(nuevos_datos)

# Guarda como PNG con transparencia
img.save("imagen_transparente.png", "PNG")

