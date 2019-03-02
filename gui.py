# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'video_annotation_gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import run
import threading
import os
import cv2
import re
# from PyQt4.QtWidgets import QFileDialog
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(696, 486)
        MainWindow.setMinimumSize(QtCore.QSize(696, 486))
        MainWindow.setMaximumSize(QtCore.QSize(696, 486))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-1, -1, 691, 461))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.clips_extraction_tab = QtGui.QWidget()
        self.clips_extraction_tab.setObjectName(_fromUtf8("clips_extraction_tab"))
        self.textEditVideosFolderPath = QtGui.QPlainTextEdit(self.clips_extraction_tab)
        self.textEditVideosFolderPath.setGeometry(QtCore.QRect(120, 60, 301, 31))
        self.textEditVideosFolderPath.setObjectName(_fromUtf8("textEditVideosFolderPath"))
        self.textEditVideoPath = QtGui.QPlainTextEdit(self.clips_extraction_tab)
        self.textEditVideoPath.setGeometry(QtCore.QRect(120, 190, 301, 31))
        self.textEditVideoPath.setObjectName(_fromUtf8("textEditVideoPath"))
        self.spinBoxClipDuration = QtGui.QSpinBox(self.clips_extraction_tab)
        self.spinBoxClipDuration.setGeometry(QtCore.QRect(510, 10, 42, 22))
        self.spinBoxClipDuration.setMinimum(1)
        self.spinBoxClipDuration.setMaximum(100)
        self.spinBoxClipDuration.setObjectName(_fromUtf8("spinBoxClipDuration"))
        self.label = QtGui.QLabel(self.clips_extraction_tab)
        self.label.setGeometry(QtCore.QRect(345, 10, 121, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.btnBrowseVideosFolder = QtGui.QPushButton(self.clips_extraction_tab)
        self.btnBrowseVideosFolder.setGeometry(QtCore.QRect(450, 60, 91, 31))
        self.btnBrowseVideosFolder.setObjectName(_fromUtf8("btnBrowseVideosFolder"))
        self.btnBrowseVideo = QtGui.QPushButton(self.clips_extraction_tab)
        self.btnBrowseVideo.setGeometry(QtCore.QRect(450, 190, 91, 31))
        self.btnBrowseVideo.setObjectName(_fromUtf8("btnBrowseVideo"))
        self.label_2 = QtGui.QLabel(self.clips_extraction_tab)
        self.label_2.setGeometry(QtCore.QRect(20, 59, 101, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.clips_extraction_tab)
        self.label_3.setGeometry(QtCore.QRect(20, 189, 101, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.progressBarVideosFolder = QtGui.QProgressBar(self.clips_extraction_tab)
        self.progressBarVideosFolder.setGeometry(QtCore.QRect(120, 110, 301, 23))
        self.progressBarVideosFolder.setProperty("value", 99)
        self.progressBarVideosFolder.setObjectName(_fromUtf8("progressBarVideosFolder"))
        self.progressBarVideo = QtGui.QProgressBar(self.clips_extraction_tab)
        self.progressBarVideo.setGeometry(QtCore.QRect(120, 240, 301, 23))
        self.progressBarVideo.setProperty("value", 99)
        self.progressBarVideo.setObjectName(_fromUtf8("progressBarVideo"))
        self.btnStartClpipingFolderVideos = QtGui.QPushButton(self.clips_extraction_tab)
        self.btnStartClpipingFolderVideos.setGeometry(QtCore.QRect(450, 110, 91, 31))
        self.btnStartClpipingFolderVideos.setObjectName(_fromUtf8("btnStartClpipingFolderVideos"))
        self.btnStartClippingVideo = QtGui.QPushButton(self.clips_extraction_tab)
        self.btnStartClippingVideo.setGeometry(QtCore.QRect(450, 240, 91, 31))
        self.btnStartClippingVideo.setObjectName(_fromUtf8("btnStartClippingVideo"))
        self.tabWidget.addTab(self.clips_extraction_tab, _fromUtf8(""))
        self.videos_captioning_tab = QtGui.QWidget()
        self.videos_captioning_tab.setObjectName(_fromUtf8("videos_captioning_tab"))
        self.label_4 = QtGui.QLabel(self.videos_captioning_tab)
        self.label_4.setGeometry(QtCore.QRect(60, 19, 101, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.btnBrowseVideosCaptioningFolder = QtGui.QPushButton(self.videos_captioning_tab)
        self.btnBrowseVideosCaptioningFolder.setGeometry(QtCore.QRect(490, 20, 91, 31))
        self.btnBrowseVideosCaptioningFolder.setObjectName(_fromUtf8("btnBrowseVideosCaptioningFolder"))
        self.textEditVideosFolderCaptioningPath = QtGui.QPlainTextEdit(self.videos_captioning_tab)
        self.textEditVideosFolderCaptioningPath.setGeometry(QtCore.QRect(160, 20, 301, 31))
        self.textEditVideosFolderCaptioningPath.setObjectName(_fromUtf8("textEditVideosFolderCaptioningPath"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.videos_captioning_tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 60, 661, 361))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_5 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.listViewVideos = QtGui.QListView(self.horizontalLayoutWidget)
        self.listViewVideos.setObjectName(_fromUtf8("listViewVideos"))
        self.verticalLayout.addWidget(self.listViewVideos)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.btnNextVideo = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btnNextVideo.setObjectName(_fromUtf8("btnNextVideo"))
        self.verticalLayout_2.addWidget(self.btnNextVideo)
        self.btnPreviousVideo = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btnPreviousVideo.setObjectName(_fromUtf8("btnPreviousVideo"))
        self.verticalLayout_2.addWidget(self.btnPreviousVideo)
        self.btnPreviewVideo = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btnPreviewVideo.setObjectName(_fromUtf8("btnPreviewVideo"))
        self.verticalLayout_2.addWidget(self.btnPreviewVideo)
        self.btnCaptionCategories = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btnCaptionCategories.setObjectName(_fromUtf8("btnCaptionCategories"))
        self.verticalLayout_2.addWidget(self.btnCaptionCategories)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.lineEditCaption1 = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.lineEditCaption1.setObjectName(_fromUtf8("lineEditCaption1"))
        self.verticalLayout_3.addWidget(self.lineEditCaption1)
        self.lineEditCaption2 = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.lineEditCaption2.setObjectName(_fromUtf8("lineEditCaption2"))
        self.verticalLayout_3.addWidget(self.lineEditCaption2)
        self.lineEditCaption3 = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.lineEditCaption3.setObjectName(_fromUtf8("lineEditCaption3"))
        self.verticalLayout_3.addWidget(self.lineEditCaption3)
        self.lineEditCaption4 = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.lineEditCaption4.setObjectName(_fromUtf8("lineEditCaption4"))
        self.verticalLayout_3.addWidget(self.lineEditCaption4)
        self.lineEditCaption5 = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.lineEditCaption5.setObjectName(_fromUtf8("lineEditCaption5"))
        self.verticalLayout_3.addWidget(self.lineEditCaption5)
        self.btnSaveCaptions = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btnSaveCaptions.setObjectName(_fromUtf8("btnSaveCaptions"))
        self.verticalLayout_3.addWidget(self.btnSaveCaptions)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.videos_captioning_tab, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 696, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #####################################################
        ##          Custom Code Goes Below
        #####################################################
        self.videos_folder = None
        self.video_file = None
        self.clip_duration = 2
        self.data_dir = None
        self.current_index = 0
        self.data_videos = None
        self.captions_directory = None

        self.spinBoxClipDuration.valueChanged.connect(self.clipduration_changed)
        self.btnBrowseVideosFolder.clicked.connect(self.btnBrowseVideosFolder_clicked)
        self.btnBrowseVideo.clicked.connect(self.btnBrowseVideo_clicked)
        self.btnStartClpipingFolderVideos.clicked.connect(self.btnStartClpipingFolderVideos_clicked)
        self.btnStartClippingVideo.clicked.connect(self.btnStartClippingVideo_clicked)
        self.btnBrowseVideosCaptioningFolder.clicked.connect(self.btnBrowseDataDir_clicked)
        self.btnPreviewVideo.clicked.connect(self.btnPreviewVideo_clicked)
        self.btnNextVideo.clicked.connect(self.btnNextVideo_clicked)
        self.btnPreviousVideo.clicked.connect(self.btnPreviousVideo_clicked)
        self.btnSaveCaptions.clicked.connect(self.btnSaveCaptions_clicked)

    def WriteVideoCaption(self,c1, c2, c3, c4,c5):
        # get the name of the video file
        video_name = os.path.splitext(self.data_videos[self.current_index])[0] 
        file_name = os.path.splitext(self.data_videos[self.current_index])[0].split('_')[0]
        print(file_name + ".txt")
        print("Subclip Name: " + video_name)
        f = open(self.captions_directory + "\\"+ file_name + ".txt", "a+")

        f.write(video_name + " " + c1 + "\n")
        f.write(video_name + " " + c2 + "\n")
        f.write(video_name + " " + c3 + "\n")
        f.write(video_name + " " + c4 + "\n")
        f.write(video_name + " " + c5 + "\n")
        
        f.close()
        # open a file in append mode

        # write the caption line by line
    def btnSaveCaptions_clicked(self):
        caption1 = self.lineEditCaption1.text()
        caption2 = self.lineEditCaption2.text()
        caption3 = self.lineEditCaption3.text()
        caption4 = self.lineEditCaption4.text()
        caption5 = self.lineEditCaption5.text()
        print(caption1)
        print(caption2)
        print(caption3)
        print(caption4)
        print(caption5)
        self.WriteVideoCaption(caption1,caption2,caption3,caption4,caption5)
        self.ClearInputs()
        self.btnNextVideo_clicked()

    def ClearInputs(self):
        self.lineEditCaption1.setText("")
        self.lineEditCaption2.setText("")
        self.lineEditCaption3.setText("")
        self.lineEditCaption4.setText("")
        self.lineEditCaption5.setText("")

    def btnPreviewVideo_clicked(self):
        if (self.data_videos == None):
            self.ShowMessageBox("Error","No Videos Loaded")
            return
        video_index = self.data_dir + "\\" + self.data_videos[self.current_index]
        print(video_index)
        cap = cv2.VideoCapture(video_index)
        nframe = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        for x in range(int(nframe)):
            flag, frame = cap.read()
            if flag:
                res = cv2.resize(frame,(400, 400), interpolation = cv2.INTER_CUBIC)
                cv2.imshow('frame',res)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                  break
        cap.release()

    def btnNextVideo_clicked(self):
        if self.data_videos == None:
            self.ShowMessageBox("Error","No Videos Loaded")
            return
        if(self.current_index < len(self.data_videos) - 1):
            self.current_index = self.current_index + 1
            print(self.data_videos[self.current_index])
            self.label_5.setText("Selected Video -> " + self.data_videos[self.current_index])

    def btnPreviousVideo_clicked(self):
        if self.data_videos == None:
            self.ShowMessageBox("Error","No Videos Loaded")
            return
        if(self.current_index >= 0):
            self.current_index = self.current_index - 1
            print(self.data_videos[self.current_index])
            self.label_5.setText("Selected Video -> " + self.data_videos[self.current_index])

    def atoi(self, text):
        return int(text) if text.isdigit() else text

    def natural_keys(self, text):
        return [ self.atoi(c) for c in re.split(r'(\d+)', text) ]

    def UpdateVideosList(self):
        self.data_videos = os.listdir(self.data_dir)
        self.data_videos.sort(key=self.natural_keys)
        model = QtGui.QStandardItemModel()
        self.listViewVideos.setModel(model)
        for i in self.data_videos:
            if(i.endswith('.mp4') or i.endswith('.avi')):
                item = QtGui.QStandardItem(i)
                model.appendRow(item)
        self.label_5.setText("Selected Video -> " + self.data_videos[0])
    def btnBrowseVideosFolder_clicked(self):
        folder = QtGui.QFileDialog.getExistingDirectory(None,'Select Videos Folder')
        if folder != None:
            print("[INFO]... " + str(folder))
            self.videos_folder = str(folder)
            self.textEditVideosFolderPath.insertPlainText(self.videos_folder)
        else:
            return
    def btnBrowseDataDir_clicked(self):
        folder = QtGui.QFileDialog.getExistingDirectory(None,'Select Data Folder')
        if folder:
            print("[INFO]... " + str(folder))
            self.data_dir = str(folder)
            self.textEditVideosFolderCaptioningPath.insertPlainText(self.data_dir)
            self.captions_directory = self.data_dir + "\\captions"
            if not os.path.exists(self.captions_directory):
                os.makedirs(self.captions_directory)
            self.UpdateVideosList()
        else:
            return
    def btnBrowseVideo_clicked(self):
        video_file = QtGui.QFileDialog.getOpenFileName(None,'Select Video', filter='Video Files (*.mp4)')
        if(video_file):
            print("[INFO]... " + str(video_file))
            self.video_file = str(video_file)
            self.textEditVideoPath.insertPlainText(self.video_file)
        else:
            return
    def btnStartClpipingFolderVideos_clicked(self):
        if(self.videos_folder == None):
            self.ShowMessageBox("Error Message","No Videos Folder Selected")
            return
        threading.Thread(target=self.ClippingFolderThread).start()
    def ClippingFolderThread(self):
        if(run.BatchProcessor(self.videos_folder, self.clip_duration)):
            self.ShowMessageBox("Success!!","Video Clips Generated Successfully")

    def btnStartClippingVideo_clicked(self):
        if(self.video_file == None):
            self.ShowMessageBox("Error Message","No Video File Selected")
            return
        threading.Thread(target=self.ClippingVideoThread).start()

    def ClippingVideoThread(self):
        if(run.OneVideo(self.video_file, self.clip_duration)):
            self.ShowMessageBox("Success!!","Video Clips Generated Successfully")

    def ShowMessageBox(self,type,err_msg):
        QtGui.QMessageBox.about(None, type, err_msg)
    def clipduration_changed(self):
        self.clip_duration = self.spinBoxClipDuration.value()
        print("[INFO]... Per Clip Duration: " + str(self.clip_duration))

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Video Annotator", None))
        self.label.setText(_translate("MainWindow", "Clip Duration (seconds)", None))
        self.btnBrowseVideosFolder.setText(_translate("MainWindow", "Browse Folder", None))
        self.btnBrowseVideo.setText(_translate("MainWindow", "Browse Video", None))
        self.label_2.setText(_translate("MainWindow", "Videos Folder", None))
        self.label_3.setText(_translate("MainWindow", "Single Video", None))
        self.btnStartClpipingFolderVideos.setText(_translate("MainWindow", "Start Clipping", None))
        self.btnStartClippingVideo.setText(_translate("MainWindow", "Start Clipping", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.clips_extraction_tab), _translate("MainWindow", "Video Clips Extraction", None))
        self.label_4.setText(_translate("MainWindow", "Videos Folder", None))
        self.btnBrowseVideosCaptioningFolder.setText(_translate("MainWindow", "Browse Folder", None))
        self.label_5.setText(_translate("MainWindow", "Selected Videos", None))
        self.btnNextVideo.setText(_translate("MainWindow", "Next Video", None))
        self.btnPreviousVideo.setText(_translate("MainWindow", "Previous Video", None))
        self.btnPreviewVideo.setText(_translate("MainWindow", "Preview Video", None))
        self.btnCaptionCategories.setText(_translate("MainWindow", "Caption Categories", None))
        self.lineEditCaption1.setPlaceholderText(_translate("MainWindow", "Caption 1", None))
        self.lineEditCaption2.setPlaceholderText(_translate("MainWindow", "Caption 2", None))
        self.lineEditCaption3.setPlaceholderText(_translate("MainWindow", "Caption 3", None))
        self.lineEditCaption4.setPlaceholderText(_translate("MainWindow", "Caption 4", None))
        self.lineEditCaption5.setPlaceholderText(_translate("MainWindow", "Caption 5", None))
        self.btnSaveCaptions.setText(_translate("MainWindow", "Save Captions", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.videos_captioning_tab), _translate("MainWindow", "Videos Captioning", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

