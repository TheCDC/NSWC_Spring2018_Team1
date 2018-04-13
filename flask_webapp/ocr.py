from PIL import Image
import pytesseract
import cv2
import re

serial_pattern = re.compile(r'[A-Z]{3}[0-9]{2}[A-Z]{1}[0-9]{3}-[0-9]{3}')


def limit_image_size(image, limit=800):
    """Shrink an image to prevent OCR from taking forever."""
    while any(d > limit for d in image.shape):
        image = cv2.resize(image, (0, 0), fx=0.8, fy=0.8)
    return image


def ocr_file(path, blockSize=115, C=50):
    """Get the OCR string from an image file."""
    try:
        original = cv2.imread(path)
        gray = cv2.cvtColor(original, cv2.COLOR_RGB2GRAY)
        # TODO: resize image if too large
    except Exception:
        raise FileNotFoundError(f'Path{path}:')
    threshed = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv2.THRESH_BINARY, blockSize, C)
    return pytesseract.image_to_string(
        Image.fromarray(cv2.cvtColor(threshed, cv2.COLOR_GRAY2RGB)))


def filter_serial(s):
    """Find the serial number from a string."""
    # return s
    found = serial_pattern.search(s)
    print(found)
    if found is not None:
        return found.group(0)
    return found
