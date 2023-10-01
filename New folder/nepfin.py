from roboflow import Roboflow
import easyocr
import cv2
image = cv2.imread('your_image.png')
rf = Roboflow(api_key="L2eNpC7z2VBt7deH0uw5")
project = rf.workspace().project("license-plate-recognition-rxg4e")
model = project.version(2).model

# infer on a local image
response = model.predict("your_image.png", confidence=40, overlap=30).json()
model.predict("your_image.png", confidence=40,
              overlap=30).save("prediction.jpg")
coords = response['predictions'][0]
width = coords['width']
height = coords['height']
x = int(coords['x']-width/2)
y = int(coords['y']-height/2)

cropped_image = image[y:y+height, x:x+width]

reader = easyocr.Reader(['en'])

# Define the path to the image you want to read
image_path = 'nep.png'

# Perform text recognition on the image
results = reader.readtext(cropped_image)

# Iterate through the recognized text and bounding boxes
for (bbox, text, prob) in results:
    # Extract the recognized text and confidence level
    recognized_text = text
    confidence = prob

    # Extract the bounding box coordinates
    (top_left, top_right, bottom_right, bottom_left) = bbox

    # Print the recognized text and confidence level
    print(f"Recognized Text: {recognized_text}")
    print(f"Confidence: {confidence:.2f}")

# Note: You can access other information in the 'results' variable, such as orientation and script.

