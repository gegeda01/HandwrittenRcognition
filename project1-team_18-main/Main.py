import sys
from turtle import position
from PIL import Image 
import PIL
from PyQt5.QtWidgets import QWidget,QApplication, QAction, qApp, QMainWindow
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPainter, QPen, QPixmap, QColor, QImage
from loader import *
from paintboard import*
# from train import mnist_train as train_dataset, train, test, DNN
from view_image_test import*
from view_image_train import*
from train import DNN
from train_GUI import *
from statistics_train import*
from statistics_test import*
from filter_train import*
from filter_test import*

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    
    def initUI(self):

        #define root to find icon
        self.canvas = paintboard(self)
        root = QFileInfo(__file__).absolutePath()

        #Set up the window, icon and size
        self.setWindowTitle('Handwriten Digit Recognizer')
        self.setWindowIcon(QIcon(root+'/Scripts/Icon/icon1.jpg'))
        self.setGeometry(300, 300, 600, 600)  
        self.show()   

        #Set up the window type and create menu bar and button boxs
        window = QWidget()
        self.addmenubar() 
        self.addbuttons()

        #Create the labels for instructions and set up their sizes and fonts 
        self.label1 = QLabel("Hi, Please make sure you download the datasets and train before you start :)",self)
        self.label1.setFont(QFont('Times New Roman',11))
        self.label2 = QLabel("Prediction:",self)
        self.label2.setFont(QFont('Times New Roman',10))
        self.label3 = QLabel("Accuracy:",self)
        self.label3.setFont(QFont('Times New Roman',10))
        self.label4 = QLabel(self)
        self.label4.setFont(QFont('Times New Roman',15))
        self.label4.setStyleSheet("font-weight: bold")
        self.label5 = QLabel(self)
        self.label5.setFont(QFont('Times New Roman',15))
        self.label5.setStyleSheet("font-weight: bold")

        #Set up the horizontal layout for canvas and buttons
        sub_layout1 = QHBoxLayout()
        sub_layout1.addWidget(self.canvas)
        sub_layout1.addWidget(self.buttons)
        
        #Set up the horizontal layout for labels
        sub_layout2 = QHBoxLayout()
        sub_layout2.addWidget(self.label2)
        sub_layout2.addWidget(self.label4)
        sub_layout2.addWidget(self.label3)
        sub_layout2.addWidget(self.label5)

        #Set up the vertical layout and add the two sub layouts
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.label1)
        main_layout.addLayout(sub_layout1)
        main_layout.addLayout(sub_layout2)

        #Set the vertical layout as the main layout
        window.setLayout(main_layout)
        self.setCentralWidget(window)


    def addmenubar(self):
        #define root to find icon
        root = QFileInfo(__file__).absolutePath()

        #Set up the quit button in the file menu
        exitAction = QAction(QIcon(root+'/Scripts/Icon/icon2.png'), 'Quit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        #Set up the train button in the file menu
        trainaction = QAction(QIcon(root+'/Scripts/Icon/icon3.png'),'Train',self)
        trainaction.setShortcut('Ctrl+T')
        trainaction.setStatusTip('Train Model')
        trainaction.triggered.connect(self.train)

        #Set up the download emnist button in the file menu
        downloadaction = QAction(QIcon(root+'/Scripts/Icon/icon6.jpg'),'Import Emnist Datasets',self)
        downloadaction.setStatusTip('Import Datasets')
        downloadaction.triggered.connect(self.download)

        #Set up the training images button to view in the view menu
        trainingImages = QAction(QIcon(root+'/Scripts/Icon/icon4.png'),'Training Images of datasets',self)
        trainingImages.setStatusTip('Training Images')
        trainingImages.triggered.connect(self.train_image)

        #Set up the testing images button to view in the view menu
        testingImages = QAction(QIcon(root+'/Scripts/Icon/icon5.png'),'Testing Images of datasets',self)
        testingImages.setStatusTip('Testing Images')
        testingImages.triggered.connect(self.test_image)

        #Set up the statistics button for train set
        trainStatistics = QAction(QIcon(root+'/Scripts/Icon/icon7.png'),'Statistics of train datasets',self)
        trainStatistics.setStatusTip('Statistics of the number of each character or digit in train set')
        trainStatistics.triggered.connect(self.train_table)

        #Set up the statistics button for test set
        testStatistics = QAction(QIcon(root+'/Scripts/Icon/icon7.png'),'Statistics of test datasets',self)
        testStatistics.setStatusTip('Statistics of the number of each character or digit in test set')
        testStatistics.triggered.connect(self.test_table)

        #Set up the filter button for train set
        filterTrain = QAction(QIcon(root+'/Scripts/Icon/icon8.png'),'Filter of train datasets',self)
        filterTrain.setStatusTip("A filter to find particular digit or letter in train set")
        filterTrain.triggered.connect(self.train_filter)

        #Set up the filter button for test set
        filterTest = QAction(QIcon(root+'/Scripts/Icon/icon8.png'),'Filter of test datasets',self)
        filterTest.setStatusTip("A filter to find particular digit or letter in test set")
        filterTest.triggered.connect(self.test_filter)


        #Create file menu bar and add in the buttons 
        menubar = self.menuBar()
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(downloadaction)
        filemenu.addAction(trainaction)
        filemenu.addAction(exitAction)


        #Create view menu bar and add in the buttons
        viewmenu = menubar.addMenu('&View')
        viewmenu.addAction(trainingImages)
        viewmenu.addAction(testingImages)
        viewmenu.addAction(trainStatistics)
        viewmenu.addAction(testStatistics)
        viewmenu.addAction(filterTrain)
        viewmenu.addAction(filterTest)

        self.setMenuBar(menubar)

    def addbuttons(self):
        self.buttons = QGroupBox()

        #Set up the window 
        window = QWidget()

        #Set up the clear button to clear the canvas when clicked
        self.Clear = QPushButton("Clear")
        self.Clear.clicked.connect(self.canvas.Clear)

        #Set up the save button that users can save their drawings
        self.Save = QPushButton("Save")
        self.Save.clicked.connect(self.on_btn_Save_Clicked)

        #Set up the Recognise button for prediction of the drawing
        self.Recognise = QPushButton("Recognise")
        self.Recognise.clicked.connect(self.on_btn_Recognise_Clicked)

        layout = QVBoxLayout(window)#Set up the vertical layout for how these buttons would be displayed

        #Set up the button for importing the selected images for testing
        self.Import = QPushButton("Import selected images")
        self.Import.clicked.connect(self.on_btn_import)

        #Set up the button for loading saved models
        self.Load  = QPushButton("Load Saved Models")


        #Add in the buttons
        layout.addWidget(self.Clear)
        layout.addWidget(self.Save)
        layout.addWidget(self.Load)
        layout.addWidget(self.Import)
        layout.addWidget(self.Recognise)

        #Set the main layout for buttons
        self.buttons.setLayout(layout)

    def on_btn_Recognise_Clicked(self):
        #Get the image from the canvas
        img = np.frombuffer(self.canvas.convertToImage().bits().asstring(300*300*4),dtype=np.uint8).reshape(300,300,4)
        image = Image.fromarray(img).convert('L')
        image = PIL.ImageOps.invert(image)
        plt.imshow(image)
        plt.show()
        #Get the prediction of the image
        DNN.load_state_dict(torch.load('./model.pth'))
        with torch.no_grad():
            prediction = DNN.predict(image)

        #Display the prediction in the status bar
        self.label2.setText('Prediction:'+str(prediction[0]))
        self.label3.setText('Accuary:'+str(prediction[1]))

    def on_btn_import(self):
        self.canvas.Clear()#First clear everything on canvas
        file_filter = 'Image File(*.png)'#Define a file type that can be selected
        #Pop out the file dialog for choosing the images to test
        importPath = QFileDialog.getOpenFileName(self,caption="Select a image",directory=os.getcwd(),filter=file_filter)
        
    def on_btn_Save_Clicked(self):
        #Pop up a dialog to ask where to save
        savePath = QFileDialog.getSaveFileName(self, 'Save Your Paint', '.\\', '*.png')#Pop up a dialog to ask where to save
        print(savePath)
        #When the dialog is close
        if savePath[0] == "":
            print("Save cancel")
            return
        image = self.canvas.convertToImage#Save the drawing into image
        image.save(savePath[0])

    def on_btn_import(self):

        file_filter = 'Image File(*.png)'
        importPath = QFileDialog.getOpenFileName(self,caption="Select a image",directory=os.getcwd(),filter=file_filter)

        
    def download(self):
        #Import the import_datasets class for import window
        self.ui2 = import_datasets()
        self.ui2.show

    def train(self):
        #Import the train class for train window
        self.ui2 = train_()
        self.ui2.show()

    def train_image(self):
        #Import the train_images class for train images viewer
        self.ui2 = train_images()
        self.ui2.show

    def test_image(self):
        #Import the test_images class for test images viewer
        self.ui2 = test_images()
        self.ui2.show

    def train_table(self):
        #Import the statistics_train class for statistics table of train set
        self.ui2 = statistics_train()
        self.ui2.show

    def test_table(self):
        #Import the statistics_test class for statistics table of test set
        self.ui2 = statistics_test()
        self.ui2.show
    
    def train_filter(self):
        #Import the train_filter class for filter window of train set
        self.ui2 = train_filter()
        self.ui2.show

    def test_filter(self):
        #Import the test_filter class for filter window of test set
        self.ui2 = test_filter()
        self.ui2.show

    def test_filter(self):
        self.ui2 = test_filter()
        self.ui2.show
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())
