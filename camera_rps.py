from tkinter import font
import cv2
import random
from cv2 import INTER_AREA
import numpy as np
import time
from keras.models import load_model

def Start():
    welcome_img = cv2.imread('/home/diasfrancisco/GitLocal/Computer-Vision-Rock-Paper-Scissors/images/rps_bkg.jpg')
    welcome_img_resized = cv2.resize(welcome_img, (640, 480), interpolation=INTER_AREA)

    while True:
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(welcome_img_resized, 'Rock, Paper, Scissors!', (120,150), font, 1, (0,0,0), 2, cv2.LINE_4)
        cv2.putText(welcome_img_resized, 'Press [s] to start', (150,250), font, 1, (0,0,0), 2, cv2.LINE_4)
        cv2.putText(welcome_img_resized, 'or [q] to quit', (180,290), font, 1, (0,0,0), 2, cv2.LINE_4)
        cv2.imshow('Rock, Paper, Scissors!', welcome_img_resized)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            Round()
            break

def Round():
    round_counter = 0

    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0) # Captures the video feed using the primary camera (denoted by 0) and stores it in a variable called 'cap'
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32) # Creates a 1 x 224 x 224 x 3 n-dimensional array using numpy and stores float32 type data in a variable called 'data'

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
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(frame, 'Round', (250, 30), font, 1, (255,0,0), 2, cv2.LINE_4)
        cv2.putText(frame, str(round_counter), (375, 30), font, 1, (255,0,0), 2, cv2.LINE_4)
        cv2.imshow('Rock, Paper, Scissors!', frame) # Displays the video feed in a window labelled 'Rock, Paper, Scissors!'
        # Press q to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()










def user_Choice():
    print('Ready')
    get_prediction = ''
    # Prints the class associated with each frame depending on the predicted value of each index
    if prediction[0][0] > 0.8:
        get_prediction = 'Rock'
        cv2.putText(frame, 'Rock', (50,50), font, 1, (255,255,255), 2, cv2.LINE_4)
    elif prediction[0][1] > 0.8:
        get_prediction = 'Paper'
        cv2.putText(frame, 'Paper', (50,50), font, 1, (255,255,255), 2, cv2.LINE_4)
    elif prediction[0][2] > 0.8:
        get_prediction = 'Scissors'
        cv2.putText(frame, 'Scissors', (50,50), font, 1, (255,255,255), 2, cv2.LINE_4)
    else:
        get_prediction = 'Nothing'
        cv2.putText(frame, 'Nothing', (50,50), font, 1, (255,255,255), 2, cv2.LINE_4)

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

Start()