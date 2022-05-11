import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0) # Captures the video feed using the primary camera (denoted by 0) and stores it in a variable called 'cap'
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32) # Creates a 1x224x224x3 n-dimensional array using numpy and stores float32 type data in a variable called 'data'

while True: 
    # Reads 'cap' and splits the information to store 'ret' (tells us if the frame is available) as a boolean and the 'frame' as an image array vector captured using the default fps defined
    ret, frame = cap.read()
    # Takes the frame and resizes it using cv2's interpolation method called 'INTER_AREA'
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    # Stores the resized frame as an array in the variable 'image_np'
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image # Stores data about the normalized image in the 0th index of the variable 'data'
    prediction = model.predict(data) # Predicts the probability of the data fitting in a certain class
    cv2.imshow('frame', frame) # Displays the video feed in a window labelled 'frame'
    # Prints the class associated with each frame depending on the predicted value of each index
    print(prediction)
    if prediction[0][0] > 0.8:
        print("Rock")
    elif prediction[0][1] > 0.8:
        print("Paper")
    elif prediction[0][2] > 0.8:
        print("Scissors")
    elif prediction[0][3] > 0.8:
        print("Nothing")
    # Press q to close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()