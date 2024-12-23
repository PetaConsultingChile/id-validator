import io
from google.cloud import vision
import os
import re

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="accounts/platinum-voice-429518-f2-2d19dd8eb7f3.json"

def ocr(image_path):
    client= vision.ImageAnnotatorClient()

    with io.open(image_path, "rb") as image_file:
        content= image_file.read()

    image = vision.Image(content = content)
    response= client.text_detection(image = image)
    texts= response.text_annotations
    detected_text= texts[0].description.lower()

    has_foreign= "extrenjero" in detected_text

    has_chileno= "chileno" in detected_text

    has_chilena= "chilena" in detected_text

    if has_foreign and (has_chilena or has_chileno):
        return True
    else:
        return False
    


    

