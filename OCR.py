#Given a folder containing 5-10 sample KYC images, use a
#for loop to run OCR on each file and store
#the results in a list.


from PIL import Image

img = Image.open("sample.png")

print("Image format:", img.format)
print("Image size:", img.size)

dpi_value = img.info.get("dpi")

if dpi_value:
    print("Image DPI:", dpi_value)
else:
    print("DPI info not found!!")
