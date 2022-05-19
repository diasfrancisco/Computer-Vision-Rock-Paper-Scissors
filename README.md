# **Computer-Vision-Rock-Paper-Scissors**

## **Milestone 1: Create the model**
---

The model used for the Computer-Vision-Rock-Paper-Scissors project was created using Teachable-Machine. The model was provided with image data from 4 classes. The classes were Rock, Paper, Scissors and Nothing. The image data was gathered using a webcam, with Teachable-Machine extracting the data frame by frame. After the data gathering phase the model was trained on a subset of the data and ready for download.

Prior to download the model was converted to a keras .h5 model in the cloud. After this conversion the model and labels file were downloaded and pushed to GitHub under the Computer-Vision-Rock-Paper-Scissors repository (public)

## **Milestone 2: Install the dependencies**
---

The current model will be run in a new virtual environment (called 'rps') on my local machine, with multiple iterations looking to add features such as user & computer inputs, win screens, a countdown timer, repetition until one party achieves 3 wins, game simulation and further optional features.

### Technologies used

OpenCV-Python is a library of python bindings that are mainly used to solve computer vision problems. While Python is loved for its readability, it tends to be slower than languages such as C/C++. Therefore, OpenCV-Python essentially combines the best qualities from C++, OpenCV, API and Python to execute code in a concise and efficient manner. The main.py file uses libraries such as cv2, keras, tensorflow and numpy to predict the class (Rock, Paper, Scissors, Nothing) of the current video being displayed by the user.

Using the example code provided I was able to using my video feed to print the predicted class of each frame.
> NOTE: More information on the code and what it does can be found in the file named 'main.py'

## **Milestone 3: Create a Rock-Paper-Scissors game**
---

### Environment setup

To setup the environment I created a conda environment called 'rps' using the command `conda create -n rps python=3.8`. After solving the environment, I used `pip installed <library>` to get libraries such as keras, tensorflow, ipykernel, numpy, and opencv-python.

### Code

I created a file called manual_rps.py to simulate the game without the use of a camera. This file stores the user's input in a variable called 'get_user_choice' and randomizes the computers choice from a list and stores it in a variable called 'get_computer_choice'. A function called 'get_Winner' takes in 2 positional arguments 'get_user_choice', 'get_computer_choice' and finds the winner using 'if, elif and else' statements. All these functions are then stored in an overall function called 'Play' which prints out the winner based on the 'get_Winner' function.

## **Milestone 4: Use the camera to play Rock-Paper-Scissors**
---

I created a new file called camera_rps.py to host the combined functionalities of both the manual and main file. This new file starts with a welcome message screen that displays [s] to start and [q] to quit. The round_counter, user_wins and computer_wins are set to 0.

#

### Welcome message screen

> ![welcome_screen](https://user-images.githubusercontent.com/79672240/168870811-d908be7d-be56-4ff4-b91b-96686834a98f.png)

#

This then runs the Ready function that adds 1 to the round_counter, displays the round number and asks the player if they are ready or not. The user either presses [y] for yes which invokes the Round function, or [n] for no which takes the user back to the welcome message screen.

#

### Ready message screen

> ![ready_screen](https://user-images.githubusercontent.com/79672240/168872693-88c40ee1-2daa-4fda-92eb-aecd3753d97e.png)

#

After the user presses 'y', the Round function is invoked which starts by capturing the video feed using the cv2 function `cv2.VideoCapture(0)`, with 0 representing the primary device connected to your PC/Laptop. The keras model is loaded in using the `load_model('name_of_the_model.h5')` function and stored in a variable called 'model'. The 'get_computer_choice' variable chooses a random item from a rps list and stores it. An empty variable called 'get_user_choice' is set along with a countdown at 5. A while loop then continuously displays the video feed in a window called 'Rock, Paper, Scissors!'.The variable start_time records the time at which this loop starts. 

When the round starts, the round_counter is displayed in red at the middle-top of the window, a green countdown in the bottom middle, the user_wins at the bottom-left and computer_wins at the bottom-right. A variable called 'time_elapsed' stores the time that has passed, in seconds, since 'start_time' was invoked using `time.time()`. The countdown starts running down from 5 to 0, and after time_elapsed > 5, white text displays the choice the user and computer have made. At time_elapsed = 6, the user's choice is then returned to the variable 'get_user_choice'. Between 7 < time_elapsed < 12, the conditions are evaluated and the winner is displayed on screen with the 'winner' variable stored. The user_wins and computer_wins are then displayed and at time_elapsed = 12 the loop breaks, calling upon if statements that adds 1 to either user_wins or computer_wins depending on the state of the 'winner' variable. This is the end of a round, with Ready(round_counter, user_wins, computer_wins) calling upon the Ready screen.

The loop repeats.

#

### Round screen
> ![round_screen](https://user-images.githubusercontent.com/79672240/168876466-fd3d728d-390b-417d-9bf8-ff502191415c.png)

#

### Round screen - winner displayed and the wins updated
> ![round_screen_winner_and_wins](https://user-images.githubusercontent.com/79672240/168890602-00909eb4-e906-45a6-8227-7e50e83bb70f.png)

#

After either the user or computer get 3 wins, the code below in Ready() gets executed...

```
# Go to the win screen if either player gets 3 wins
if user_wins == 3 or computer_wins == 3:
    win_Screen(user_wins, computer_wins)
else:
    pass
```

This runs the win_Screen() function, which takes in the user_wins and computer_wins parameters, and spits out the winner screen as seen below

### Winner screen
> ![winner_screen](https://user-images.githubusercontent.com/79672240/168890686-e0f830a6-fae4-488f-9291-69640c3d4b4f.png)

#

The win screen has the option to reset the game by pressing [r] or quit the game by pressing [q]

### Error screen
> ![error_screen](https://user-images.githubusercontent.com/79672240/168891548-1362b056-60ca-4a3a-9b25-2cffd028c551.png)

#

If ret, the variable that checks if the frame is available, returns False the Error() function is executed which displayed the error screen above with the option to fix the error and retry by pressing [t]