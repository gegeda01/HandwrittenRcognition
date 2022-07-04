# Handwritten Digits and Characters Recognition

**Authors:**

Project1-team18: Katherine Luo & Cynthia Cao

**A Brief Introduction of our project:**

Our project is called Handwritten Digits and Character Recognition. The main features of this project are importing datasets, viewing 
images of datasets, traning a model and predicting users' handwritten digit or letters. All of the features are able to run on GUI. 

**Set up:**

To start, first download Python 3.8 or a higher version.
Then download Conda 11.3 and run this command on Anconda Prompt to install pytorch: 
conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch.
Visual Studio code or Pycharm is preferable for code editing. 
Lastly, run these commands below in CMD:
- pip install torchvision
- pip install matplotlib
- pip install numpy
- pip install pyqt5
- pip install pillow
- pip install emnist
- pip install requests
- pip install urllib3
- pip install torch

## Running The Application:
- Download the zip file of project1-team_18 and extract it.
- Go to Folder - project1-team_18
- Double click the **Main.py** 
- Click Run and Debug on the left panel and choose your Python Interpreter.
- The main window will then pop up and means the program is runnable.

## Key Functionllities:
- Import the EMNIST Datasets
- Viewing Images of Datasets
- Training the model
- Recognition

**Import the EMNIST Datasets:**
- To import the datasets, go to File->Import Emnist Datasets
- Click "Start" to start the downloading
- A time reminder on the top tells you how many seconds are left and a progress bar in the middle tells you the progress percentage of downloading.
- Dowloading is stoppable by pressing "Stop" button

**Viewer of Images:**
- To view the images of the datasets, go to View->Training Images of datasets or View->Testing Images of datasets
- To view the Statistics of the total number for each digit and letter, go to View->Statistics of train datasets or View->Statistics of test datasets
- To view for a specifc digit or letter, go to View->Filter of train datasets or View->Filter of test datasets

**Training the model:**
- To train a model, go to File->Train
- Select the ratio of datasets that prefered to be trained
- Select a model
- Input the batch size and epoch number
- Input a preferable model name
- Press "Start" to start the training
- Once the training is done, a window will pop out that shows all the training informations

**Recognition:**
- Go back to main window
- Draw a random digit or letter inside the canvas in the middle
- Click "Recognise" to predict the pattern your write
- On the buttom, there's a section telling you the prediction and the accuracy

