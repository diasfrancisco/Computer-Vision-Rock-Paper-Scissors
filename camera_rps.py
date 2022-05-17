import cv2
import random
from cv2 import INTER_AREA
from cv2 import FONT_HERSHEY_COMPLEX
import numpy as np
import time
from keras.models import load_model

round_counter = 0

def Error(ret):
    error_img = cv2.imread('/home/diasfrancisco/GitLocal/Computer-Vision-Rock-Paper-Scissors/images/Error.jpg') # Reads in the error image
    error_img_resized = cv2.resize(error_img, (640, 480), interpolation=INTER_AREA) # Resizes the image

    # Display the error message depending on the error type
    while True:
        font = FONT_HERSHEY_COMPLEX
        if ret == False:
            cv2.putText(error_img_resized, 'Error!', (280,350), font, 1, (255,255,255), 2, cv2.LINE_4)
            cv2.putText(error_img_resized, 'Missing video feed', (170,380), font, 1, (255,255,255), 2, cv2.LINE_4)
            cv2.putText(error_img_resized, 'Press [t] to try again', (150,450), font, 1, (255,255,255), 2, cv2.LINE_4)
        cv2.imshow('Error!', error_img_resized)

        # Pressing 't' to try again
        if cv2.waitKey(1) & 0xFF == ord('t'):
            break
        
    if ret == False:
        Error(ret)
    else:
        pass

def win_Screen(user_wins, computer_wins):
    welcome_img = cv2.imread('/home/diasfrancisco/GitLocal/Computer-Vision-Rock-Paper-Scissors/images/rps_bkg.jpg') # Reads in the background image
    welcome_img_resized = cv2.resize(welcome_img, (640, 480), interpolation=INTER_AREA) # Resizes the image
    
    # Display the winner
    while True:
        font = FONT_HERSHEY_COMPLEX
        if user_wins == 3:
            cv2.putText(welcome_img_resized, 'The winner is User!', (150,150), font, 1, (0,0,0), 2, cv2.LINE_4)
        elif computer_wins == 3:
            cv2.putText(welcome_img_resized, 'The winner is Computer!', (105,150), font, 1, (0,0,0), 2, cv2.LINE_4)
        cv2.putText(welcome_img_resized, 'Press [r] to restart', (150,250), font, 1, (0,0,0), 2, cv2.LINE_4)
        cv2.putText(welcome_img_resized, 'or [q] to quit', (200,290), font, 1, (0,0,0), 2, cv2.LINE_4)
        cv2.imshow('Rock, Paper, Scissors!', welcome_img_resized)

        # Press 'r' to restart
        if cv2.waitKey(1) & 0xFF == ord('r'):
            Welcome()
        # Pressing 'q' quits the game
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Destroy all the windows
    cv2.destroyAllWindows()
    exit()

def Welcome():
    welcome_img = cv2.imread('/home/diasfrancisco/GitLocal/Computer-Vision-Rock-Paper-Scissors/images/rps_bkg.jpg') # Reads in the background image
    welcome_img_resized = cv2.resize(welcome_img, (640, 480), interpolation=INTER_AREA) # Resizes the image

    user_wins = 0
    computer_wins = 0

    while True:
        font = cv2.FONT_HERSHEY_COMPLEX
        # Displays the welcome message and instructions
        cv2.putText(welcome_img_resized, 'Rock, Paper, Scissors!', (120,150), font, 1, (0,0,0), 2, cv2.LINE_4)
        cv2.putText(welcome_img_resized, 'Press [s] to start', (150,250), font, 1, (0,0,0), 2, cv2.LINE_4)
        cv2.putText(welcome_img_resized, 'or [q] to quit', (180,290), font, 1, (0,0,0), 2, cv2.LINE_4)
        cv2.imshow('Rock, Paper, Scissors!', welcome_img_resized)
        # Pressing 's' starts the game
        if cv2.waitKey(1) & 0xFF == ord('s'):
            Ready(round_counter, user_wins, computer_wins)
            break
        # Pressing 'q' quits the game
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Destroy all the windows
    cv2.destroyAllWindows()
    exit()

def Round(round_counter, user_wins, computer_wins):
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0) # Captures the video feed using the primary camera (denoted by 0) and stores it in a variable called 'cap'
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32) # Creates a 1 x 224 x 224 x 3 n-dimensional array using numpy and stores float32 type data

    rps_List = ['Rock', 'Paper', 'Scissors']
    get_computer_choice = random.choice(rps_List) # Randomly chooses the computer's choice
    get_user_choice = ''

    winner = ''

    countdown = 5
    start_time = time.time()

    while True:
        # Reads 'cap' and splits the information to store 'ret' (tells us if the frame is available) as a boolean and the 'frame' as an image array vector captured using the default fps defined
        ret, frame = cap.read()
        if ret == False:
            Error(ret)
        else:
            pass
        # Takes the frame and resizes it using cv2's interpolation method called 'INTER_AREA'
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        # Stores the resized frame as an array in the variable 'image_np'
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image # Stores data about the normalized image in the 0th index of the variable 'data'
        prediction = model.predict(data) # Predicts the probability of the data fitting in a certain class
        font = FONT_HERSHEY_COMPLEX
        cv2.putText(frame, 'Round ' + str(round_counter), (250, 30), font, 1, (0,0,255), 2, cv2.LINE_4) # Display the round number
        time_elapsed = int(time.time() - start_time)
        # Display the countdown
        if countdown >= 0 and time_elapsed <= 5:
            cv2.putText(frame, (str(countdown - time_elapsed)), (300,400), font, 3, (0,255,0), 2, cv2.LINE_4)

        if time_elapsed > 5:
            cv2.putText(frame, 'Computer: ' + str(get_computer_choice), (360,70), font, 0.8, (255,0,0), 2, cv2.LINE_4) # Displays the computer's choice
            # Displays the class associated with each frame depending on the predicted value of each index
            if prediction[0][0] > 0.8:
                cv2.putText(frame, 'User: Rock', (20, 70), font, 0.8, (255, 0, 0), 2, cv2.LINE_4)
            elif prediction[0][1] > 0.8:
                cv2.putText(frame, 'User: Paper', (20, 70), font, 0.8, (255, 0, 0), 2, cv2.LINE_4)
            elif prediction[0][2] > 0.8:
                cv2.putText(frame, 'User: Scissors', (20, 70), font, 0.8, (255, 0, 0), 2, cv2.LINE_4)
            elif prediction[0][3] > 0.8:
                cv2.putText(frame, 'User: Nothing', (20, 70), font, 0.8, (255, 0, 0), 2, cv2.LINE_4)
            else:
                cv2.putText(frame, 'Please readjust', (20, 70), font, 0.8, (255, 0, 0), 2, cv2.LINE_4)

        if time_elapsed == 6:
            # Sets the user choice at 6 seconds after the countdown
            if prediction[0][0] > 0.8:
                get_user_choice = 'Rock'
            elif prediction[0][1] > 0.8:
                get_user_choice = 'Paper'
            elif prediction[0][2] > 0.8:
                get_user_choice = 'Scissors'
            elif prediction[0][3] > 0.8:
                get_user_choice = 'Nothing'
            else:
                get_user_choice == 'Nothing'
        
        if time_elapsed > 7 and time_elapsed < 12:
            # Conditions for the User to be the winner
            if (get_computer_choice == 'Rock' and get_user_choice == 'Paper') or (get_computer_choice == 'Paper' and get_user_choice == 'Scissors') or (get_computer_choice == 'Scissors' and get_user_choice == 'Rock'):
                cv2.putText(frame, 'The winner is User', (150,400), font, 1, (255,255,255), 2, cv2.LINE_4)
                winner = 'User'
            # Conditions for the Computer to be the winner
            elif (get_computer_choice == 'Paper' and get_user_choice == 'Rock') or (get_computer_choice == 'Scissors' and get_user_choice == 'Paper') or (get_computer_choice == 'Rock' and get_user_choice == 'Scissors'):
                cv2.putText(frame, 'The winner is Computer', (120,400), font, 1, (255,255,255), 2, cv2.LINE_4)
                winner = 'Computer'
            # Conditions for a draw
            else:
                cv2.putText(frame, 'It was a draw', (180,400), font, 1, (255,255,255), 2, cv2.LINE_4)

        cv2.putText(frame, 'User wins: ' + str(user_wins), (5, 475), font, 1, (0,255,255), 2, cv2.LINE_4) # Display user wins
        cv2.putText(frame, 'Computer wins: ' + str(computer_wins), (335, 475), font, 1, (0,255,255), 2, cv2.LINE_4) # Display computer wins
        cv2.imshow('Rock, Paper, Scissors!', frame) # Displays the video feed in a window labelled 'Rock, Paper, Scissors!'

        if time_elapsed == 12:
            break

        # Press q to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Add 1 to the win score depending on who wins, 0 if it is a draw
    if winner == 'User':
        user_wins += 1
    elif winner == 'Computer':
        computer_wins += 1
    else:
        pass

    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    Ready(round_counter, user_wins, computer_wins)

def Ready(round_counter, user_wins, computer_wins):
    # Go to the win screen if either player gets 3 wins
    if user_wins == 3 or computer_wins == 3:
        win_Screen(user_wins, computer_wins)
    else:
        pass

    round_counter += 1
    welcome_img = cv2.imread('/home/diasfrancisco/GitLocal/Computer-Vision-Rock-Paper-Scissors/images/rps_bkg.jpg') # Reads in the background image
    welcome_img_resized = cv2.resize(welcome_img, (640, 480), interpolation=INTER_AREA) # Resizes the image

    while True:
        # Prints the ready message
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(welcome_img_resized, 'Round ' + str(round_counter), (250, 160), font, 1, (255,0,0), 2, cv2.LINE_4)
        cv2.putText(welcome_img_resized, 'Are you ready?', (190, 240), font, 1, (255,0,0), 2, cv2.LINE_4)
        cv2.putText(welcome_img_resized, 'Press [y] for yes or [n] for no', (50, 280), font, 1, (255,0,0), 2, cv2.LINE_4)
        cv2.imshow('Rock, Paper, Scissors!', welcome_img_resized) # Displays the video feed in a window labelled 'Rock, Paper, Scissors!'

        # Press n to return to the welcome page
        if cv2.waitKey(1) & 0xFF == ord('n'):
            Welcome()
        # Press y to start the round
        if cv2.waitKey(1) & 0xFF == ord('y'):
            break

    Round(round_counter, user_wins, computer_wins)

Welcome()