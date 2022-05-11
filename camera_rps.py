from tkinter import font
import cv2
import random
import numpy as np
import time
from keras.models import load_model

def user_Choice():
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0) # Captures the video feed using the primary camera (denoted by 0) and stores it in a variable called 'cap'
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32) # Creates a 1x224x224x3 n-dimensional array using numpy and stores float32 type data in a variable called 'data'

    while True:
        get_prediction = ''
        # Reads 'cap' and splits the information to store 'ret' (tells us if the frame is available) as a boolean and the 'frame' as an image array vector captured using the default fps defined
        ret, frame = cap.read()
        font = cv2.FONT_HERSHEY_COMPLEX
        # Takes the frame and resizes it using cv2's interpolation method called 'INTER_AREA'
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        # Stores the resized frame as an array in the variable 'image_np'
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image # Stores data about the normalized image in the 0th index of the variable 'data'
        prediction = model.predict(data) # Predicts the probability of the data fitting in a certain class
        # Prints the class associated with each frame depending on the predicted value of each index
        if prediction[0][0] > 0.8:
            get_prediction = 'Rock'
            cv2.putText(frame, 'Rock', (50,50), font, 1, (255,255,255), 2, cv2.LINE_4)
            print('Rock')
        elif prediction[0][1] > 0.8:
            get_prediction = 'Paper'
            cv2.putText(frame, 'Paper', (50,50), font, 1, (255,255,255), 2, cv2.LINE_4)
            print('Paper')
        elif prediction[0][2] > 0.8:
            get_prediction = 'Scissors'
            cv2.putText(frame, 'Scissors', (50,50), font, 1, (255,255,255), 2, cv2.LINE_4)
            print('Scissors')
        else:
            get_prediction = 'Nothing'
            cv2.putText(frame, 'Nothing', (50,50), font, 1, (255,255,255), 2, cv2.LINE_4)
            print('Nothing')
        cv2.imshow('frame', frame) # Displays the video feed in a window labelled 'frame'
        # Press q to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

    print(get_prediction)

def computer_Choice():
    l1 = ['Rock', 'Paper', 'Scissors'] # List of different rps options
    get_computer_choice = random.choice(l1) # Randomized computer choice

def get_Winner():
    get_computer_choice = computer_Choice()
    get_user_choice = user_Choice()
    winner = ''
    # Conditions for the User to be the winner
    if (get_computer_choice == 'Rock' and get_user_choice == 'Paper') or (get_computer_choice == 'Paper' and get_user_choice == 'Scissors') or (get_computer_choice == 'Scissors' and get_user_choice == 'Rock'):
        winner = 'User'
        return winner
    # Conditions for the Computer to be the winner
    elif (get_computer_choice == 'Paper' and get_user_choice == 'Rock') or (get_computer_choice == 'Scissors' and get_user_choice == 'Paper') or (get_computer_choice == 'Rock' and get_user_choice == 'Scissors'):
        winner = 'Computer'
        return winner
    # Conditions for a draw
    else:
        winner = 'Draw'
        return winner

user_Choice()