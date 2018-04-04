from PIL import Image
import pytesseract
import cv2


def ocr_file(path, blockSize=115, C=50):
    try:
        original = cv2.imread(path)
        gray = cv2.cvtColor(original, cv2.COLOR_RGB2GRAY)
        # TODO: resize image if too large
    except Exception:
        raise FileNotFoundError(f'Path{path}:')
    threshed = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv2.THRESH_BINARY, blockSize, C)
    return pytesseract.image_to_string(
        Image.fromarray(cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)))
