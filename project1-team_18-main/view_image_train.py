import torchvision 
import torch.utils.data as Data 
import torchvision.transforms as tt
from torchvision.datasets import EMNIST
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import numpy as np
from torchvision import datasets, transforms
import sys
from PIL import Image as im
import torch as t #for nn

#Source code: https://jovian.ai/anurag3301/emnist-project
dataset_Transform = transform=tt.Compose([
                    lambda img: tt.functional.rotate(img, -90),
                    lambda img: tt.functional.hflip(img),
                    tt.ToTensor()
                ])
train_data = torchvision.datasets.EMNIST(root= './emnist_data', split='byclass', download= True, train=True,transform = dataset_Transform)
class train_images(QWidget):

    def __init__(self):
        super().__init__()

        # calling a defined method to initialize UI
        self.init_UI()
        

    def init_UI(self):
        root = QFileInfo(__file__).absolutePath()
        global Index
        Index = 0

        # Main window initialisation
        self.setFixedSize(1000,600)
        self.setWindowTitle('Viewer for train images')
        self.setWindowIcon(QIcon(root+'/Scripts/Icon/icon4.png'))
        
        self.wid = QWidget()
        #Set up a scroll area that can scroll down and scroll up
        self.sc = QScrollArea(self)

        #The total number of images
        total = len(train_data)
        if total % 12 == 0:
            rows = int(total/12)#Get the rows
        else:
            rows = int(total/12) + 1
        #Set up the size for scroll area
        self.wid.setMinimumSize(1000,250*rows)

        #Set iterations as 100000, as running total number will crash the program
        for i in range(100000):

            image = train_data[Index][0]
                    
            #Convert raw tensor to an ndarray and removes unecessary index
            imageToDisplay = image.numpy().squeeze(0)
                    
            #Convert floats to ints
            imageToDisplay *= 255
            imageToDisplay = imageToDisplay.astype(np.uint8)
                    
            #Use the PIL method to save image
            imagetosave = im.fromarray(imageToDisplay)
            imagetosave.save('image1.png')
            newImage = QImage('image1.png')
            #Convert the image into pixmap
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

        self.setLayout(vl)
        self.show()
        
if __name__ == '__main__':

    # create app
    App = QApplication(sys.argv)

    ex = train_images()

    # start the app
    sys.exit(App.exec())




