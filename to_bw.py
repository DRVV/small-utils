import argparse
import numpy
from scipy import misc


def to_bw(img):
    '''convert RGB image to Black White image'''
    # read image as a numpy array
    data = misc.imread(img, mode='L')
    data[data < 128] = 0
    data[data >= 128] = 255
    return data


def main(img, file=None):
    # do something
    print(__doc__)
    import matplotlib.pyplot as plt
    bwimg = to_bw(img)
    plt.imshow(bwimg)
    plt.show()
    misc.imsave(file, bwimg)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('img', help='image file')
    parser.add_argument('save_file', help='save output to ...')
    args = parser.parse_args()

    main(args.img, file=args.save_file)