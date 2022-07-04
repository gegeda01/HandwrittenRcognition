
import sys
from turtle import position
from requests import options

import torch
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from train import train, test, DNN


class train_(QWidget):

    def __init__(self):
        super().__init__()

        # calling a defined method to initialize UI
        self.init_UI()

    # method for creating UI widgets
    def init_UI(self):
        root = QFileInfo(__file__).absolutePath()

        #Set up the start train button
        self.TrainAction = QPushButton(self)
        self.TrainAction.move(30,385)
        self.TrainAction.setText('Start')
        self.TrainAction.clicked.connect(self.train_click)
        #Set up the Stop button
        self.stopAction = QPushButton(self)
        self.stopAction.move(130,385)
        self.stopAction.setText('Stop')

        #Set up the Cancel button
        self.cancelAction = QPushButton(self)
        self.cancelAction.move(230,385)
        self.cancelAction.setText('Cancel')
        self.cancelAction.clicked.connect(self.close)

        #Set up a slide box for train datasets
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setGeometry(45, 60, 200, 30)
        self.slider.setRange(0, 100)
        self.slider.setSingleStep(1) 
        self.slider.valueChanged[int].connect(self.onChanged)

        self.label1 = QLabel(self)
        self.label1.move(270, 62)
        self.label1.setText(" ")

        qle = QLineEdit(self)
        qle.setGeometry(45, 270, 250, 30)
        
        self.label2 = QLabel("Train Dataset", self)
        self.label2.move(45,20)

        self.label3 = QLabel("Model Name",self)
        self.label3.move(45,230)

        self.label4 = QLabel("Select a function in DNN model(s)",self)
        self.label4.move(45,100)

        self.options = QComboBox(self)
        self.options.addItem("Nonlinear activation function (ReLU)")
        self.options.move(45,130)

        self.label5 = QLabel("Batch size",self)
        self.label5.move(45,170)

        self.label6 = QLabel("Epoch number",self)
        self.label6.move(170,170)

        self.qle2 = QLineEdit(self)
        self.qle2.setGeometry(45, 190, 100, 30)

        self.qle3 = QLineEdit(self)
        self.qle3.setGeometry(170, 190, 100, 30)

        self.pb =  QProgressBar(self)
        self.pb.setGeometry(30,330,320,30)

        #Set up the window, icon and size
        self.setWindowTitle('Train Datasets')
        self.setWindowIcon(QIcon(root+'/Scripts/Icon/icon3.png'))
        self.setGeometry(300, 300, 350, 430)        
        self.show()

    def onChanged(self, percent):
        self.label1.setText(str(percent)+"%")      # show the text
        self.label1.adjustSize()       # adjust the label size automatically
    def train_click(self):
        total_epoch = int(self.qle3.text())

        for epoch in range(0, total_epoch):
            train(epoch,int(self.qle2.text()))
            print("Epoch: ", epoch)
            self.pb.setValue(epoch/total_epoch*100)
        self.pb.setValue(100)
        test()
        torch.save(DNN.state_dict(), './model.pth')
        print('Model saved')

        self.diabox = QDialog()
        self.diabox.setFixedSize(350,400)

        self.model = QLabel("A model is being saved, below is the information: ")
        self.percentage = QLabel("Train/validation ratio: "+self.label1.text())
        self.dnn = QLabel("Selected dnn name: "+self.options.currentText())
        self.batch = QLabel("Batch size: "+self.qle2.text())
        self.epnumber = QLabel("Epoch number: "+self.qle3.text())

        self.loss = QLabel("Training Loss: ")
        self.acc  = QLabel("Accuracy: ")

        

        main = QVBoxLayout()
        main.addWidget(self.model)
        main.addWidget(self.percentage)
        main.addWidget(self.dnn)
        main.addWidget(self.batch)
        main.addWidget(self.epnumber)
        main.addWidget(self.loss)
        main.addWidget(self.acc)


        self.diabox.setLayout(main)
        self.diabox.exec()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = train_()
    sys.exit(app.exec_())
import sys
from turtle import position
from requests import options

import torch
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from train import train, test, DNN


class train_(QWidget):

    def __init__(self):
        super().__init__()

        # calling a defined method to initialize UI
        self.init_UI()

    # method for creating UI widgets
    def init_UI(self):
        root = QFileInfo(__file__).absolutePath()

        #Set up the start train button
        self.TrainAction = QPushButton(self)
        self.TrainAction.move(30,385)
        self.TrainAction.setText('Start')
        self.TrainAction.clicked.connect(self.train_click)
        #Set up the Stop button
        self.stopAction = QPushButton(self)
        self.stopAction.move(130,385)
        self.stopAction.setText('Stop')

        #Set up the Cancel button
        self.cancelAction = QPushButton(self)
        self.cancelAction.move(230,385)
        self.cancelAction.setText('Cancel')
        self.cancelAction.clicked.connect(self.close)

        #Set up a slide box for train datasets
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setGeometry(45, 60, 200, 30)
        self.slider.setRange(0, 100)
        self.slider.setSingleStep(1) 
        self.slider.valueChanged[int].connect(self.onChanged)

        self.label1 = QLabel(self)
        self.label1.move(270, 62)
        self.label1.setText(" ")
        #Set up the line edit for model name
        self.qle = QLineEdit(self)
        self.qle.setGeometry(45, 270, 250, 30)
        
        self.label2 = QLabel("Train Dataset", self)
        self.label2.move(45,20)

        self.label3 = QLabel("Model Name",self)
        self.label3.move(45,230)

        self.label4 = QLabel("Select a function in DNN model(s)",self)
        self.label4.move(45,100)
        #Insert the choice for selecting DNN
        self.options = QComboBox(self)
        self.options.addItem("Nonlinear activation funtion (ReLU")
        self.options.move(45,130)

        self.label5 = QLabel("Batch size",self)
        self.label5.move(45,170)

        self.label6 = QLabel("Epoch number",self)
        self.label6.move(170,170)
        #Set up the line edit for batch size
        self.qle2 = QLineEdit(self)
        self.qle2.setGeometry(45, 190, 100, 30)
        #Set up the line edit for epoch number
        self.qle3 = QLineEdit(self)
        self.qle3.setGeometry(170, 190, 100, 30)
        #Set up the progress bar
        self.pb =  QProgressBar(self)
        self.pb.setGeometry(30,330,320,30)
        #Set up the window, icon and size
        self.setWindowTitle('Train Datasets')
        self.setWindowIcon(QIcon(root+'/Scripts/Icon/icon3.png'))
        self.setGeometry(300, 300, 350, 430)        
        self.show()

    def onChanged(self, percent):
        self.label1.setText(str(percent)+"%")      # show the percentage
        self.label1.adjustSize()       # adjust the label size automatically
        
    def train_click(self):
        total_epoch = int(self.qle3.text()) #get the number of epoch

        for epoch in range(0, total_epoch): 
            train(epoch,int(self.qle2.text()))
            print("Epoch: ", epoch)
            self.pb.setValue(epoch/total_epoch*100)#Update the progress bar
        self.pb.setValue(100)
        test()
        torch.save(DNN.state_dict(), self.qle.text()+'.pth')
        print('Model saved')
        
        #Show up a window after trained
        self.diabox = QDialog()
        self.diabox.setFixedSize(350,550)
        #Show the information of the trained model
        self.model = QLabel("A model is being saved, below is the information: ")
        self.percentage = QLabel("Train/validation ratio: "+self.label1.text())
        self.dnn = QLabel("Selected dnn name: "+self.options.currentText())
        self.batch = QLabel("Batch size: "+self.qle2.text())
        self.epnumber = QLabel("Epoch number: "+self.qle3.text())

        self.loss = QLabel("Training Loss: ")
        self.acc  = QLabel("Accuracy: ")

        
        main = QVBoxLayout()
        main.addWidget(self.model)
        main.addWidget(self.percentage)
        main.addWidget(self.dnn)
        main.addWidget(self.batch)
        main.addWidget(self.epnumber)
        main.addWidget(self.loss)
        main.addWidget(self.acc)

        self.diabox.setLayout(main)
        self.diabox.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = train_()
    sys.exit(app.exec_())


    









