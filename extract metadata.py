#Create a Python program to extract metadata
#(size, DPI, format) from an image file using Pillow.


from PIL import Image

img = Image.open("photo.png")

print("Image format:", img.format)
print("Image size:", img.size)

dpi_value = img.info.get("dpi")

if dpi_value:
    print("Image DPI:", dpi_value)
else:
    print("DPI information not available")
