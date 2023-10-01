
from roboflow import Roboflow
import easyocr
import cv2
import json
from datetime import datetime


image = cv2.imread('nep.png')
rf = Roboflow(api_key="008xZ6NU2AHcTyWejENj")
project = rf.workspace().project("license-plate-recognition-rxg4e")
model = project.version(2).model


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


image_path = 'nep.png'


results = reader.readtext(image_path)


plate_data = {}

for (bbox, text, prob) in results:
    recognized_text = text
    confidence = prob

    # Extract the 3rd and 4th recognized texts for plate number
    if len(plate_data) < 5:
        plate_data[len(plate_data) + 1] = recognized_text

    (top_left, top_right, bottom_right, bottom_left) = bbox



    print(f"Recognized Text: {recognized_text}")
    print(f"Confidence: {confidence:.2f}")

# print(plate_data)

# Check if both parts of the plate number are found
if len(plate_data) >= 2:
    # Concatenate the recognized texts to form the plate number
    plate_number = plate_data[3]+ ' ' + plate_data[4]
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   
    

    # Create a JSON object with the plate number
    plate_json = {
        "plate_number": plate_number,
        "current_datetime": current_datetime
    }

    # Save the plate number to "fin.json"
    with open("fin.json", "w") as f:
        json.dump(plate_json, f, indent=4)






# from roboflow import Roboflow
# import easyocr
# import cv2
# import json

# # Load the image
# image = cv2.imread('nep.png')

# # Initialize Roboflow
# rf = Roboflow(api_key="008xZ6NU2AHcTyWejENj")  # Replace with your actual API key
# project = rf.workspace().project("license-plate-recognition-rxg4e")
# model = project.version(2).model

# # Make a prediction
# response = model.predict("your_image.png", confidence=40, overlap=30).json()
# model.predict("your_image.png", confidence=40, overlap=30).save("prediction.jpg")
# coords = response['predictions'][0]
# width = coords['width']
# height = coords['height']
# x = int(coords['x'] - width / 2)
# y = int(coords['y'] - height / 2)

# # Crop the image
# cropped_image = image[y:y + height, x:x + width]

# # Initialize EasyOCR reader
# reader = easyocr.Reader(['en'])

# # Read text from the cropped image
# results = reader.readtext(cropped_image)

# # Initialize a dictionary to store the plate number
# plate_data = {}

# for (bbox, text, prob) in results:
#     recognized_text = text
#     confidence = prob

#     # Extract the 3rd and 4th recognized texts for plate number
#     if len(plate_data) < 2:
#         plate_data[len(plate_data) + 1] = recognized_text

#     (top_left, top_right, bottom_right, bottom_left) = bbox

#     print(f"Recognized Text: {recognized_text}")
#     print(f"Confidence: {confidence:.2f}")

# # Check if both parts of the plate number are found
# if len(plate_data) == 2:
#     # Concatenate the recognized texts to form the plate number
#     plate_number = plate_data[1] + plate_data[2]

#     # Create a JSON object with the plate number
#     plate_json = {
#         "plate_number": plate_number
#     }

#     # Save the plate number to "fuk.json"
#     with open("fuk.json", "w") as f:
#         json.dump(plate_json, f, indent=4)








# # from roboflow import Roboflow
# # import easyocr
# # import cv2
# # image = cv2.imread('nep.png')
# # rf = Roboflow(api_key="008xZ6NU2AHcTyWejENj")
# # project = rf.workspace().project("license-plate-recognition-rxg4e")
# # model = project.version(2).model


# # response = model.predict("your_image.png", confidence=40, overlap=30).json()
# # model.predict("your_image.png", confidence=40,
# #               overlap=30).save("prediction.jpg")
# # coords = response['predictions'][0]
# # width = coords['width']
# # height = coords['height']
# # x = int(coords['x']-width/2)
# # y = int(coords['y']-height/2)

# # cropped_image = image[y:y+height, x:x+width]

# # reader = easyocr.Reader(['en'])


# # image_path = 'nep.png'


# # results = reader.readtext(image_path)


# plate_data = {}

# for (bbox, text, prob) in results:
#     recognized_text = text
#     confidence = prob

#     # Extract the 3rd and 4th recognized texts for plate number
#     if len(plate_data) < 2:
#         plate_data[len(plate_data) + 1] = recognized_text

#     (top_left, top_right, bottom_right, bottom_left) = bbox





# # for (bbox, text, prob) in results:
# #     recognized_text = text
# #     confidence = prob

 
# #     (top_left, top_right, bottom_right, bottom_left) = bbox

# #     print(f"Recognized Text: {recognized_text}")
# #     print(f"Confidence: {confidence:.2f}")

