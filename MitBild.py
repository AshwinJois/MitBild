# Code to create a GUI with Image Processing features 

import cv2
import sys
import os
import numpy as np
import shutil
import pilgram
from PIL import Image
from matplotlib import pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QPixmap 
from PyQt5.QtWidgets import  QFileDialog ,QButtonGroup, QLabel 
from AboutWindow import Ui_HelpWindow


class Ui_MainWindow(object):
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1230, 809)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        MainWindow.setFont(font)
        MainWindow.setAcceptDrops(False)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("background-color: gray;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.event_list = list()
        self.label_Image = QtWidgets.QLabel(self.centralwidget)
        self.label_Image.setGeometry(QtCore.QRect(40, 30, 811, 441))        
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.label_Image.setStyleSheet("background-color: white;")
        self.label_Image.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_Image.setFont(font)
        self.label_Image.setAutoFillBackground(True)
        self.label_Image.setObjectName("label_Image")
                        
        self.Right_button = QtWidgets.QPushButton(self.centralwidget)
        self.Right_button.setGeometry(QtCore.QRect(500, 500, 91, 31))
        self.Right_button.setObjectName("Right_button")
        self.Right_button.clicked.connect(self.rotate_img_right)
        self.Right_button.setCheckable(True) # To display Button's status (Clicked or not) 
        self.Right_button.setStyleSheet("background-color: white;")        
        
        self.Left_button = QtWidgets.QPushButton(self.centralwidget)
        self.Left_button.setGeometry(QtCore.QRect(290, 500, 101, 31))
        self.Left_button.setObjectName("Left_button")
        self.Left_button.clicked.connect(self.rotate_img_left)
        self.Left_button.setCheckable(True)
        self.Left_button.setStyleSheet("background-color: white;")

        self.label_histogram = QtWidgets.QLabel(self.centralwidget)
        self.label_histogram.setGeometry(QtCore.QRect(870, 220, 351, 251))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        self.label_histogram.setFont(font)
        self.label_histogram.setAutoFillBackground(True)
        self.label_histogram.setObjectName("label_histogram")
        self.label_histogram.setPalette(palette)       
        self.label_histogram.setStyleSheet("background-color: white;")
            
        self.Flip_button = QtWidgets.QPushButton(self.centralwidget)
        self.Flip_button.setGeometry(QtCore.QRect(420, 500, 51, 31))
        self.Flip_button.setObjectName("Flip_button")
        self.Flip_button.clicked.connect(self.flip_image)
        self.Flip_button.setCheckable(True)
        self.Flip_button.setStyleSheet("background-color: white;")
        
        self.ResetImg_button = QtWidgets.QPushButton(self.centralwidget)
        self.ResetImg_button.setGeometry(QtCore.QRect(30, 700, 131, 41))
        self.ResetImg_button.setObjectName("ResetImg_button")
        self.ResetImg_button.setCheckable(True)
        self.ResetImg_button.clicked.connect(self.reset_image)        
        self.ResetImg_button.setStyleSheet("background-color: white;")
                    
        self.horizontalSlider_R = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_R.setGeometry(QtCore.QRect(920, 50, 101, 22))
        self.horizontalSlider_R.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_R.setObjectName("horizontalSlider_R")
                
        self.horizontalSlider_H = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_H.setGeometry(QtCore.QRect(1080, 50, 101, 22))
        self.horizontalSlider_H.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_H.setObjectName("horizontalSlider_H")
                
        self.horizontalSlider_V = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_V.setGeometry(QtCore.QRect(1080, 130, 101, 22))
        self.horizontalSlider_V.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_V.setObjectName("horizontalSlider_V")
        
        self.horizontalSlider_G = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_G.setGeometry(QtCore.QRect(920, 90, 101, 22))
        self.horizontalSlider_G.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_G.setObjectName("horizontalSlider_G")
        self.horizontalSlider_G.setObjectName("horizontalSlider_G")
        
        self.horizontalSlider_B = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_B.setGeometry(QtCore.QRect(920, 130, 101, 22))
        self.horizontalSlider_B.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_B.setObjectName("horizontalSlider_B")
        self.horizontalSlider_B.setObjectName("horizontalSlider_G")

        self.horizontalSlider_S = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_S.setGeometry(QtCore.QRect(1080, 90, 101, 22))
        self.horizontalSlider_S.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_S.setObjectName("horizontalSlider_S")
        self.horizontalSlider_S.setObjectName("horizontalSlider_G")
        
        self.Change_Image_button = QtWidgets.QPushButton(self.centralwidget)
        self.Change_Image_button.setGeometry(QtCore.QRect(30, 640, 131, 41))
        self.Change_Image_button.setObjectName("AddVideo_button")
        self.Change_Image_button.setCheckable(True)  
        self.Change_Image_button.clicked.connect(self.change_image)
        self.Change_Image_button.setStyleSheet("background-color: white;")
                
        self.BG_Sub_button = QtWidgets.QPushButton(self.centralwidget)
        self.BG_Sub_button.setGeometry(QtCore.QRect(730, 580, 151, 41))
        self.BG_Sub_button.setObjectName("BG_Sub_button")
        self.BG_Sub_button.setCheckable(True)
        self.BG_Sub_button.clicked.connect(self.saliency_map)        
        self.BG_Sub_button.setStyleSheet("background-color: white;")
        
        self.Saliency_det_button = QtWidgets.QPushButton(self.centralwidget)
        self.Saliency_det_button.setGeometry(QtCore.QRect(730, 640, 151, 41))
        self.Saliency_det_button.setObjectName("OpticalFlow_button")
        self.Saliency_det_button.setCheckable(True)        
        self.Saliency_det_button.setStyleSheet("background-color: white;")
        self.Saliency_det_button.clicked.connect(self.saliency_detection)        
        
        self.Threshold_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Threshold_Button.setGeometry(QtCore.QRect(730, 700, 151, 41))
        self.Threshold_Button.setObjectName("EdgeDet_Button")
        self.Threshold_Button.setCheckable(True)        
        self.Threshold_Button.setStyleSheet("background-color: white;")
        self.Threshold_Button.clicked.connect(self.threshold_image)
        
        self.AddImage_button = QtWidgets.QPushButton(self.centralwidget)
        self.AddImage_button.setGeometry(QtCore.QRect(30, 580, 131, 41))
        self.AddImage_button.setObjectName("AddImage_button")
        self.AddImage_button.clicked.connect(self.add_image) # To open a folder 
        self.AddImage_button.setCheckable(True)        
        self.AddImage_button.setStyleSheet("background-color: white;")
        
        self.HarrisDet_button = QtWidgets.QPushButton(self.centralwidget)
        self.HarrisDet_button.setGeometry(QtCore.QRect(210, 640, 131, 41))
        self.HarrisDet_button.setObjectName("HarrisDet_button")
        self.HarrisDet_button.clicked.connect(self.harris_corner_detection)
        self.HarrisDet_button.setCheckable(True) 
        self.HarrisDet_button.setStyleSheet("background-color: white;")
       
        self.CannyDet_button = QtWidgets.QPushButton(self.centralwidget)
        self.CannyDet_button.setGeometry(QtCore.QRect(210, 700, 131, 41))
        self.CannyDet_button.setObjectName("CannyDet_button")
        self.CannyDet_button.clicked.connect(self.canny_edge_detection)
        self.CannyDet_button.setCheckable(True)
        self.CannyDet_button.setStyleSheet("background-color: white;")

        self.HSV_button = QtWidgets.QPushButton(self.centralwidget)
        self.HSV_button.setGeometry(QtCore.QRect(210, 580, 131, 41))
        self.HSV_button.setObjectName("SaliencyDet_button")
        self.HSV_button.setCheckable(True)
        self.HSV_button.setStyleSheet("background-color: white;")
        self.HSV_button.clicked.connect(self.hsv_image)
         
        self.moon_button = QtWidgets.QPushButton(self.centralwidget)
        self.moon_button.setGeometry(QtCore.QRect(390, 580, 141, 41))
        self.moon_button.setObjectName("Gray_nutton")
        self.moon_button.setCheckable(True)
        self.moon_button.clicked.connect(self.Moon_effect)
        self.moon_button.setStyleSheet("background-color: white;")

        self.Early_button = QtWidgets.QPushButton(self.centralwidget)
        self.Early_button.setGeometry(QtCore.QRect(390, 640, 141, 41))
        self.Early_button.setObjectName("Blur_button")
        self.Early_button.setCheckable(True)        
        self.Early_button.clicked.connect(self.EarlyBird_effect)
        self.Early_button.setStyleSheet("background-color: white;")

        self.Brooklyn_button = QtWidgets.QPushButton(self.centralwidget)
        self.Brooklyn_button.setGeometry(QtCore.QRect(540, 580, 141, 41))
        self.Brooklyn_button.setObjectName("Vintage_button")
        self.Brooklyn_button.setCheckable(True)        
        self.Brooklyn_button.clicked.connect(self.Brooklyn_effect)
        self.Brooklyn_button.setStyleSheet("background-color: white;")

        self.Hudson_button = QtWidgets.QPushButton(self.centralwidget)
        self.Hudson_button.setGeometry(QtCore.QRect(540, 640, 141, 41))
        self.Hudson_button.setObjectName("Gotham_button")
        self.Hudson_button.setCheckable(True)        
        self.Hudson_button.clicked.connect(self.Hudson_effect)
        self.Hudson_button.setStyleSheet("background-color: white;")

        self.Nashville_button = QtWidgets.QPushButton(self.centralwidget)
        self.Nashville_button.setGeometry(QtCore.QRect(540, 700, 141, 41))
        self.Nashville_button.setObjectName("New1_button")
        self.Nashville_button.setCheckable(True)        
        self.Nashville_button.clicked.connect(self.Nashville_effect)
        self.Nashville_button.setStyleSheet("background-color: white;")

        self.Blur_button = QtWidgets.QPushButton(self.centralwidget)
        self.Blur_button.setGeometry(QtCore.QRect(390, 700, 141, 41))
        self.Blur_button.setObjectName("New_button")
        self.Blur_button.setCheckable(True)        
        self.Blur_button.clicked.connect(self.Kelvin_effect)
        self.Blur_button.setStyleSheet("background-color: white;")        
        
        self.label_R = QtWidgets.QLabel(self.centralwidget)
        self.label_R.setGeometry(QtCore.QRect(900, 50, 21, 21))
        self.label_R.setObjectName("label_R")
        self.label_R.setStyleSheet("background-color: gray;")         
        
        self.label_B = QtWidgets.QLabel(self.centralwidget)
        self.label_B.setGeometry(QtCore.QRect(900, 130, 16, 16))
        self.label_B.setObjectName("label_B")
        self.label_B.setStyleSheet("text-color: gray;")
       
        self.label_G = QtWidgets.QLabel(self.centralwidget)
        self.label_G.setGeometry(QtCore.QRect(900, 90, 16, 16))
        self.label_G.setObjectName("label_G")
        self.label_G.setStyleSheet("background-color: gray;")
 
        self.label_S = QtWidgets.QLabel(self.centralwidget)
        self.label_S.setGeometry(QtCore.QRect(1060, 90, 16, 16))
        self.label_S.setObjectName("label_S")
        self.label_S.setStyleSheet("background-color: gray;")
        
        self.label_H = QtWidgets.QLabel(self.centralwidget)
        self.label_H.setGeometry(QtCore.QRect(1060, 50, 21, 21))
        self.label_H.setObjectName("label_H")
        self.label_H.setStyleSheet("background-color: gray;")
        
        self.label_V = QtWidgets.QLabel(self.centralwidget)
        self.label_V.setGeometry(QtCore.QRect(1060, 130, 16, 16))
        self.label_V.setObjectName("label_V")
        self.label_V.setStyleSheet("background-color: gray;")
        
        self.label_FeatureDet = QtWidgets.QLabel(self.centralwidget)
        self.label_FeatureDet.setGeometry(QtCore.QRect(209, 549, 141, 31))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_FeatureDet.setFont(font)
        self.label_FeatureDet.setObjectName("label_FeatureDet")
        self.label_FeatureDet.setStyleSheet("background-color: gray;")
                
        self.objectDet_button = QtWidgets.QPushButton(self.centralwidget)
        self.objectDet_button.setGeometry(QtCore.QRect(930, 580, 131, 41))
        self.objectDet_button.setObjectName("objectDet_button")
        self.objectDet_button.setCheckable(True)        
        self.objectDet_button.setStyleSheet("background-color: white;")
        self.objectDet_button.clicked.connect(self.object_detection)
        
        self.Exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.Exit_button.setGeometry(QtCore.QRect(1100, 640, 111, 41))
        self.Exit_button.setObjectName("Exit_button")
        self.Exit_button.clicked.connect(Exit_Window)
        self.Exit_button.setCheckable(True)        
        self.Exit_button.setStyleSheet("background-color: white;")

        self.Save_button = QtWidgets.QPushButton(self.centralwidget)
        self.Save_button.setGeometry(QtCore.QRect(1100, 580, 111, 41))
        self.Save_button.setObjectName("Save_button")
        self.Save_button.setCheckable(True)        
        self.Save_button.setStyleSheet("background-color: white;")
        self.Save_button.clicked.connect(self.save_image)
       
        self.label_FeatureDet_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_FeatureDet_2.setGeometry(QtCore.QRect(1010, 180, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_FeatureDet_2.setFont(font)
        self.label_FeatureDet_2.setObjectName("label_FeatureDet_2")
        self.label_FeatureDet_2.setStyleSheet("background-color: gray;")        
        
        self.label_FeatureDet_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_FeatureDet_3.setGeometry(QtCore.QRect(490, 549, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_FeatureDet_3.setFont(font)
        self.label_FeatureDet_3.setObjectName("label_FeatureDet_3")
        self.label_FeatureDet_3.setStyleSheet("background-color: gray;")
        
        self.label_FeatureDet_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_FeatureDet_4.setGeometry(QtCore.QRect(930, 550, 141, 31))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_FeatureDet_4.setFont(font)
        self.label_FeatureDet_4.setObjectName("label_FeatureDet_4")
        self.label_FeatureDet_4.setStyleSheet("background-color: gray;")

        self.label_FeatureDet_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_FeatureDet_5.setGeometry(QtCore.QRect(746, 549, 141, 31))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_FeatureDet_5.setFont(font)
        self.label_FeatureDet_5.setObjectName("label_FeatureDet_5")
        self.label_FeatureDet_5.setStyleSheet("background-color: gray;")
                
        self.label_FeatureDet_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_FeatureDet_6.setGeometry(QtCore.QRect(1020, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_FeatureDet_6.setFont(font)
        self.label_FeatureDet_6.setObjectName("label_FeatureDet_6")
        self.label_FeatureDet_6.setStyleSheet("background-color: gray;")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1230, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuFile.triggered.connect(self.helpwindow)
        
        MainWindow.setMenuBar(self.menuBar)
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.menuFile.addAction(self.actionHelp)
        self.menuFile.addSeparator()
        self.menuBar.addAction(self.menuFile.menuAction())

        self.remaining_button_state()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

# Creating a group, adding buttons to the group for displaying Button's status(clicked or not)
        self.button_group = QButtonGroup()
        self.button_group.addButton(self.AddImage_button)
        self.button_group.addButton(self.Change_Image_button)
        self.button_group.addButton(self.ResetImg_button)
        self.button_group.addButton(self.HSV_button)
        self.button_group.addButton(self.HarrisDet_button)
        self.button_group.addButton(self.CannyDet_button)
        self.button_group.addButton(self.moon_button)
        self.button_group.addButton(self.Brooklyn_button)
        self.button_group.addButton(self.Early_button)
        self.button_group.addButton(self.Hudson_button)
        self.button_group.addButton(self.objectDet_button)
        self.button_group.addButton(self.Nashville_button)
        self.button_group.addButton(self.Blur_button)
        self.button_group.addButton(self.Threshold_Button)
        self.button_group.addButton(self.Saliency_det_button)
        self.button_group.addButton(self.BG_Sub_button)
        self.button_group.addButton(self.Right_button)
        self.button_group.addButton(self.Left_button)
        self.button_group.addButton(self.Flip_button)
        self.button_group.addButton(self.Save_button)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MitBild"))
        self.label_Image.setText(_translate("MainWindow", "                                                Add Image"))
        self.Right_button.setText(_translate("MainWindow", "Rotate Right"))
        self.Left_button.setText(_translate("MainWindow", "Rotate Left"))
        self.label_histogram.setText(_translate("MainWindow", "                         Histogram"))
        self.Flip_button.setText(_translate("MainWindow", "Flip"))
        self.ResetImg_button.setText(_translate("MainWindow", "Reset Image"))
        self.Change_Image_button.setText(_translate("MainWindow", "Change Image"))
        self.BG_Sub_button.setText(_translate("MainWindow", "Saliency Map"))
        self.Saliency_det_button.setText(_translate("MainWindow", "Saliency Detection"))
        self.Threshold_Button.setText(_translate("MainWindow", "Threshold Image"))
        self.AddImage_button.setText(_translate("MainWindow", "Add Image"))
        self.HarrisDet_button.setText(_translate("MainWindow", "Harris Detection"))
        self.CannyDet_button.setText(_translate("MainWindow", "Canny Detection"))
        self.HSV_button.setText(_translate("MainWindow", "HSV Image"))
        self.moon_button.setText(_translate("MainWindow", "Moon"))
        self.Early_button.setText(_translate("MainWindow", "Early Bird"))
        self.Brooklyn_button.setText(_translate("MainWindow", "Brooklyn"))
        self.Hudson_button.setText(_translate("MainWindow", "Hudson"))
        self.Nashville_button.setText(_translate("MainWindow", "Nashville"))
        self.Blur_button.setText(_translate("MainWindow", "Blur"))
        self.label_R.setText(_translate("MainWindow", "R"))
        self.label_B.setText(_translate("MainWindow", "B"))
        self.label_G.setText(_translate("MainWindow", "G"))
        self.label_S.setText(_translate("MainWindow", "S"))
        self.label_H.setText(_translate("MainWindow", "H"))
        self.label_V.setText(_translate("MainWindow", "V"))
        self.label_FeatureDet.setText(_translate("MainWindow", "Feature Detection"))
        self.objectDet_button.setText(_translate("MainWindow", "Detect"))
        self.Exit_button.setText(_translate("MainWindow", "Exit"))
        self.Save_button.setText(_translate("MainWindow", "Save"))
        self.label_FeatureDet_2.setText(_translate("MainWindow", "Histogram"))
        self.label_FeatureDet_3.setText(_translate("MainWindow", "Image Effects"))
        self.label_FeatureDet_4.setText(_translate("MainWindow", "Object Detection"))
        self.label_FeatureDet_5.setText(_translate("MainWindow", "Salient Features"))
        self.label_FeatureDet_6.setText(_translate("MainWindow", "Levels"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionHelp.setText(_translate("MainWindow", "About"))

# State of all other Buttons when "Add Image" Button is clicked
    def buttonstate(self):
            
            if self.AddImage_button.isChecked():
                self.AddImage_button.setEnabled(False) 
                self.Change_Image_button.setEnabled(True)
                self.ResetImg_button.setEnabled(True)
                self.HSV_button.setEnabled(True)
                self.HarrisDet_button.setEnabled(True)
                self.CannyDet_button.setEnabled(True)
                self.moon_button.setEnabled(True)
                self.Brooklyn_button.setEnabled(True)
                self.Early_button.setEnabled(True)
                self.Hudson_button.setEnabled(True)
                self.Threshold_Button.setEnabled(True)
                self.Saliency_det_button.setEnabled(True)
                self.BG_Sub_button.setEnabled(True)
                self.Right_button.setEnabled(True)
                self.Left_button.setEnabled(True)
                self.Flip_button.setEnabled(True)           
                self.Blur_button.setEnabled(True)
                self.Nashville_button.setEnabled(True)
                self.objectDet_button.setEnabled(True)

            elif self.Change_Image_button.isChecked():                
                self.AddImage_button.setEnabled(False) 
                self.Change_Image_button.setEnabled(True)
                self.ResetImg_button.setEnabled(True)
                self.HSV_button.setEnabled(True)
                self.HarrisDet_button.setEnabled(True)
                self.CannyDet_button.setEnabled(True)
                self.moon_button.setEnabled(True)
                self.Brooklyn_button.setEnabled(True)
                self.Early_button.setEnabled(True)
                self.Hudson_button.setEnabled(True)
                self.Threshold_Button.setEnabled(True)
                self.Saliency_det_button.setEnabled(True)
                self.BG_Sub_button.setEnabled(True)
                self.Right_button.setEnabled(True)
                self.Left_button.setEnabled(True)
                self.Flip_button.setEnabled(True)           
                self.Blur_button.setEnabled(True)
                self.Nashville_button.setEnabled(True)
                self.objectDet_button.setEnabled(True)                
                                   
            else:      
                self.remaining_button_state()

    def HSV_slider_status(self):
        if self.HSV_button.isChecked():
            self.horizontalSlider_H.setEnabled(True)
            self.horizontalSlider_S.setEnabled(True)
            self.horizontalSlider_V.setEnabled(True)
            self.horizontalSlider_R.setEnabled(False)
            self.horizontalSlider_G.setEnabled(False)
            self.horizontalSlider_B.setEnabled(False)

        else:
            self.horizontalSlider_H.setEnabled(False)
            self.horizontalSlider_S.setEnabled(False)
            self.horizontalSlider_V.setEnabled(False)
            self.horizontalSlider_R.setEnabled(True)
            self.horizontalSlider_G.setEnabled(True)
            self.horizontalSlider_B.setEnabled(True)

# Initial State of all the Buttons when GUI is opened
    def remaining_button_state(self):
       self.AddImage_button.setEnabled(True)
       self.Change_Image_button.setEnabled(False)
       self.Exit_button.setEnabled(True)
       self.ResetImg_button.setEnabled(False)
       self.HSV_button.setEnabled(False)
       self.HarrisDet_button.setEnabled(False)
       self.CannyDet_button.setEnabled(False)
       self.moon_button.setEnabled(False)
       self.Brooklyn_button.setEnabled(False)
       self.Early_button.setEnabled(False)
       self.Hudson_button.setEnabled(False)
       self.Threshold_Button.setEnabled(False)
       self.Saliency_det_button.setEnabled(False)
       self.BG_Sub_button.setEnabled(False)
       self.Right_button.setEnabled(False)
       self.Left_button.setEnabled(False)
       self.Flip_button.setEnabled(False)       
       self.Blur_button.setEnabled(False)
       self.Nashville_button.setEnabled(False)
       self.objectDet_button.setEnabled(False)
       self.horizontalSlider_H.setEnabled(False)
       self.horizontalSlider_S.setEnabled(False)
       self.horizontalSlider_V.setEnabled(False)
       self.horizontalSlider_R.setEnabled(False)
       self.horizontalSlider_G.setEnabled(False)
       self.horizontalSlider_B.setEnabled(False)

    def helpwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HelpWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def add_image(self):
        Path_to_image = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","All Files (*);;jpeg (*.jpg)")        
        #os.mkdir(os.getcwd()+"\\temp")
        original_image = cv2.imread(Path_to_image[0])
        os.mkdir(os.getcwd()+"\\temp")

        dimensions = original_image.shape
        width = original_image.shape[0]
        height = original_image.shape[1]
        channels = original_image.shape[2]

        Temp_path = (os.getcwd()+"\\temp\\all_new.jpeg")
        cv2.imwrite(Temp_path,original_image)
        label = QLabel(self.label_Image)
        pixmap = QPixmap(Temp_path)
        if (width>height):   
            pix_map = pixmap.scaled(320, 480)
        else:
            pix_map = pixmap.scaled(640, 480)
                           
        self.event_list.append(Temp_path)        
        self.label_Image.setAlignment(Qt.AlignCenter)
        self.label_Image.setPixmap(pix_map)        
        self.update_histogram(Temp_path)
        self.buttonstate()
        self.update_rgb_channel(Temp_path)
        self.HSV_slider_status()
        self.set_sliders_to_zero


    def change_image(self):
        shutil.rmtree(os.getcwd()+"\\temp")
        self.add_image()
        self.set_sliders_to_zero()
      

    def update_histogram(self,path_to_image):        
        img = cv2.imread(path_to_image)
        Temp_path_histogram = (os.getcwd()+"\\temp\\curr_img_histogram.jpeg")
        hist = cv2.calcHist([img],[0],None,[256],[0,256])
        Histogram = plt.hist(img.ravel(),256,[0,256])           
        plt.savefig(Temp_path_histogram)
        label_2= QLabel(self.label_histogram)
        pixmap = QPixmap(Temp_path_histogram)
        pix_map = pixmap.scaled(351, 251)
        self.label_histogram.setPixmap(pix_map) 

    
    def Moon_effect(self):        
        Temp_path = (os.getcwd()+"\\temp\\all_new.jpeg")    
        img = cv2.imread(Temp_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        dimensions = img.shape
        width = img.shape[0]
        height = img.shape[1]
        channels = img.shape[2]
        Temp_path_Moon_effect = (os.getcwd()+"\\temp\\Moon_Effect.jpeg")
        cv2.imwrite(Temp_path_Moon_effect,gray)
        self.event_list.append(Temp_path_Moon_effect)       
        label = QLabel(self.label_Image)
        pixmap = QPixmap(Temp_path_Moon_effect)        
        if (width>height):   
            pix_map = pixmap.scaled(320, 480)
        else:
            pix_map = pixmap.scaled(640, 480)                 
        self.label_Image.setAlignment(Qt.AlignCenter) # Aligns the displayed image in the middle
        self.label_Image.setPixmap(pix_map)  
        self.update_histogram(Temp_path_Moon_effect)
        self.HSV_slider_status()
    
    def Brooklyn_effect(self):
        Temp_path = (os.getcwd()+"\\temp\\all_new.jpeg") 
        im = Image.open(Temp_path)
        Temp_path_brooklyn_effect = (os.getcwd()+"\\temp\\Brooklyn_Effect.jpeg")
        pilgram.brooklyn(im).save(Temp_path_brooklyn_effect)                
        self.event_list.append(Temp_path_brooklyn_effect)       
        label = QLabel(self.label_Image)
        pixmap = QPixmap(Temp_path_brooklyn_effect)
        width, height = im.size
        print(width)
        print(height)        
        if (width>height):   
            pix_map = pixmap.scaled(640, 480)
        else:
            pix_map = pixmap.scaled(320, 480)        
        self.label_Image.setAlignment(Qt.AlignCenter) # Aligns the displayed image in the middle
        self.label_Image.setPixmap(pix_map)  
        self.update_histogram(Temp_path_brooklyn_effect)
        self.update_rgb_channel(Temp_path_brooklyn_effect) 
        self.HSV_slider_status()

    
    def EarlyBird_effect(self):
        Temp_path = (os.getcwd()+"\\temp\\all_new.jpeg") 
        im = Image.open(Temp_path)
        Temp_path_earlybird_effect = (os.getcwd()+"\\temp\\EarlyBird_Effect.jpeg")
        pilgram.earlybird(im).save(Temp_path_earlybird_effect)              
        self.event_list.append(Temp_path_earlybird_effect)       
        label = QLabel(self.label_Image)
        pixmap = QPixmap(Temp_path_earlybird_effect)
        width, height = im.size
        print(width)
        print(height)
        
        if (width>height):   
            pix_map = pixmap.scaled(640, 480)
        else:
            pix_map = pixmap.scaled(320, 480)        
        self.label_Image.setAlignment(Qt.AlignCenter) # Aligns the displayed image in the middle
        self.label_Image.setPixmap(pix_map)  
        self.update_histogram(Temp_path_earlybird_effect)
        self.update_rgb_channel(Temp_path_earlybird_effect)  
        self.HSV_slider_status()
    
    
    def Hudson_effect(self):
        Temp_path = (os.getcwd()+"\\temp\\all_new.jpeg") 
        im = Image.open(Temp_path)
        Temp_path_Hudson_effect = (os.getcwd()+"\\temp\\Hudson_effect.jpeg")
        pilgram.hudson(im).save(Temp_path_Hudson_effect)                
        self.event_list.append(Temp_path_Hudson_effect)       
        label = QLabel(self.label_Image)
        pixmap = QPixmap(Temp_path_Hudson_effect)
        width, height = im.size
        print(width)
        print(height)
        
        if (width>height):   
            pix_map = pixmap.scaled(640, 480)
        else:
            pix_map = pixmap.scaled(320, 480)        
        self.label_Image.setAlignment(Qt.AlignCenter) # Aligns the displayed image in the middle
        self.label_Image.setPixmap(pix_map)  
        self.update_histogram(Temp_path_Hudson_effect)
        self.update_rgb_channel(Temp_path_Hudson_effect)   
        self.HSV_slider_status()
        
        
    def Kelvin_effect(self):
        Temp_path = (os.getcwd()+"\\temp\\all_new.jpeg")         
        img = cv2.imread(Temp_path)
        dst = cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)
        dimensions = img.shape
        width = img.shape[0]
        height = img.shape[1]
        channels = img.shape[2]
        Temp_path_kelvin_effect = (os.getcwd()+"\\temp\\kelvin_effect.jpeg")
        cv2.imwrite(Temp_path_kelvin_effect,dst)       
        self.event_list.append(Temp_path_kelvin_effect)       
        label = QLabel(self.label_Image)
        pixmap = QPixmap(Temp_path_kelvin_effect)
        print(width)
        print(height)
        
        if (width>height):   
            pix_map = pixmap.scaled(320, 480)
        else:
            pix_map = pixmap.scaled(640, 480)        
        self.label_Image.setAlignment(Qt.AlignCenter) # Aligns the displayed image in the middle
        self.label_Image.setPixmap(pix_map)  
        self.update_histogram(Temp_path_kelvin_effect)
        self.update_rgb_channel(Temp_path_kelvin_effect)          
        self.HSV_slider_status()
       

    def Nashville_effect(self):
        Temp_path = (os.getcwd()+"\\temp\\all_new.jpeg") 
        im = Image.open(Temp_path)
        Temp_path_Nashville_effect = (os.getcwd()+"\\temp\\Nashville_effect.jpeg")
        pilgram.nashville(im).save(Temp_path_Nashville_effect)             
        self.event_list.append(Temp_path_Nashville_effect)       
        label = QLabel(self.label_Image)
        pixmap = QPixmap(Temp_path_Nashville_effect)
        width, height = im.size
        print(width)
        print(height)        
        if (width>height):   
            pix_map = pixmap.scaled(640, 480)
        else:
            pix_map = pixmap.scaled(320, 480)        
        self.label_Image.setAlignment(Qt.AlignCenter) # Aligns the displayed image in the middle
        self.label_Image.setPixmap(pix_map)  
        self.update_histogram(Temp_path_Nashville_effect)
        self.update_rgb_channel(Temp_path_Nashville_effect)  
        self.HSV_slider_status()

# Function to set all the sliders to zero
    def set_sliders_to_zero(self):
        self.horizontalSlider_R.setValue(0)
        self.horizontalSlider_G.setValue(0)
        self.horizontalSlider_B.setValue(0)
        self.horizontalSlider_H.setValue(0)
        self.horizontalSlider_S.setValue(0)
        self.horizontalSlider_V.setValue(0)        
    
    def reset_image(self):
        path_reset_image = (os.getcwd()+"\\temp\\all_new.jpeg")        
        a1 = cv2.imread(path_reset_image)
        dimensions = a1.shape
        width = a1.shape[0]
        height = a1.shape[1]
        channels = a1.shape[2]              
        label = QLabel(self.label_Image)
        pixmap = QPixmap(path_reset_image)
        if (width>height):   
            pix_map = pixmap.scaled(320, 480)
        else:
            pix_map = pixmap.scaled(640, 480)                
        self.label_Image.setAlignment(Qt.AlignCenter)
        self.label_Image.setPixmap(pix_map)        
        self.update_histogram(path_reset_image)
        self.event_list.append(path_reset_image)
        self.update_rgb_channel(path_reset_image)
        self.set_sliders_to_zero()


    def rotate_img_right(self, path_to_rotate):
        Temp_path_to_rotate_resize = (os.getcwd()+"\\temp\\resized_rotated_right_img.jpeg")
        path_to_rotate = self.event_list[len(self.event_list)-1]
        a1 = cv2.imread(path_to_rotate)        
        img_rotate_90_clockwise = cv2.rotate(a1, cv2.ROTATE_90_CLOCKWISE)
        dimensions = img_rotate_90_clockwise.shape
        width = img_rotate_90_clockwise.shape[0]
        height = img_rotate_90_clockwise.shape[1]
        channels = img_rotate_90_clockwise.shape[2] 
        a2 = cv2.imwrite(Temp_path_to_rotate_resize,img_rotate_90_clockwise)                        
        self.event_list.append(Temp_path_to_rotate_resize)
        pixmap = QtGui.QPixmap(Temp_path_to_rotate_resize)   
        if (width>height):   
            pixmap = pixmap.scaled(320,480)
        else:
            pixmap = pixmap.scaled(640, 480)          
        self.label_Image.setAlignment(Qt.AlignCenter)
        self.label_Image.setPixmap(pixmap)
        self.HSV_slider_status()
       
    def rotate_img_left(self, path_to_rotate):
        Temp_path_to_rotate_resize = (os.getcwd()+"\\temp\\resized_rotated_left_img.jpeg")
        path_to_rotate = self.event_list[len(self.event_list)-1]
        a1 = cv2.imread(path_to_rotate)        
        img_rotate_90_counterclockwise = cv2.rotate(a1, cv2.ROTATE_90_COUNTERCLOCKWISE)
        dimensions = img_rotate_90_counterclockwise.shape
        width = img_rotate_90_counterclockwise.shape[0]
        height = img_rotate_90_counterclockwise.shape[1]
        channels = img_rotate_90_counterclockwise.shape[2] 
        cv2.imwrite(Temp_path_to_rotate_resize,img_rotate_90_counterclockwise)                
        self.event_list.append(Temp_path_to_rotate_resize)
        pixmap = QtGui.QPixmap(Temp_path_to_rotate_resize)
        if (width>height):   
            pixmap = pixmap.scaled(320,480)
        else:
            pixmap = pixmap.scaled(640, 480) 
        self.label_Image.setAlignment(Qt.AlignCenter)
        self.label_Image.setPixmap(pixmap)
        self.HSV_slider_status()

    def flip_image(self, path_to_flip):
        Temp_path_to_flip = (os.getcwd()+"\\temp\\flipped_image.jpeg")
        path_to_flip = self.event_list[len(self.event_list)-1]        
        a1 = cv2.imread(path_to_flip) 
        flipHorizontal = cv2.flip(a1, 1)        
        dimensions = flipHorizontal.shape
        width = flipHorizontal.shape[0]
        height = flipHorizontal.shape[1]
        channels = flipHorizontal.shape[2]                 
        cv2.imwrite(Temp_path_to_flip,flipHorizontal)                
        self.event_list.append(Temp_path_to_flip)                       
        label = QLabel(self.label_Image)
        pixmap = QPixmap(Temp_path_to_flip)
        if (width>height):   
            pixmap = pixmap.scaled(320,480)
        else:
            pixmap = pixmap.scaled(640, 480)        
        self.label_Image.setAlignment(Qt.AlignCenter)
        self.label_Image.setPixmap(pixmap)
        self.HSV_slider_status()

    def canny_edge_detection(self):
        Temp_path_gray_sacle = (os.getcwd()+"\\temp\\all_new.jpeg")        
        img = cv2.imread(Temp_path_gray_sacle)
        edges = cv2.Canny(img,100,200)
        Temp_path_edge_detection = (os.getcwd()+"\\temp\\edgedetect.jpeg")
        cv2.imwrite(Temp_path_edge_detection,edges)                
        dimensions = img.shape
        width = img.shape[0]
        height = img.shape[1]
        channels = img.shape[2]                
        self.event_list.append(Temp_path_edge_detection)                       
        label = QLabel(self.label_Image)
        pixmap = QPixmap(Temp_path_edge_detection)
        if (width>height):   
            pix_map = pixmap.scaled(320, 480)
        else:
            pix_map = pixmap.scaled(640, 480)          
        self.label_Image.setAlignment(Qt.AlignCenter)
        self.label_Image.setPixmap(pix_map)       
        self.update_rgb_channel(Temp_path_edge_detection)        
        self.HSV_slider_status()

    def harris_corner_detection(self):
        Temp_path = (os.getcwd()+"\\temp\\all_new.jpeg")       
        img = cv2.imread(Temp_path)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        gray = np.float32(gray)
        dst = cv2.cornerHarris(gray,2,3,0.04)       
        Temp_path_corner_detection = (os.getcwd()+"\\temp\\cornerdetect.jpeg")
        cv2.imwrite(Temp_path_corner_detection,dst)          
        dimensions = img.shape
        width = img.shape[0]
        height = img.shape[1]
        channels = img.shape[2]        
        self.event_list.append(Temp_path_corner_detection)               
        label = QLabel(self.label_Image)
        pixmap = QPixmap(Temp_path_corner_detection)        
        if (width>height):   
            pix_map = pixmap.scaled(320, 480)
        else:
            pix_map = pixmap.scaled(640, 480)              
        self.label_Image.setAlignment(Qt.AlignCenter)
        self.label_Image.setPixmap(pix_map)
        self.update_rgb_channel(Temp_path_corner_detection)
        self.HSV_slider_status()

    def saliency_map(self):
        Temp_path = (os.getcwd()+"\\temp\\all_new.jpeg")       
        img = cv2.imread(Temp_path)        
        saliency = cv2.saliency.StaticSaliencySpectralResidual_create()
        (success, saliencyMap) = saliency.computeSaliency(img)
        saliencyMap = (saliencyMap * 255).astype("uint8")
        Temp_path_Saliency_map = (os.getcwd()+"\\temp\\saliency_map.jpeg")
        cv2.imwrite(Temp_path_Saliency_map, saliencyMap)
        dimensions = img.shape
        width = img.shape[0]
        height = img.shape[1]
        channels = img.shape[2]                   
        self.event_list.append(Temp_path_Saliency_map)               
        label = QLabel(self.label_Image)
        pixmap = QPixmap(Temp_path_Saliency_map)        
        if (width>height):   
            pix_map = pixmap.scaled(320, 480)
        else:
            pix_map = pixmap.scaled(640, 480)              
        self.label_Image.setAlignment(Qt.AlignCenter)
        self.label_Image.setPixmap(pix_map)
        self.HSV_slider_status()
        
        
    def saliency_detection(self):
        Temp_path = (os.getcwd()+"\\temp\\all_new.jpeg")       
        img = cv2.imread(Temp_path)        
        fine_grain_saliency = cv2.saliency.StaticSaliencyFineGrained_create()
        (success, fine_grain_saliencyMap) = fine_grain_saliency.computeSaliency(img)        
        Temp_path_Saliency_detection = (os.getcwd()+"\\temp\\saliency_detect.jpeg")
        image = cv2.convertScaleAbs(fine_grain_saliencyMap, alpha=(255.0))
        cv2.imwrite(Temp_path_Saliency_detection, image)
        dimensions = img.shape
        width = img.shape[0]
        height = img.shape[1]
        channels = img.shape[2]           
        self.event_list.append(Temp_path_Saliency_detection)               
        label = QLabel(self.label_Image)
        pixmap = QPixmap(Temp_path_Saliency_detection)        
        if (width>height):   
            pix_map = pixmap.scaled(320, 480)
        else:
            pix_map = pixmap.scaled(640, 480)              
        self.label_Image.setAlignment(Qt.AlignCenter)
        self.label_Image.setPixmap(pix_map)
        self.HSV_slider_status()
                   

    def threshold_image(self):
        Temp_path = (os.getcwd()+"\\temp\\all_new.jpeg")       
        img = cv2.imread(Temp_path)        
        fine_grain_saliency = cv2.saliency.StaticSaliencyFineGrained_create()
        (success, saliencyMap) = fine_grain_saliency.computeSaliency(img)
        threshMap = cv2.threshold((saliencyMap*255).astype("uint8"), 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]        
        Temp_path_threshold_img = (os.getcwd()+"\\temp\\threshold_img.jpeg")
        cv2.imwrite(Temp_path_threshold_img, threshMap)
        dimensions = img.shape
        width = img.shape[0]
        height = img.shape[1]
        #channels = img.shape[2]                   
        self.event_list.append(Temp_path_threshold_img)               
        label = QLabel(self.label_Image)
        pixmap = QPixmap(Temp_path_threshold_img)        
        if (width>height):   
            pix_map = pixmap.scaled(320, 480)
        else:
            pix_map = pixmap.scaled(640, 480)              
        self.label_Image.setAlignment(Qt.AlignCenter)
        self.label_Image.setPixmap(pix_map)
        self.HSV_slider_status()
                           

    def update_rgb_channel(self,Temp_path):
        myimg = cv2.imread(Temp_path)        
        avg_color_per_row = np.average(myimg, axis=0)
        avg_color = np.average(avg_color_per_row, axis=0)
        print(avg_color)        
        self.r_channel, self.g_channel, self.b_channel = avg_color

        self.horizontalSlider_R.valueChanged.connect(self.change_r_values)
        self.horizontalSlider_G.valueChanged.connect(self.change_r_values)
        self.horizontalSlider_B.valueChanged.connect(self.change_r_values)
        self.horizontalSlider_H.valueChanged.connect(self.change_hsv)
        self.horizontalSlider_S.valueChanged.connect(self.change_hsv)
        self.horizontalSlider_V.valueChanged.connect(self.change_hsv)

    
    def change_r_values(self):        
        Temp_path = (os.getcwd()+"\\temp\\all_new.jpeg")
        a1 = cv2.imread(Temp_path)        
        dimensions = a1.shape
        width = a1.shape[0]
        height = a1.shape[1]
        channels = a1.shape[2]          
        
        path = (os.getcwd()+"\\temp\\trial.jpeg")
        red_channel = a1[:,:,2]
        green_channel = a1[:,:,1]
        blue_channel = a1[:,:,0]
                
        temp_img = np.zeros(a1.shape)
        temp_img[:,:,0] = a1[:,:,0]+self.horizontalSlider_B.value()
        temp_img[:,:,1] = a1[:,:,1]+self.horizontalSlider_G.value()
        temp_img[:,:,2] = a1[:,:,2]+ self.horizontalSlider_R.value()
        Temp_path_to_changed_rgb = (os.getcwd()+"\\temp\\rgb_image.jpeg")
        
        cv2.imwrite(Temp_path_to_changed_rgb,temp_img)       
        label = QLabel(self.label_Image)
        pixmap = QPixmap(Temp_path_to_changed_rgb)
        if (width>height):   
            pixmap = pixmap.scaled(320,480)
        else:
            pixmap = pixmap.scaled(640, 480)        
        self.label_Image.setAlignment(Qt.AlignCenter)
        self.label_Image.setPixmap(pixmap)        
        self.event_list.append(Temp_path_to_changed_rgb)     
        self.HSV_slider_status()

    def change_hsv(self):
        Temp_path = (os.getcwd()+"\\temp\\all_new.jpeg")
        a1 = cv2.imread(Temp_path)        
        dimensions = a1.shape
        width = a1.shape[0]
        height = a1.shape[1]
        channels = a1.shape[2]
        hsv_img = cv2.cvtColor(a1, cv2.COLOR_BGR2HSV)        
        temp_hsv = np.zeros(hsv_img.shape)
        temp_hsv[:,:,0] = hsv_img[:,:,0]+self.horizontalSlider_H.value()        
        temp_hsv[:,:,1] = hsv_img[:,:,1]+self.horizontalSlider_S.value()        
        temp_hsv[:,:,2] = hsv_img[:,:,2]+self.horizontalSlider_V.value()        
        
        Temp_path_to_changed_hsv = (os.getcwd()+"\\temp\\hsv_image.jpeg")
        cv2.imwrite(Temp_path_to_changed_hsv,temp_hsv)       

        label = QLabel(self.label_Image)
        pixmap = QPixmap(Temp_path_to_changed_hsv)
        if (width>height):   
            pixmap = pixmap.scaled(320,480)
        else:
            pixmap = pixmap.scaled(640, 480)        
        self.label_Image.setAlignment(Qt.AlignCenter)
        self.label_Image.setPixmap(pixmap)        
        self.event_list.append(Temp_path_to_changed_hsv)         


    def hsv_image(self):
        Temp_path = (os.getcwd()+"\\temp\\all_new.jpeg")
        a1 = cv2.imread(Temp_path)        
        dimensions = a1.shape
        width = a1.shape[0]
        height = a1.shape[1]
        channels = a1.shape[2]
        hsv_img = cv2.cvtColor(a1, cv2.COLOR_BGR2HSV)        
        Temp_path_to_hsv_img = (os.getcwd()+"\\temp\\Original_hsv_image.jpeg")
        cv2.imwrite(Temp_path_to_hsv_img,hsv_img)       
        label = QLabel(self.label_Image)
        pixmap = QPixmap(Temp_path_to_hsv_img)
        if (width>height):   
            pixmap = pixmap.scaled(320,480)
        else:
            pixmap = pixmap.scaled(640, 480)        
        self.label_Image.setAlignment(Qt.AlignCenter)
        self.label_Image.setPixmap(pixmap)        
        self.event_list.append(Temp_path_to_hsv_img)  
        self.HSV_slider_status()
       
        
    def save_image(self):
        path_to_img = self.event_list[len(self.event_list)-1]        
        a1 = cv2.imread(path_to_img)
        pathsave_custom = QFileDialog.getSaveFileName(None,"Save Image As()", "","All Files (*);;jpeg (*.jpg)") 
        cv2.imwrite(pathsave_custom[0],a1)


    def object_detection(self):

        #load yolo
        
        net = cv2.dnn.readNet(os.getcwd()+"\\yolov3.weights", os.getcwd()+"\\yolov3.cfg")
        classes = []
        with open(os.getcwd()+"\\coco.names", "r") as f:
            classes = [line.strip() for line in f.readlines()]
        #print(classes)    
        layer_names = net.getLayerNames()
        output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
        #colors = np.random.uniform(0, 255, size=(len(classes), 3))
        
        Temp_path = (os.getcwd()+"\\temp\\all_new.jpeg")

        # Loading image
        img = cv2.imread(Temp_path)
        #img = cv2.resize(img, None, fx=0.3, fy=0.3)
        height, width, channels = img.shape
        
        # Detecting objects
        
        # A Blob is a way to extract features from the image
        blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)        
        net.setInput(blob)
        outs = net.forward(output_layers)
        
        # Showing information on the screen
        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    #object detected
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                              
                    # Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)            
                                
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)
                    
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                labels = str(classes[class_ids[i]])
                #color = colors[i]
                cv2.rectangle(img, (x, y), (x + w, y + h), (0,255,0),2)
                cv2.putText(img, labels, (x, y + 30), font, 1,(255,255,255), 2)
                print(labels)
        
        Temp_path_to_object_detection = (os.getcwd()+"\\temp\\objectdetimage.jpeg")        
        cv2.imwrite(Temp_path_to_object_detection,img)
        
        #dimensions = img.shape
        width = img.shape[0]
        height = img.shape[1]
        #channels = img.shape[2]
        label = QLabel(self.label_Image)
        pixmap = QPixmap(Temp_path_to_object_detection)
        if (width>height):   
            pixmap = pixmap.scaled(320,480)
        else:
            pixmap = pixmap.scaled(640, 480)        
        self.label_Image.setAlignment(Qt.AlignCenter)
        self.label_Image.setPixmap(pixmap)        
        self.event_list.append(Temp_path_to_object_detection)  


def Exit_Window():
    
    try:        
        shutil.rmtree(os.getcwd()+"\\temp")        
    except:              
        pass
    
    MainWindow.close()  

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
