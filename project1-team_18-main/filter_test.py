from typing import Text
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

dataset_Transform = transform=tt.Compose([
                    lambda img: tt.functional.rotate(img, -90),
                    lambda img: tt.functional.hflip(img),
                    tt.ToTensor()
                ])
test_data = torchvision.datasets.EMNIST(root= './emnist_data', split='byclass', download= True, train=False,transform = dataset_Transform)




class test_filter(QWidget):

    def __init__(self):
        super().__init__()

        # calling a defined method to initialize UI
        self.init_UI()
        

    def init_UI(self):
        root = QFileInfo(__file__).absolutePath()
        
        # Main window initialisation
        self.setFixedSize(500,400)
        self.setWindowTitle('Filter for test images')
        self.setWindowIcon(QIcon(root+'/Scripts/Icon/icon8.png'))

        #Create the first page where users need to insert a specific digit or letter they want to view

        self.label1 = QLabel("Please select a specific digit or letter you want to view")
        self.label1.setFont(QFont('Times New Roman',11))
        self.Combo = QComboBox()
        #Insert all the digits and letters
        self.Combo.addItems(["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F", "G", "H", "I", "J", "K", "L", 
        "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","a","b","c","d","e","f", "g", "h", "i", "j", "k", 
        "l", "m", "n", "o", "p", "q", "r","s", "t", "u", "v", "w", "x", "y", "z"])
        #Set a button for showing the viewer
        self.start = QPushButton("Start")
        self.start.clicked.connect(self.openviewer)
        self.page1Layout = QVBoxLayout()
        self.page1Layout.addWidget(self.label1)
        self.page1Layout.addWidget(self.Combo)
        self.page1Layout.addWidget(self.start)
        self.setLayout(self.page1Layout)
        self.show()

    def openviewer(self):
        root = QFileInfo(__file__).absolutePath()
        Index = 0
        #Create the second page where users can view the result
        self.diaBox = QDialog()
        self.diaBox.setFixedSize(1000,600)
        self.diaBox.setWindowTitle("Viewer of particular pattern")
        self.diaBox.setWindowIcon(QIcon(root+'/Scripts/Icon/icon4.png'))
        self.wid = QWidget()
        self.sc = QScrollArea(self)
        #Getting the total number of datasets
        total = len(test_data)
        if total % 12 == 0:
            rows = int(total/12)#get the rows
        else:
            rows = int(total/12) + 1

        self.wid.setMinimumSize(1000,250*rows)

        for i in range(total):
            #If the index of the train_data is equal to the selected pattern index, start the following actions
            if test_data.targets[i] == self.Combo.currentIndex():
                image = test_data[i][0]
                #Converts raw tensor to an ndarray and removes unecessary index
                imageToDisplay = image.numpy().squeeze(0)
                    
                #Convert floats to ints
                imageToDisplay *= 255
                imageToDisplay = imageToDisplay.astype(np.uint8)
                    
                #Use the PIL method to save image
                imagetosave = im.fromarray(imageToDisplay)
                imagetosave.save('image4.png')
                newImage = QImage('image4.png')
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
                tmp.move(70 * (Index % 12), 83 * int(Index/ 12))
                Index = Index + 1

        self.sc.setWidget(self.wid)
        self.sc.setWidgetResizable(True)
        self.sc.setFixedHeight(1000)


        v2 = QVBoxLayout()
        v2.addWidget(self.sc)

        self.diaBox.setLayout(v2)

        self.diaBox.exec()


if __name__ == '__main__':

    # create app
    App = QApplication(sys.argv)

    ex = test_filter()

    # start the app
    sys.exit(App.exec())

