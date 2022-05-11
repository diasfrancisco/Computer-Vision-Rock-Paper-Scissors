# **Computer-Vision-Rock-Paper-Scissors**

## **Milestone 1: Create the model**
---

The model used for the Computer-Vision-Rock-Paper-Scissors project was created using Teachable-Machine. The model was provided with image data from 4 classes. The classes were Rock, Paper, Scissors and Nothing. The image data was gathered using a webcam, with Teachable-Machine extracting the data frame by frame. After the data gathering phase the model was trained on a subset of the data and ready for download.

Prior to download the model was converted to a keras .h5 model in the cloud. After this conversion the model and labels file were downloaded and pushed to GitHub under the Computer-Vision-Rock-Paper-Scissors repository (public)

## **Milestone 2: Install the dependencies**
---

The current model will be run in a new virtual environment (called 'rps') on my local machine, with multiple iterations looking to add features such as user & computer inputs, win screens, a countdown timer, repetition until one party achieves 3 wins, game simulation and further optional features.

### Technologies used

OpenCV-Python is a library of python bindings that are mainly used to solve computer vision problems. While Python is loved for its readability, it tends to be slower than languages such as C/C++. Therefore, OpenCV-Python essentially combines the best qualities from C++, OpenCV, API and Python to execute code in a concise and efficent manner. The main.py file uses libraries such as cv2, keras, tensorflow and numpy to predict the class (Rock, Paper, Scissors, Nothing) of the current video being displayed by the user.

Using the example code provided I was able to using my video feed to print the predicted class of each frame.
> NOTE: More information on the code and what it does can be found in the file named 'main.py'

## **Milestone 3: Create a Rock-Paper-Scissors game**
---

### Environment setup

To setup the environment I created a conda environment called 'rps' using the command `conda create -n rps python=3.8`. After solving the environment, I used `pip installed <library>` to get libraries such as keras, tensorflow, ipykernel, numpy, and cvopen-python.

### Code

I created a file called manual_rps.py to simulate the game without the use of a camera. This file stores the user's input in a variable called 'get_user_choice' and randomizes the computers choice from a list and stores it in a variable called 'get_computer_choice'. A function called 'get_Winner' takes in 2 positional arguments 'get_user_choice', 'get_computer_choice' and finds the winner using 'if, elif and else' statements. All these functions are then stored in an overall function called 'Play' which prints out the winner based on the 'get_Winner' function.