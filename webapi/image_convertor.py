from PIL import Image

img = Image.open("bee.png")  # Replace with your PNG filename
img.save("favicon.ico", format="ICO", sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
