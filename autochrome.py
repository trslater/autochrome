import sys
import PIL.Image
import numpy as np


def main():
    subject = np.array(PIL.Image.open(sys.argv[1]))
    
    plate = starched_plate(*subject.shape[:2])
    plate = exposed_plate(plate, subject)

    render(plate)


def starched_plate(height, width):
    # Array of each seed color, defines distribution
    starch = np.array(((255, 0, 0), (0, 255, 0), (0, 0, 255)), np.uint8)
    
    pop_size, _ = starch.shape
    num_each = height*width/pop_size
    rem = height*width % pop_size
    
    if rem:
        print("uh oh")
        return

    # Repeat each to the size of width*height
    starch = np.repeat(starch, num_each, 0)
    # Randomize
    np.random.shuffle(starch)
    
    # Reshape into shape of image
    return np.reshape(starch, (height, width, 3))


def exposed_plate(plate, subject):
    # Filter subject by starch
    return np.minimum(plate, subject)


def render(image):
    PIL.Image.fromarray(image, mode="RGB").show()


if __name__ == "__main__":
    main()
