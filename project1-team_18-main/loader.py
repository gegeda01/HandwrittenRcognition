import urllib.request
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from zipfile import ZipFile
import os
import sys

#Source code: https://www.geeksforgeeks.org/pyqt5-how-to-automate-progress-bar-while-downloading-using-urllib/
class import_datasets(QWidget):

    def __init__(self):
        super().__init__()

        # calling a defined method to initialize UI
        self.init_UI()

    # method for creating UI widgets
    def init_UI(self):
        root = QFileInfo(__file__).absolutePath()

        #Set up the window, icon and size
        self.setWindowTitle('Import Datasets')
        self.setWindowIcon(QIcon(root+'/Scripts/Icon/icon6.png'))
        self.setGeometry(300, 300, 300, 300)        
        self.show()

        #Set up the Cancel button
        self.cancelAction = QPushButton(self)
        self.cancelAction.setText('Cancel')
        self.cancelAction.clicked.connect(self.close)

        #Set up the Start button
        self.stopAction = QPushButton(self)
        self.stopAction.setText('Stop')
        
        #Set up the Download Mnist button
        self.downloadAction = QPushButton(self)
        self.downloadAction.setText('Start')
        self.downloadAction.clicked.connect(self.Download)

        #creating progress bar
        self.progressBar = QProgressBar(self)

        #Set up the labels for time reminder
        self.label1 = QLabel("Time left: ")
        self.label1.setFont(QFont('Times New Roman',10))
        self.label2 = QLabel()
        self.label2.setFont(QFont('Times New Roman',12))
        self.label2.setStyleSheet("font-weight: bold")

        #layout of horizontal box
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.downloadAction)
        hbox1.addWidget(self.stopAction)
        hbox1.addWidget(self.cancelAction)

        #layout of horizontal box
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.label1)
        hbox2.addWidget(self.label2)

        #layout of vetical box
        vbox = QVBoxLayout() 
        vbox.addLayout(hbox2)
        vbox.addStretch(1) 
        vbox.addWidget(self.progressBar)
        vbox.addStretch(1) 
        vbox.addLayout(hbox1)
        vbox.addStretch(1) 

        #Set the main layout
        self.setLayout(vbox)

    def Handle_Progress(self, blocknum, blocksize, totalsize):

        # calculate the progress
        readed_data = blocknum * blocksize

        if totalsize > 0:
            time = 120.5#Average time for downloading
            download_percentage = int(readed_data * 100 / totalsize)
            self.progressBar.setValue(download_percentage)
            self.label2.setText(str(time-time*download_percentage*0.01)+"s")
            QApplication.processEvents()

    #method to download any file using urllib
    #when push button is pressed, this method is called
    def Download(self):
        
        #Specify the url of the file which is to be downloaded
        down_url = 'https://www.itl.nist.gov/iaui/vip/cs_links/EMNIST/gzip.zip' # specify download url here

        #Specify save location where the file is to be saved
        dir=os.path.abspath('.') 
        save_loc = os.path.join(dir,'EMNIST.zip')

        #Downloading using urllib
        urllib.request.urlretrieve(down_url,save_loc, self.Handle_Progress)

        #Once it is fully downloaded, extract the zip file
        with ZipFile('EMNIST.zip', 'r') as EMNISTObj:
           # Extract all the contents of zip file in current directory
               EMNISTObj.extractall()



if __name__ == '__main__':

    # create app
    App = QApplication(sys.argv)

    # create the instance of our window
    window = import_datasets()

    # start the app
    sys.exit(App.exec())
