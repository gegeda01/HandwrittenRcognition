import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor
from PyQt5.QtCore import Qt, QPoint, QSize

#Source code: https://www.geeksforgeeks.org/pyqt5-create-paint-application/

class paintboard(QWidget):
    def __init__(self, Parent = None):
        super().__init__(Parent)
        
        #Set up default size and color for the canvas
        self.__size = QSize(300, 300)               
        self.__fill = QColor(255,255,255)                 

        #Define the start point and end point
        self.__start_point = QPoint()
        self.__end_point = QPoint()

        #Set up default thickness and color for the pen
        self.__thickness = 8               
        self.__penColor = QColor(0,0,0)

        self.__board = QPixmap(self.__size)
        self.__board.fill(self.__fill)
         
        self.setFixedSize(self.__size)
        self.__painter = QPainter()        


    def Clear(self):
        #Set up the clear method for the canvas
        self.__board.fill(self.__fill)
        self.update()

    
    def convertToImage(self):
        #Create the convert to image method
        image = self.__board.toImage()
        return image 


    def paintEvent(self, paintEvent):         
        self.__painter.begin(self)
        self.__painter.drawPixmap(0,0,self.__board)
        self.__painter.end()

    def showImage(self,image): #shows image file
        self.__board.fromImage(image)
        self.update()

    def mousePressEvent(self, mouseEvent):
        #Only if the left button of the mouse is pressed, will trigger the action
        if mouseEvent.button() == Qt.LeftButton:
            #Track the path of the mouse
            self.__start_point = mouseEvent.pos()
            self.__end_point = self.__start_point

    def mouseMoveEvent(self, mouseEvent):
        #Only if the left button of the mouse is pressed, will trigger the action
        if mouseEvent.buttons() == Qt.LeftButton:
            self.__end_point = mouseEvent.pos()
 
            self.__painter.begin(self.__board)#Begin the painter on canvas
            self.__painter.setPen(QPen(self.__penColor,self.__thickness))#Set up the pen setting
            self.__painter.drawLine(self.__start_point, self.__end_point)#Draw line between the two ppints
            self.__painter.end()

            self.__start_point = self.__end_point
            self.update()

