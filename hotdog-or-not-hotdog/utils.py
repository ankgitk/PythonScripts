# utility function used to solve
# Lab assignment: indoor image classification

from glob import glob
from scipy.misc import imread, imresize
#from imageio import imread
import matplotlib.pyplot as plt


def image_to_rgb(image):
    '''parse image to rgb'''

    # images config
    COLORS = ('r','g','b')
    COLOR_MIN_VALUE = 0
    COLOR_MAX_VALUE = 255
    COLOR_NUM_VALUES = COLOR_MAX_VALUE - COLOR_MIN_VALUE + 1

    # Tolerance for white and black
    tol = 100
    white_end = tol - COLOR_MIN_VALUE
    black_start = COLOR_MAX_VALUE - tol

    # Copy image
    image2 = image.copy()

    # Set black pixels to pure red
    black_pixels = (image[:, :, 0] <= white_end) &\
                   (image[:, :, 1] <= white_end) &\
                   (image[:, :, 2] <= white_end)
    image2[black_pixels] = [COLOR_MAX_VALUE, COLOR_MIN_VALUE, COLOR_MIN_VALUE] # [255,0,0]

    # Set white pixels to pure green
    white_pixels = (image[:, :, 0] >= black_start) &\
                   (image[:, :, 1] >= black_start) &\
                   (image[:, :, 2] >= black_start)
    image2[white_pixels] = [COLOR_MIN_VALUE, COLOR_MAX_VALUE, COLOR_MIN_VALUE] # [0,255,0]

    # Set all the rest to pure blue
    image2[~(black_pixels | white_pixels)] = [COLOR_MIN_VALUE, COLOR_MIN_VALUE, COLOR_MAX_VALUE] # [0,0,255]
    
    return image2

    
def read_images_from_path(path, height, width):
    '''read images from path and return images array'''
    print('Getting images from path: {}...'.format(path))
    
    images_in_path = glob(path + '/*.*')

    # read image and resize images
    images = [imresize(arr=imread(image_path), size=[height, width])
              for image_path in images_in_path]
    
    return images


def plot_loss_and_accuracy(model_history):
    plt.figure(figsize=(18,6))

    # Loss Curves
    plt.subplot(1,2,1)
    plt.plot(model_history.history['loss'], linewidth=3.0, linestyle='dotted')
    plt.plot(model_history.history['val_loss'], linewidth=3.0)
    plt.legend(['Training loss', 'Validation Loss'], fontsize=18)
    plt.xlabel('Epochs', fontsize=16)
    plt.ylabel('Loss', fontsize=16)
    plt.title('Loss Curves', fontsize=16)

    # Accuracy Curves
    plt.subplot(1,2,2)
    plt.plot(model_history.history['acc'], linewidth=3.0, linestyle='dotted')
    plt.plot(model_history.history['val_acc'], linewidth=3.0)
    plt.legend(['Training Accuracy', 'Validation Accuracy'], fontsize=18)
    plt.xlabel('Epochs', fontsize=16)
    plt.ylabel('Accuracy', fontsize=16)
    plt.title('Accuracy Curves', fontsize=16)

    plt.show()
    
    