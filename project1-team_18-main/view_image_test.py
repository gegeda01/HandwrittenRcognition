from msilib.schema import CheckBox
import torchvision 
import torch.utils.data as Data 
import torchvision.transforms as tt
from torchvision.datasets import EMNIST
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import numpy as np
from torchvision import datasets, transforms
import sys
from PIL import Image as im
import torch as t #for nn
import os

#Source code: https://jovian.ai/anurag3301/emnist-project
dataset_Transform = transform=tt.Compose([
                    lambda img: tt.functional.rotate(img, -90),
                    lambda img: tt.functional.hflip(img),
                    tt.ToTensor()
                ])
test_data = torchvision.datasets.EMNIST(root= './emnist_data', split='byclass', download= True, train=False,transform = dataset_Transform)
class test_images(QWidget):

    def __init__(self):
        super().__init__()

        # calling a defined method to initialize UI
        self.init_UI()
        

    def init_UI(self):
        root = QFileInfo(__file__).absolutePath()

        # Main window initialisation
        self.setFixedSize(300,300)
        self.setWindowTitle('Viewer for test images')
        self.setWindowIcon(QIcon(root+'/Scripts/Icon/icon5.png'))

        #Set up a label for instruction
        self.label1 = QLabel("Please select a mode to execute")
        self.label1.setFont(QFont('Times New Roman',11))

        #Set up the two modes selections
        self.view = QPushButton("Viewer mode")
        self.view.clicked.connect(self.openviewmode)
        self.test = QPushButton("Test mode")
        self.test.clicked.connect(self.opentestmode)
        
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.view)
        self.hbox.addWidget(self.test)

        main = QVBoxLayout()
        main.addWidget(self.label1)
        main.addLayout(self.hbox)

        #Set the layout
        self.setLayout(main)
        self.show()

    def openviewmode(self):
        root = QFileInfo(__file__).absolutePath()
        global Index
        Index = 0

        #Diabox gui initialisation
        self.diaBox = QDialog()
        self.diaBox.setFixedSize(1000,600)
        self.diaBox.setWindowTitle('Viewer mode for test images')
        self.diaBox.setWindowIcon(QIcon(root+'/Scripts/Icon/icon5.png'))

        self.wid = QWidget()

        #Set up a scroll area that can scroll down and scroll up
        self.sc = QScrollArea(self)

        #The total number of images
        total = len(test_data)
        if total % 12 == 0:
            rows = int(total/12)#Get the rows
        else:
            rows = int(total/12) + 1
        #Set up the size for scroll area
        self.wid.setMinimumSize(1000,250*rows)

        #Set iterations as 100000, as running total number will crash the program
        for i in range(100000):

            image = test_data[Index][0]
                    
            #Convert raw tensor to an ndarray and removes unecessary index
            imageToDisplay = image.numpy().squeeze(0)
                    
            #Convert floats to ints
            imageToDisplay *= 255
            imageToDisplay = imageToDisplay.astype(np.uint8)
                    
            #Use the PIL method to save image
            imagetosave = im.fromarray(imageToDisplay)
            imagetosave.save('image2.png')
            newImage = QImage('image2.png')
            pixmap = QPixmap.fromImage(newImage)
            pixmapImage = QPixmap(pixmap)
            
            tmp = QWidget(self.wid)
            vl = QVBoxLayout()

            #Set up the label for storing the pixmap image 
            label = QLabel()
            label.setFixedSize(60,60)
            label.setStyleSheet("border:1px solid gray")
            label.setPixmap(pixmapImage)
            label.setScaledContents(True)

            #Set up its corrensponding label
            name = QLabel(str(i),self)

            vl.addWidget(label)
            vl.addWidget(name)
            tmp.setLayout(vl)
            #Move some space for the next iteration
            tmp.move(70 * (i % 12), 83 * int(i / 12))
            Index = Index + 1

        self.sc.setWidget(self.wid)
        self.sc.setWidgetResizable(True)
        self.sc.setFixedHeight(1000)


        vl = QVBoxLayout()
        vl.addWidget(self.sc)

        self.diaBox.setLayout(vl)
        self.diaBox.exec()

    def opentestmode(self):
        root = QFileInfo(__file__).absolutePath()
        global Index
        Index = 0

        #Diabox2 gui initialisation
        self.diaBox2 = QDialog()
        self.diaBox2.setFixedSize(1000,600)
        self.diaBox2.setWindowTitle('Viewer mode for test images')
        self.diaBox2.setWindowIcon(QIcon(root+'/Scripts/Icon/icon5.png'))

        self.wid = QWidget()

        #Set up a scroll area that can scroll down and scroll up
        self.sc = QScrollArea(self)

        #The total number of images
        total = len(test_data)
        if total % 12 == 0:
            rows = int(total/12)#Get the rows
        else:
            rows = int(total/12) + 1
        self.wid.setMinimumSize(1000,250*rows)

        self.boxlist = []#Create a list to store all the checkboxs
        for i in range(10000):

            image = test_data[Index][0]
                    
            #Convert raw tensor to an ndarray and removes unecessary index
            imageToDisplay = image.numpy().squeeze(0)
                    
            #Convert floats to ints
            imageToDisplay *= 255
            imageToDisplay = imageToDisplay.astype(np.uint8)
                    
            #Use the PIL method to save image
            imagetosave = im.fromarray(imageToDisplay)
            imagetosave.save('image2.png')
            newImage = QImage('image2.png')
            pixmap = QPixmap.fromImage(newImage)
            pixmapImage = QPixmap(pixmap)
            
            tmp = QWidget(self.wid)
            vl = QVBoxLayout()

            #Set up the label for storing the pixmap image 
            label = QLabel()
            label.setFixedSize(60,60)
            label.setStyleSheet("border:1px solid gray")
            label.setPixmap(pixmapImage)
            label.setScaledContents(True)
            #Set its corrensponding checkboxs
            self.select = QCheckBox(str(i))
            #Append the checkbox
            self.boxlist.append(self.select)
            #Set up its corrensponding label
            name = QLabel("img"+str(i)+".png",self)

            vl.addWidget(label)
            vl.addWidget(name)
            vl.addWidget(self.select)
            tmp.setLayout(vl)
            tmp.move(70 * (i % 12), 120 * int(i / 12))
            Index = Index + 1
        


        self.sc.setWidget(self.wid)
        self.sc.setWidgetResizable(True)
        self.sc.setFixedHeight(1000)
        #Set up a button to save these selected images
        self.save_btn = QPushButton("Save")
        self.save_btn.setStyleSheet("background-color : yellow")
        self.save_btn.clicked.connect(self.check)
        vl = QVBoxLayout()
        vl.addWidget(self.sc)
        vl.addWidget(self.save_btn)

        self.diaBox2.setLayout(vl)
        self.diaBox2.show()

    def check(self):
        global Index
        Index = 0
        #Create a foler to store the selected images
        if os.path.isdir('selected_images'):
            pass
        else:
            os.makedirs('selected_images')
        
        for self.select in self.boxlist:
            if self.select.isChecked():
                image = test_data[Index][0]
                    
                #Convert raw tensor to an ndarray and removes unecessary index
                imageToDisplay = image.numpy().squeeze(0)
                    
                #Convert floats to ints
                imageToDisplay *= 255
                imageToDisplay = imageToDisplay.astype(np.uint8)
                    
                #Use the PIL method to save image into a specific folder
                imagetosave = im.fromarray(imageToDisplay)
                imagetosave.save('selected_images/image'+str(Index)+'.png')
                Index+=1
            else:
                pass
                Index+=1

    
if __name__ == '__main__':

    # create app
    App = QApplication(sys.argv)

    ex = test_images()

    # start the app
    sys.exit(App.exec())
