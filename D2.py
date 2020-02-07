#import sys
#from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

from PyQt5 import QtCore,QtGui,QtWidgets

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *
import pandas as pd
#pd.plotting.register_matplotlib_converters()
import sys
import qtawesome
import os


class Example(QWidget):
    my_data = None

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        #self.setGeometry(300, 300, 300, 220)
        self.setFixedSize(1080,700) #在現在的螢幕顯示視窗 視窗大小
        self.cwd = os.getcwd()
        #self.resize(300,200)
        self.setWindowTitle('DAQ') #window text
        self.setWindowIcon(QIcon('6.png'))
        
        
        
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局
        
        #button
        self.button = QtWidgets.QPushButton("456", self)
        self.button.clicked.connect(QCoreApplication.instance().quit)
        self.button.resize(self.button.sizeHint())
        self.button.move(10, 10)
        
        '''self.button2 = QPushButton("save", self)
        self.button2.clicked.connect(lambda: self.slot_btn_saveFile())
        self.button2.resize(self.button.sizeHint())
        self.button2.move(50, 50)'''
        
        self.btn_chooseFile = QPushButton("選取文件", self)  
        #self.btn_chooseFile.setObjectName("btn_chooseFile")  
        #self.btn_chooseFile.setText("選取文件")
        self.btn_chooseFile.clicked.connect(self.slot_btn_chooseFile)
        self.btn_chooseFile.move(50, 50)
        
        self.btn_saveFile = QPushButton("保存文件", self)  
        self.btn_saveFile.clicked.connect(self.slot_btn_saveFile)
        self.btn_saveFile.move(200, 50)
        

        
        
    def slot_btn_chooseFile(self):
        global my_data
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,  
                                    "選取文件",  
                                    self.cwd, # 起始路径 
                                    "All Files (*);;Text Files (*.txt);;Csv Files (*.csv)")   # 设置文件扩展名过滤,用双分号间隔

        if fileName_choose == "":
            print("\n取消選擇")
            return

        # Path of the file to read
        #my_filepath = fileName_choose

        # Read the file into a variable spotify_data
        my_data = pd.read_csv(fileName_choose, index_col="page_id")
        print("\n妳選擇的文件為:")
        print(fileName_choose)
        print("文件篩選器類型: ",filetype)
        print(my_data)

    def slot_btn_saveFile(self):
        global my_data
        fileName_choose2, filetype = QFileDialog.getSaveFileName(self,  
                                    "文件保存",  
                                    self.cwd, # 起始路径 
                                    "Csv Files (*.csv);;All Files (*);;Text Files (*.txt)")  

        if fileName_choose2 == "":
            print("\n取消選擇")
            return
        my_d=pd.Series(["4 cups", "1 cup", "2 large", "1 can"], 
                       index=["Flour", "Milk", "Eggs", "Spam"], name="Dinner")
        #my_d.to_csv("fileName_choose2")
        print("\n你選擇要保存的文件為:")
        print(fileName_choose2)
        print("文件篩選器類型: ",filetype)
        my_data.to_csv(fileName_choose2)


    '''def set_save_path(self):

        save_path = filedialog.askdirectory(title='Save Path Selection')

        if save_path:
            configuration.save_path = save_path

        print(configuration.save_path)

    def load_clicked(self):
        self.tableWidget.check_change = False
        path = QFileDialog.getOpenFileName(self.tableWidget, 'Open CSV', os.getenv('HOME'), 'CSV(*.csv)')

        if path[0] != '':
            with open(path[0], newline='') as csv_file:
                #print(path[0])
                csv_reader = csv.reader(csv_file, dialect='excel')
                #print(list(csv_reader))
               # self.tableWidget.setRowCount(len(list(csv_reader)))
                self.tableWidget.setRowCount(0)
                self.tableWidget.setColumnCount(2)
               # my_file = csv.reader(csv_file, dialect='excel')
                #print(csv_reader)
                for row_data in csv_reader:
                    #print(row_data)
                    row = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row)
                    if len(row_data) > 2:
                        self.tableWidget.setColumnCount(len(row_data))
                    for column, stuff in enumerate(row_data):
                        item = QTableWidgetItem(stuff)
                        self.tableWidget.setItem(row, column, item)
               # print(list(csv_reader))        `
        self.tableWidget.check_change = True 
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)'''

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())