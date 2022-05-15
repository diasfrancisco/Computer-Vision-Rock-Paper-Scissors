from tkinter import font
import cv2
import random
from cv2 import INTER_AREA
from cv2 import FONT_HERSHEY_COMPLEX
import numpy as np
import time
from keras.models import load_model

def Welcome():
    welcome_img = cv2.imread('/home/diasfrancisco/GitLocal/Computer-Vision-Rock-Paper-Scissors/images/rps_bkg.jpg') # Reads in the background image
    welcome_img_resized = cv2.resize(welcome_img, (640, 480), interpolation=INTER_AREA) # Resizes the image

    while True:
        font = cv2.FONT_HERSHEY_COMPLEX
        # Displays the welcome message and instructions
        cv2.putText(welcome_img_resized, 'Rock, Paper, Scissors!', (120,150), font, 1, (0,0,0), 2, cv2.LINE_4)
        cv2.putText(welcome_img_resized, 'Press [s] to start', (150,250), font, 1, (0,0,0), 2, cv2.LINE_4)
        cv2.putText(welcome_img_resized, 'or [q] to quit', (180,290), font, 1, (0,0,0), 2, cv2.LINE_4)
        cv2.imshow('Rock, Paper, Scissors!', welcome_img_resized)
        # Pressing 's' starts the game
        if cv2.waitKey(1) & 0xFF == ord('s'):
            Ready(round_counter)
            break
        # Pressing 'q' quits the game
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

round_counter = 0

def Round(round_counter):
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0) # Captures the video feed using the primary camera (denoted by 0) and stores it in a variable called 'cap'
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32) # Creates a 1 x 224 x 224 x 3 n-dimensional array using numpy and stores float32 type data

    start_time = time.time()
    time_elapsed = (time.time() - start_time)

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
        font = FONT_HERSHEY_COMPLEX
        cv2.putText(frame, 'Round ' + str(round_counter), (250, 30), font, 1, (255,0,0), 2, cv2.LINE_4)
        cv2.putText(frame, str(time_elapsed), (120,150), font, 1, (255,0,0), 2, cv2.LINE_4)
        
        # Prints the class associated with each frame depending on the predicted value of each index
        if prediction[0][0] > 0.8:
            cv2.putText(frame, 'You: Rock', (50, 50), font, 1, (255, 0, 0), 2, cv2.LINE_4)
        elif prediction[0][1] > 0.8:
            cv2.putText(frame, 'You: Paper', (50, 50), font, 1, (255, 0, 0), 2, cv2.LINE_4)
        elif prediction[0][2] > 0.8:
            cv2.putText(frame, 'You: Scissors', (50, 50), font, 1, (255, 0, 0), 2, cv2.LINE_4)
        elif prediction[0][3] > 0.8:
            cv2.putText(frame, 'You: Nothing', (50, 50), font, 1, (255, 0, 0), 2, cv2.LINE_4)
        else:
            cv2.putText(frame, 'Please readjust', (50, 50), font, 1, (255, 0, 0), 2, cv2.LINE_4)
        cv2.imshow('Rock, Paper, Scissors!', frame) # Displays the video feed in a window labelled 'frame'

        # Pressing 'q' quits the game
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()


def Ready(round_counter):
    round_counter += 1
    welcome_img = cv2.imread('/home/diasfrancisco/GitLocal/Computer-Vision-Rock-Paper-Scissors/images/rps_bkg.jpg') # Reads in the background image
    welcome_img_resized = cv2.resize(welcome_img, (640, 480), interpolation=INTER_AREA) # Resizes the image

    while True:
        # Prints the ready message
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(welcome_img_resized, 'Round ' + str(round_counter), (250, 30), font, 1, (255,0,0), 2, cv2.LINE_4)
        cv2.putText(welcome_img_resized, 'Are you ready?', (190, 60), font, 1, (255,0,0), 2, cv2.LINE_4)
        cv2.putText(welcome_img_resized, 'Press [y] for yes or [n] for no', (50, 90), font, 1, (255,0,0), 2, cv2.LINE_4)
        cv2.imshow('Rock, Paper, Scissors!', welcome_img_resized) # Displays the video feed in a window labelled 'Rock, Paper, Scissors!'

        # Press n to return to the welcome page
        if cv2.waitKey(1) & 0xFF == ord('n'):
            Welcome()
            break
        # Press y to start the round
        if cv2.waitKey(1) & 0xFF == ord('y'):
            break
        
    Round(round_counter)

Welcome()