from pypackageinstaller import install
install()

from PIL import Image
img = Image.open("examples/ProjectExample/testImage.png")
img.show()