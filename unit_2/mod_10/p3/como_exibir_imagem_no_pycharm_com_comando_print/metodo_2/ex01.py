
# Mostrar uma imagem

"""Necessário instalação pelo pip:
   $ pip install matplotlib
"""

# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg

from matplotlib import pyplot as plt
from matplotlib import image as mpimg

def output_image(name):

    img=mpimg.imread(name)
    imgplot = plt.imshow(img)
    plt.show()

output_image('test.png')