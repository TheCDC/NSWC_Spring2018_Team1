from PIL import Image
import pytesseract
import argparse
import cv2
import os

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help="path to input image to be OCR'd")
ap.add_argument(
    "-p",
    "--preprocess",
    type=str,
    default="thresh",
    help="type of preprocessing to be done")
ap.add_argument(
    '-v',
    '--video',
    default=False,
    help="Enable video mode. Pulls frames from default webcam. Overrides -i",
    action="store_true")
ap.add_argument(
    '-c',
    '--camera',
    default=-1,
    type=int,
    help='Id of webcam to use',
)
args = ap.parse_args()

# handle requiring at least one argument
if not (args.image or args.video):
    raise RuntimeError("Must use one of -i or -v")
rval = True
if args.video:
    vc = cv2.VideoCapture(args.camera)

    rval, frame = vc.read()

while rval:
    if args.video:
        rval, frame = vc.read()
    else:
        frame = cv2.imread(args.image)

    # load the example image and convert it to grayscale
    # image = cv2.imread(args.image)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # check to see if we should apply thresholding to preprocess the
    # image
    if args.preprocess == "thresh":
        gray = cv2.threshold(gray, 0, 255,
                             cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # make a check to see if median blurring should be done to remove
    # noise
    elif args.preprocess == "blur":
        gray = cv2.medianBlur(gray, 3)

    # write the grayscale image to disk as a temporary file so we can
    # apply OCR to it
    filename = "{}.tiff".format(os.getpid())
    cv2.imwrite(filename, gray)

    # load the image as a PIL/Pillow image, apply OCR, and then delete
    # the temporary file
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    print(text)

    # show the output images
    cv2.imshow("Image", frame)
    cv2.imshow("Output", gray)
    key = cv2.waitKey(1)
    # escape key
    if key == 27:
        break
    if not args.video:
        cv2.waitKey(0)
        break
