#!/usr/bin/env python3

from PIL import Image
import glob
import time


def read_pgm(pgmfile):
    # Verifies that the pgm image is of type P5
    filetype = pgmfile.readline()
    #print(filetype)
    assert filetype == b'P5\n'

    # Captures the dimensions of the image
    (width, height) = [int(i) for i in pgmfile.readline().split()]
    #print(width, height)

    # Verifies that the value of the grayscale is below 255
    maxval = int(pgmfile.readline())
    #print(maxval)
    assert maxval <= 255

    arraylength = height*width
    image = []
    for y in range(arraylength):
        image.append(ord(pgmfile.read(1)))

    #print(len(image))

    return image


def read_folder():
    i = 1
    dataset = []
    result = []
    
    for filename in glob.glob('img/*.pgm'):
        file = open(filename, 'rb')
        #print('\n', filename, i)
        dataset.append(read_pgm(file))
        i+=1
        

    return(dataset)

def main():
    start = time.time()
    dataset = read_folder()
    end = time.time()
    print(end - start)
    result = []

    


if __name__ == '__main__':
    main()  
