from pickle import FALSE
import torchvision 
from torchvision.datasets import EMNIST
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from torchvision import datasets, transforms
import sys

#Pass in the train dataset
test_data = torchvision.datasets.EMNIST(root="./emnist_data",train=False,download=True,transform=None,split="byclass")

data = test_data.targets
result = {}#Create a empty list to store the data

#Getting the number 
for i in data:
    if i.item() in result:
        result[i.item()] += 1
    else:
        result[i.item()] = 1

class statistics_test(QWidget):

    def __init__(self):
        super().__init__()

        # calling a defined method to initialize UI
        self.init_UI()
        

    def init_UI(self):
        root = QFileInfo(__file__).absolutePath()

        self.setWindowTitle('Statistics of test dataset')
        self.setWindowIcon(QIcon(root+'/Scripts/Icon/icon7.png'))
        self.setGeometry(300, 300, 500, 500) 

        self.addtable()

        self.show()


    def addtable(self):

        table = QTableWidget(self)
        table.setColumnCount(3)#Creating 3 columns becasue there's 3 classification which are digits, uppercase letters and lowercase letters
        table.setRowCount(27)#Creating three rows because there's a maximum of 26 letters and another row to specific the 3 classification

        #Add the first row
        table.setItem(0,0,QTableWidgetItem("Number of digits"))
        table.setItem(0,1,QTableWidgetItem("Number of uppercases letters"))
        table.setItem(0,2,QTableWidgetItem("Number of lowercases letters"))

        #Add the first column for displaying number of digits
        table.setItem(1,0,QTableWidgetItem("0:  "+str(result[0])))
        table.setItem(2,0,QTableWidgetItem("1:  "+str(result[1])))
        table.setItem(3,0,QTableWidgetItem("2:  "+str(result[2])))
        table.setItem(4,0,QTableWidgetItem("3:  "+str(result[3])))
        table.setItem(5,0,QTableWidgetItem("4:  "+str(result[4])))
        table.setItem(6,0,QTableWidgetItem("5:  "+str(result[5])))
        table.setItem(7,0,QTableWidgetItem("6:  "+str(result[6])))
        table.setItem(8,0,QTableWidgetItem("7:  "+str(result[7])))
        table.setItem(9,0,QTableWidgetItem("8:  "+str(result[8])))
        table.setItem(10,0,QTableWidgetItem("9:  "+str(result[9])))

        #Add the second column for displaying number of uppercase letters
        table.setItem(1,1,QTableWidgetItem("A:  "+str(result[10])))
        table.setItem(2,1,QTableWidgetItem("B:  "+str(result[11])))
        table.setItem(3,1,QTableWidgetItem("C:  "+str(result[12])))
        table.setItem(4,1,QTableWidgetItem("D:  "+str(result[13])))
        table.setItem(5,1,QTableWidgetItem("E:  "+str(result[14])))
        table.setItem(6,1,QTableWidgetItem("F:  "+str(result[15])))
        table.setItem(7,1,QTableWidgetItem("G:  "+str(result[16])))
        table.setItem(8,1,QTableWidgetItem("H:  "+str(result[17])))
        table.setItem(9,1,QTableWidgetItem("I:  "+str(result[18])))
        table.setItem(10,1,QTableWidgetItem("J:  "+str(result[19])))
        table.setItem(11,1,QTableWidgetItem("K:  "+str(result[20])))
        table.setItem(12,1,QTableWidgetItem("L:  "+str(result[21])))
        table.setItem(13,1,QTableWidgetItem("M:  "+str(result[22])))
        table.setItem(14,1,QTableWidgetItem("N:  "+str(result[23])))
        table.setItem(15,1,QTableWidgetItem("O:  "+str(result[24])))
        table.setItem(16,1,QTableWidgetItem("P:  "+str(result[25])))
        table.setItem(17,1,QTableWidgetItem("Q:  "+str(result[26])))
        table.setItem(18,1,QTableWidgetItem("R:  "+str(result[27])))
        table.setItem(19,1,QTableWidgetItem("S:  "+str(result[28])))
        table.setItem(20,1,QTableWidgetItem("T:  "+str(result[29])))
        table.setItem(21,1,QTableWidgetItem("U:  "+str(result[30])))
        table.setItem(22,1,QTableWidgetItem("V:  "+str(result[31])))
        table.setItem(23,1,QTableWidgetItem("W:  "+str(result[32])))
        table.setItem(24,1,QTableWidgetItem("X:  "+str(result[33])))
        table.setItem(25,1,QTableWidgetItem("Y:  "+str(result[34])))
        table.setItem(26,1,QTableWidgetItem("Z:  "+str(result[35])))

        #Add the last column for displaying number of lowercase letters
        table.setItem(1,2,QTableWidgetItem("a:  "+str(result[36])))
        table.setItem(2,2,QTableWidgetItem("b:  "+str(result[37])))
        table.setItem(3,2,QTableWidgetItem("c:  "+str(result[38])))
        table.setItem(4,2,QTableWidgetItem("d:  "+str(result[39])))
        table.setItem(5,2,QTableWidgetItem("e:  "+str(result[40])))
        table.setItem(6,2,QTableWidgetItem("f:  "+str(result[41])))
        table.setItem(7,2,QTableWidgetItem("g:  "+str(result[42])))
        table.setItem(8,2,QTableWidgetItem("h:  "+str(result[43])))
        table.setItem(9,2,QTableWidgetItem("i:  "+str(result[44])))
        table.setItem(10,2,QTableWidgetItem("j:  "+str(result[45])))
        table.setItem(11,2,QTableWidgetItem("k:  "+str(result[46])))
        table.setItem(12,2,QTableWidgetItem("l:  "+str(result[47])))
        table.setItem(13,2,QTableWidgetItem("m:  "+str(result[48])))
        table.setItem(14,2,QTableWidgetItem("n:  "+str(result[49])))
        table.setItem(15,2,QTableWidgetItem("o:  "+str(result[50])))
        table.setItem(16,2,QTableWidgetItem("p:  "+str(result[51])))
        table.setItem(17,2,QTableWidgetItem("q:  "+str(result[52])))
        table.setItem(18,2,QTableWidgetItem("r:  "+str(result[53])))
        table.setItem(19,2,QTableWidgetItem("s:  "+str(result[54])))
        table.setItem(20,2,QTableWidgetItem("t:  "+str(result[55])))
        table.setItem(21,2,QTableWidgetItem("u:  "+str(result[56])))
        table.setItem(22,2,QTableWidgetItem("v:  "+str(result[57])))
        table.setItem(23,2,QTableWidgetItem("w:  "+str(result[58])))
        table.setItem(24,2,QTableWidgetItem("x:  "+str(result[59])))
        table.setItem(25,2,QTableWidgetItem("y:  "+str(result[60])))
        table.setItem(26,2,QTableWidgetItem("z:  "+str(result[61])))

        main_layout = QVBoxLayout()
        main_layout.addWidget(table)

        self.setLayout(main_layout)



if __name__ == '__main__':

    # create app
    App = QApplication(sys.argv)

    ex = statistics_test()

    # start the app
    sys.exit(App.exec())
